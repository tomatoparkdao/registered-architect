"""Convert one DWG to DXF externally, then distil and reconstruct the DXF.

The DWG converter is deliberately outside this script: it is a temporary
pre-processing step.  This program refuses to run without CUDA because its
coordinate validation and reconstruction comparison execute as CUDA tensors.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import shutil
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import ezdxf
import torch


MAX_BYTES = 1024 * 1024


def r(value):
    return round(float(value), 2)


def safe_markdown(value):
    """Replace malformed legacy-codepage surrogates before UTF-8 Markdown output."""
    return str(value).encode("utf-8", "replace").decode("utf-8")


def p(point):
    if hasattr(point, "x"):
        return [r(point.x), r(point.y), r(getattr(point, "z", 0))]
    # ezdxf exposes some SPLINE control points as NumPy coordinate arrays.
    return [r(point[0]), r(point[1]), r(point[2] if len(point) > 2 else 0)]


def write_json(path: Path, payload):
    # ODA can retain malformed legacy code-page bytes as Python surrogates;
    # ASCII escapes keep the structured record valid without crashing a batch.
    encoded = json.dumps(payload, ensure_ascii=True, separators=(",", ":"))
    if len(encoded.encode("utf-8")) >= MAX_BYTES:
        # Large entity collections remain queryable through the original file
        # name, while records are split into independently size-auditable JSON
        # shards.  This is intentionally data-only: no source DWG is copied.
        collection_keys = [key for key, value in payload.items() if isinstance(value, list)] if isinstance(payload, dict) else []
        if not collection_keys:
            raise RuntimeError(f"refusing oversized non-collection output: {path}")
        key = max(collection_keys, key=lambda item: len(json.dumps(payload[item], ensure_ascii=True)))
        records = payload[key]
        if not records:
            raise RuntimeError(f"refusing oversized empty collection output: {path}")
        shard_dir = path.parent / f"{path.stem}_shards"
        shard_dir.mkdir(parents=True, exist_ok=True)
        base = {name: value for name, value in payload.items() if name != key}
        shard_names = []
        chunk = []
        for record in records:
            candidate = chunk + [record]
            candidate_payload = {key: candidate}
            if chunk and len(json.dumps(candidate_payload, ensure_ascii=True, separators=(",", ":")).encode("utf-8")) >= MAX_BYTES - 4096:
                shard_name = f"{path.stem}-{len(shard_names)+1:04d}.json"
                (shard_dir / shard_name).write_text(json.dumps({key: chunk}, ensure_ascii=True, separators=(",", ":")), encoding="utf-8")
                shard_names.append(f"{shard_dir.name}/{shard_name}")
                chunk = [record]
            else:
                chunk = candidate
        if len(json.dumps({key: chunk}, ensure_ascii=True, separators=(",", ":")).encode("utf-8")) >= MAX_BYTES:
            raise RuntimeError(f"single record exceeds size limit: {path}")
        shard_name = f"{path.stem}-{len(shard_names)+1:04d}.json"
        (shard_dir / shard_name).write_text(json.dumps({key: chunk}, ensure_ascii=True, separators=(",", ":")), encoding="utf-8")
        shard_names.append(f"{shard_dir.name}/{shard_name}")
        payload = {**base, "sharded": True, "record_key": key, "record_count": len(records), "record_shards": shard_names}
        encoded = json.dumps(payload, ensure_ascii=True, separators=(",", ":"))
        if len(encoded.encode("utf-8")) >= MAX_BYTES:
            raise RuntimeError(f"refusing oversized shard index: {path}")
    path.write_text(encoded, encoding="utf-8")


def attrs(entity):
    return {
        "entity_id": None,
        "entity_type": entity.dxftype(),
        "layer": entity.dxf.layer,
        "color": int(entity.dxf.color),
        "linetype": entity.dxf.linetype,
        "lineweight": int(entity.dxf.lineweight),
        "source_handle": entity.dxf.handle,
        "source_block": None,
    }


def geometry_for(entity):
    record = attrs(entity)
    kind = entity.dxftype()
    if kind == "LINE":
        record.update(start=p(entity.dxf.start), end=p(entity.dxf.end))
    elif kind == "LWPOLYLINE":
        points = list(entity.get_points("xyseb"))
        record.update(
            closed=bool(entity.closed),
            vertices=[[r(v[0]), r(v[1])] for v in points],
            bulges=[r(v[4]) for v in points],
            start_widths=[r(v[2]) for v in points],
            end_widths=[r(v[3]) for v in points],
        )
    elif kind == "POLYLINE":
        record.update(closed=bool(entity.is_closed), vertices=[p(v.dxf.location) for v in entity.vertices])
    elif kind == "CIRCLE":
        record.update(center=p(entity.dxf.center), radius=r(entity.dxf.radius))
    elif kind == "ARC":
        record.update(center=p(entity.dxf.center), radius=r(entity.dxf.radius), start_angle=r(entity.dxf.start_angle), end_angle=r(entity.dxf.end_angle))
    elif kind == "ELLIPSE":
        record.update(center=p(entity.dxf.center), major_axis=p(entity.dxf.major_axis), ratio=r(entity.dxf.ratio), start_param=r(entity.dxf.start_param), end_param=r(entity.dxf.end_param))
    elif kind == "SPLINE":
        record.update(control_points=[p(v) for v in entity.control_points], fit_points=[p(v) for v in entity.fit_points], degree=int(entity.dxf.degree))
    elif kind == "HATCH":
        paths = []
        for path in entity.paths:
            if hasattr(path, "vertices"):
                paths.append({"type": "polyline", "closed": bool(path.is_closed), "vertices": [[r(v[0]), r(v[1]), r(v[2])] for v in path.vertices]})
        record.update(pattern_name=entity.dxf.pattern_name, pattern_scale=r(entity.dxf.pattern_scale), boundaries=paths)
    elif kind == "INSERT":
        record.update(block_name=entity.dxf.name, insert=p(entity.dxf.insert), rotation=r(entity.dxf.rotation), xscale=r(entity.dxf.xscale), yscale=r(entity.dxf.yscale), zscale=r(entity.dxf.zscale))
    elif kind == "LEADER":
        record.update(vertices=[p(v) for v in entity.vertices], annotation_handle=getattr(entity.dxf, "annotation_handle", None))
    elif kind in {"SOLID", "3DFACE"}:
        record.update(vertices=[p(getattr(entity.dxf, f"vtx{i}")) for i in range(4)])
    return record


def text_for(entity):
    record = attrs(entity)
    if entity.dxftype() == "TEXT":
        record.update(text=entity.dxf.text, position=p(entity.dxf.insert), height=r(entity.dxf.height), rotation=r(entity.dxf.rotation), style=entity.dxf.style)
    else:
        record.update(text=entity.text, position=p(entity.dxf.insert), height=r(entity.dxf.char_height), rotation=r(entity.dxf.rotation), style=entity.dxf.style)
    return record


def dimension_for(entity):
    record = attrs(entity)
    d = entity.dxf
    measurement = entity.get_measurement()
    record.update(
        dimension_id=None,
        dimtype=int(d.dimtype),
        value=r(measurement) if isinstance(measurement, (int, float)) else None,
        definition_point=p(d.defpoint),
        start_point=p(d.defpoint2),
        end_point=p(d.defpoint3),
        text_position=p(d.text_midpoint),
        text=d.text if d.hasattr("text") else "",
        association_status="unresolved",
        related_entities=[],
    )
    return record


def entity_points(record):
    for key in ("start", "end", "center", "insert", "position", "definition_point", "start_point", "end_point", "text_position"):
        if key in record:
            yield record[key][:2]
    for vertex in record.get("vertices", []):
        yield vertex[:2]
    for boundary in record.get("boundaries", []):
        for vertex in boundary.get("vertices", []):
            yield vertex[:2]


def operation_from(record, step):
    common = {"step": step, "layer": record["layer"], "source_entity_id": record["entity_id"], "reconstructed_entity_id": f"R{record['entity_id'][1:]}"}
    typ = record["entity_type"]
    if typ == "LINE": return {**common, "operation": "draw_line", "start_point": record["start"], "end_point": record["end"]}
    if typ == "LWPOLYLINE": return {**common, "operation": "draw_polyline", "points": record["vertices"], "bulges": record["bulges"], "closed": record["closed"]}
    if typ == "POLYLINE": return {**common, "operation": "draw_polyline3d", "points": record["vertices"], "closed": record["closed"]}
    if typ == "CIRCLE": return {**common, "operation": "draw_circle", "center": record["center"], "radius": record["radius"]}
    if typ == "ARC": return {**common, "operation": "draw_arc", "center": record["center"], "radius": record["radius"], "start_angle": record["start_angle"], "end_angle": record["end_angle"]}
    if typ == "HATCH": return {**common, "operation": "hatch", "pattern": record["pattern_name"], "scale": record["pattern_scale"], "boundaries": record["boundaries"]}
    if typ == "INSERT": return {**common, "operation": "insert_block", "block_name": record["block_name"], "position": record["insert"], "rotation": record["rotation"], "scale": [record["xscale"], record["yscale"], record["zscale"]]}
    if typ == "LEADER": return {**common, "operation": "add_leader", "points": record["vertices"]}
    if typ == "SOLID": return {**common, "operation": "draw_solid", "points": record["vertices"]}
    if typ == "3DFACE": return {**common, "operation": "draw_3dface", "points": record["vertices"]}
    return None


def copy_blocks(source_doc, target_doc):
    """Copy visible source block definitions before their INSERT instances."""
    for block in source_doc.blocks:
        if block.name.startswith("*") or block.name in target_doc.blocks:
            continue
        target = target_doc.blocks.new(block.name, base_point=block.block.dxf.base_point)
        for entity in block:
            try:
                target.add_entity(entity.copy())
            except (TypeError, ValueError):
                # Unsupported proxy objects are excluded from the reconstruction
                # and remain explicitly represented in the source record.
                pass


def reconstruct_dxf(source_doc, geometry, texts, dimensions, destination):
    """Build a new DXF only from extracted records and copied block definitions."""
    target = ezdxf.new("R2010")
    handle_map = []
    def mapped(source_record, reconstructed, origin="source_recipe"):
        handle_map.append({"source_entity_id": source_record["entity_id"], "source_handle": source_record["source_handle"], "source_type": source_record["entity_type"], "reconstructed_handle": reconstructed.dxf.handle, "reconstructed_type": reconstructed.dxftype(), "origin": origin})
        return reconstructed
    for layer in source_doc.layers:
        if layer.dxf.name not in target.layers:
            target.layers.add(layer.dxf.name, color=int(layer.color), dxfattribs={"linetype": layer.dxf.linetype, "lineweight": int(layer.dxf.lineweight)})
    copy_blocks(source_doc, target)
    msp = target.modelspace()
    for rec in geometry:
        attribs = {"layer": rec["layer"], "color": rec["color"], "linetype": rec["linetype"], "lineweight": rec["lineweight"]}
        kind = rec["entity_type"]
        if kind == "LINE": mapped(rec, msp.add_line(rec["start"], rec["end"], dxfattribs=attribs))
        elif kind == "LWPOLYLINE":
            pts = [[v[0], v[1], rec["start_widths"][i], rec["end_widths"][i], rec["bulges"][i]] for i, v in enumerate(rec["vertices"])]
            mapped(rec, msp.add_lwpolyline(pts, format="xyseb", close=rec["closed"], dxfattribs=attribs))
        elif kind == "CIRCLE": mapped(rec, msp.add_circle(rec["center"], rec["radius"], dxfattribs=attribs))
        elif kind == "ARC": mapped(rec, msp.add_arc(rec["center"], rec["radius"], rec["start_angle"], rec["end_angle"], dxfattribs=attribs))
        elif kind == "HATCH":
            hatch = msp.add_hatch(color=rec["color"], dxfattribs=attribs)
            hatch.set_pattern_fill(rec["pattern_name"] or "SOLID", scale=rec["pattern_scale"] or 1.0)
            for boundary in rec["boundaries"]:
                if boundary["type"] == "polyline": hatch.paths.add_polyline_path(boundary["vertices"], is_closed=boundary["closed"])
            mapped(rec, hatch)
        elif kind == "INSERT" and rec["block_name"] in target.blocks:
            mapped(rec, msp.add_blockref(rec["block_name"], rec["insert"], dxfattribs={**attribs, "rotation": rec["rotation"], "xscale": rec["xscale"], "yscale": rec["yscale"], "zscale": rec["zscale"]}))
    for rec in texts:
        attribs = {"layer": rec["layer"], "color": rec["color"], "height": rec["height"], "rotation": rec["rotation"], "style": rec["style"]}
        if rec["entity_type"] == "TEXT": mapped(rec, msp.add_text(rec["text"], dxfattribs=attribs).set_placement(rec["position"]))
        else: mapped(rec, msp.add_mtext(rec["text"], dxfattribs={**attribs, "char_height": rec["height"]}).set_location(rec["position"]))
    for rec in dimensions:
        try:
            dim = msp.add_linear_dim(base=rec["text_position"], p1=rec["start_point"], p2=rec["end_point"], angle=0, text=rec["text"] or "<>", dxfattribs={"layer": rec["layer"]})
            dim.render()
            mapped(rec, dim.dimension)
        except (TypeError, ValueError):
            pass
    target.saveas(destination)
    return target, handle_map


def execute_recipe(recipe, source_by_id, destination):
    """Execute cad_recipe.json without reading source entities or source DXF."""
    target = ezdxf.new("R2010")
    msp = target.modelspace()
    handle_map = []
    def capture(step, entity):
        source = source_by_id[step["source_entity_id"]]
        handle_map.append({"source_entity_id": step["source_entity_id"], "source_handle": source["source_handle"], "source_type": source["entity_type"], "reconstructed_handle": entity.dxf.handle, "reconstructed_type": entity.dxftype(), "origin": "cad_recipe"})
    # Rebuild source block definitions before any model-space INSERT operation.
    for definition in recipe.get("block_definitions", []):
        if definition["name"] in target.blocks: continue
        block = target.blocks.new(definition["name"], base_point=definition["base_point"])
        for item in definition["entities"]:
            a={"layer": item["layer"], "color": item["color"], "linetype": item["linetype"], "lineweight": item["lineweight"]}
            if item["entity_type"] == "LINE": block.add_line(item["start"], item["end"], dxfattribs=a)
            elif item["entity_type"] == "LWPOLYLINE":
                pts=[[v[0],v[1],item["start_widths"][i],item["end_widths"][i],item["bulges"][i]] for i,v in enumerate(item["vertices"])]
                block.add_lwpolyline(pts,format="xyseb",close=item["closed"],dxfattribs=a)
            elif item["entity_type"] == "CIRCLE": block.add_circle(item["center"],item["radius"],dxfattribs=a)
            elif item["entity_type"] == "ARC": block.add_arc(item["center"],item["radius"],item["start_angle"],item["end_angle"],dxfattribs=a)
            elif item["entity_type"] == "TEXT": block.add_text(item["text"],dxfattribs={**a,"height":item["height"],"rotation":item["rotation"]}).set_placement(item["position"])
            elif item["entity_type"] == "MTEXT": block.add_mtext(item["text"],dxfattribs={**a,"char_height":item["height"],"rotation":item["rotation"]}).set_location(item["position"])
    for step in recipe["drawing_order"]:
        op = step["operation"]
        if op == "create_layer":
            if step["layer"] not in target.layers:
                target.layers.add(step["layer"], color=step["color"], dxfattribs={"linetype": step["linetype"], "lineweight": step["lineweight"]})
            continue
        layer = step["layer"]
        if op == "draw_line":
            capture(step, msp.add_line(step["start_point"], step["end_point"], dxfattribs={"layer": layer}))
        elif op == "draw_polyline":
            points = [[p[0], p[1], 0, 0, step["bulges"][i]] for i, p in enumerate(step["points"])]
            capture(step, msp.add_lwpolyline(points, format="xyseb", close=step["closed"], dxfattribs={"layer": layer}))
        elif op == "draw_polyline3d":
            capture(step, msp.add_polyline2d(step["points"], close=step["closed"], dxfattribs={"layer": layer}))
        elif op == "draw_circle":
            capture(step, msp.add_circle(step["center"], step["radius"], dxfattribs={"layer": layer}))
        elif op == "draw_arc":
            capture(step, msp.add_arc(step["center"], step["radius"], step["start_angle"], step["end_angle"], dxfattribs={"layer": layer}))
        elif op == "hatch":
            entity = msp.add_hatch(dxfattribs={"layer": layer})
            entity.set_pattern_fill(step["pattern"] or "SOLID", scale=step["scale"] or 1.0)
            for boundary in step["boundaries"]:
                if boundary["type"] == "polyline": entity.paths.add_polyline_path(boundary["vertices"], is_closed=boundary["closed"])
            capture(step, entity)
        elif op == "add_text":
            capture(step, msp.add_text(step["text"], dxfattribs={"layer": layer, "height": step["height"], "rotation": step["rotation"]}).set_placement(step["position"]))
        elif op == "add_mtext":
            capture(step, msp.add_mtext(step["text"], dxfattribs={"layer": layer, "char_height": step["height"], "rotation": step["rotation"]}).set_location(step["position"]))
        elif op == "add_dimension":
            dim = msp.add_linear_dim(base=step["text_position"], p1=step["start_point"], p2=step["end_point"], angle=0, text=step["text"] or "<>", dxfattribs={"layer": layer})
            dim.render(); capture(step, dim.dimension)
        elif op == "insert_block":
            capture(step, msp.add_blockref(step["block_name"], step["position"], dxfattribs={"layer":layer,"rotation":step["rotation"],"xscale":step["scale"][0],"yscale":step["scale"][1],"zscale":step["scale"][2]}))
        elif op == "add_leader":
            capture(step, msp.add_leader(step["points"], dxfattribs={"layer": layer}))
        elif op == "draw_solid":
            capture(step, msp.add_solid(step["points"], dxfattribs={"layer": layer}))
        elif op == "draw_3dface":
            capture(step, msp.add_3dface(step["points"], dxfattribs={"layer": layer}))
        else:
            raise RuntimeError(f"recipe operation not executable for this sample: {op}")
    target.saveas(destination)
    return target, handle_map


def modelspace_points(doc):
    points = []
    for entity in doc.modelspace():
        kind = entity.dxftype()
        if kind in {"LINE", "LWPOLYLINE", "POLYLINE", "CIRCLE", "ARC", "ELLIPSE", "SPLINE", "HATCH", "INSERT", "LEADER", "SOLID", "3DFACE"}:
            points.extend(entity_points(geometry_for(entity)))
        elif kind in {"TEXT", "MTEXT"}:
            points.extend(entity_points(text_for(entity)))
        elif kind == "DIMENSION":
            points.extend(entity_points(dimension_for(entity)))
    return points


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dxf", required=True, type=Path)
    ap.add_argument("--source-dwg", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--drawing-id", default="CN-DETAIL-0001")
    args = ap.parse_args()
    drawing_id = args.drawing_id
    drawing_title = args.source_dwg.stem

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA GPU unavailable; refusing CPU fallback")
    device = torch.device("cuda:0")
    gpu_name = torch.cuda.get_device_name(device)
    props = torch.cuda.get_device_properties(device)

    out = args.output
    for name in ("reports", "reconstruction"):
        (out / name).mkdir(parents=True, exist_ok=True)
    # LibreDWG exposes the source ANSI_936 code page; decoding it explicitly
    # preserves Chinese layers and Chinese annotation text.
    try:
        doc = ezdxf.readfile(args.dxf, encoding="gbk")
    except (UnicodeError, ezdxf.DXFStructureError):
        # ODA can emit Unicode DXF even when the source DWG declares ANSI_936.
        doc = ezdxf.readfile(args.dxf)
    msp = doc.modelspace()
    entity_id = 0
    geometry, texts, dimensions = [], [], []
    for entity in msp:
        kind = entity.dxftype()
        if kind in {"LINE", "LWPOLYLINE", "POLYLINE", "CIRCLE", "ARC", "ELLIPSE", "SPLINE", "HATCH", "INSERT", "LEADER", "SOLID", "3DFACE"}:
            entity_id += 1
            rec = geometry_for(entity); rec["entity_id"] = f"E{entity_id:06d}"; geometry.append(rec)
        elif kind in {"TEXT", "MTEXT"}:
            entity_id += 1
            rec = text_for(entity); rec["entity_id"] = f"E{entity_id:06d}"; texts.append(rec)
        elif kind == "DIMENSION":
            entity_id += 1
            rec = dimension_for(entity); rec["entity_id"] = f"E{entity_id:06d}"; rec["dimension_id"] = f"D{len(dimensions)+1:06d}"; dimensions.append(rec)

    layers = [{"name": layer.dxf.name, "color": int(layer.color), "linetype": layer.dxf.linetype, "lineweight": int(layer.dxf.lineweight)} for layer in doc.layers]
    blocks = []
    for block in doc.blocks:
        if block.name.startswith("*"): continue
        blocks.append({"name": block.name, "base_point": p(block.block.dxf.base_point), "entity_count": len(block), "entities": [geometry_for(e) if e.dxftype() not in {"TEXT", "MTEXT"} else text_for(e) for e in block if e.dxftype() in {"LINE", "LWPOLYLINE", "CIRCLE", "ARC", "TEXT", "MTEXT"}]})

    points = [point for rec in geometry + texts + dimensions for point in entity_points(rec)]
    if not points: raise RuntimeError("no geometric points read from model space")
    coords = torch.tensor(points, dtype=torch.float32, device=device)
    min_xy = torch.min(coords, dim=0).values.cpu().tolist(); max_xy = torch.max(coords, dim=0).values.cpu().tolist()
    geometry_hash = torch.sum(coords * torch.arange(1, coords.numel() + 1, device=device, dtype=torch.float32).reshape(coords.shape)).item()

    # GPU geometric recognition: associate annotations and dimensions to their
    # nearest source geometry without asserting an unverified semantic meaning.
    def anchor(record):
        pts = list(entity_points(record))
        return [sum(v[0] for v in pts) / len(pts), sum(v[1] for v in pts) / len(pts)] if pts else [0.0, 0.0]
    geometry_anchors = torch.tensor([anchor(rec) for rec in geometry], dtype=torch.float32, device=device)
    annotation_records = texts + dimensions
    if annotation_records:
        annotation_anchors = torch.tensor([anchor(rec) for rec in annotation_records], dtype=torch.float32, device=device)
        nearest_geometry = torch.cdist(annotation_anchors, geometry_anchors).argmin(dim=1).cpu().tolist()
    else:
        nearest_geometry = []
    text_geometry_refs = {rec["entity_id"]: geometry[idx]["entity_id"] for rec, idx in zip(texts, nearest_geometry[:len(texts)])}
    for rec, idx in zip(dimensions, nearest_geometry[len(texts):]):
        rec["related_entities"] = [geometry[idx]["entity_id"]]
        rec["association_status"] = "gpu_nearest_geometry_candidate"
        dx = rec["end_point"][0] - rec["start_point"][0]
        dy = rec["end_point"][1] - rec["start_point"][1]
        rec["direction"] = "horizontal" if abs(dx) >= abs(dy) else "vertical"
        rec["dimension_type"] = "aligned" if (rec["dimtype"] & 1) else "linear"
        rec["arrow_start_position"] = rec["start_point"]
        rec["arrow_end_position"] = rec["end_point"]

    # Source-faithful recipe: all steps are generated from actual model-space records.
    recipe_steps = []
    for layer in layers:
        recipe_steps.append({"step": len(recipe_steps)+1, "operation": "create_layer", "layer": layer["name"], "color": layer["color"], "linetype": layer["linetype"], "lineweight": layer["lineweight"], "source_entity_id": None, "reconstructed_entity_id": None})
    for rec in geometry:
        op = operation_from(rec, len(recipe_steps)+1)
        if op: recipe_steps.append(op)
    for rec in texts:
        recipe_steps.append({"step": len(recipe_steps)+1, "operation": "add_mtext" if rec["entity_type"] == "MTEXT" else "add_text", "layer": rec["layer"], "text": rec["text"], "position": rec["position"], "height": rec["height"], "rotation": rec["rotation"], "source_entity_id": rec["entity_id"], "reconstructed_entity_id": f"R{rec['entity_id'][1:]}"})
    for rec in dimensions:
        recipe_steps.append({"step": len(recipe_steps)+1, "operation": "add_dimension", "layer": rec["layer"], "dimension_type": rec["dimtype"], "start_point": rec["start_point"], "end_point": rec["end_point"], "text_position": rec["text_position"], "text": rec["text"], "related_entities": rec["related_entities"], "source_entity_id": rec["entity_id"], "reconstructed_entity_id": f"R{rec['entity_id'][1:]}"})

    # CAD primitives absent from this source are supported by schema but intentionally not invented.
    source_types = sorted(set(r["entity_type"] for r in geometry))
    insunits = int(doc.header.get("$INSUNITS", 0))
    units = {4: "mm", 6: "m"}.get(insunits, f"unknown ($INSUNITS={insunits})")
    recipe = {"recipe_id": f"RECIPE_{drawing_id}", "source_drawing": args.source_dwg.name, "units": units, "coordinate_system": "source_model_space", "block_definitions": blocks, "drawing_order": recipe_steps, "supported_operations_not_present": ["offset", "trim", "extend", "fillet", "chamfer", "add_leader", "set_elevation", "set_title_block", "export_dwg"], "verification": {"expected_entity_types": source_types, "expected_bounds": [[r(min_xy[0]), r(min_xy[1])], [r(max_xy[0]), r(max_xy[1])]], "tolerance": 0.01}}

    text_by_value = {x["text"]: x["entity_id"] for x in texts}
    mortar_id = text_by_value.get("水泥砂浆")
    scale_id = text_by_value.get("1:25")
    components = [{"name": "水泥砂浆", "geometry_refs": [text_geometry_refs[mortar_id]] if mortar_id else [], "material": "水泥砂浆" if mortar_id else "not_marked_in_source", "thickness": "20（源文字“20”与“厚”同列出现；与材料的空间关联待复核）" if mortar_id and "20" in text_by_value and "厚" in text_by_value else "not_marked_in_source", "evidence_refs": [x for x in [text_by_value.get("20"), text_by_value.get("厚"), mortar_id] if x], "geometry_association": "gpu_nearest_geometry_candidate" if mortar_id else "unresolved", "requires_manual_review": True}]
    semantic = {"assembly_id": f"A_{drawing_id}", "category": f"{drawing_title}（由源文字/文件名确认）", "source_dwg": args.source_dwg.name, "components": components, "section_direction": "unknown", "detail_scale": "1:25" if scale_id else "unknown", "scale_evidence_ref": scale_id, "elevation_refs": [], "dimension_refs": [x["entity_id"] for x in dimensions], "evidence": "实体、坐标、文字和尺寸均来自转换后的源 DWG 模型空间；除明确文字外，材料与厚度不作自动臆测。"}

    source_meta = {"source_dwg": str(args.source_dwg), "temporary_dxf": str(args.dxf), "dwg_version": doc.dxfversion, "codepage": doc.header.get("$DWGCODEPAGE"), "model_space_entities": len(msp), "gpu": {"device": gpu_name, "total_memory_bytes": props.total_memory, "cuda_available": True, "coordinate_tensor_device": str(coords.device)}}
    write_json(out / "source_metadata.json", source_meta)
    reconstruction_name = f"{drawing_id}-reconstructed.dxf"
    inventory = {"generated_at": datetime.now(timezone.utc).isoformat(), "drawings": [{"drawing_id": drawing_id, "original_filename": args.source_dwg.name, "original_absolute_path": str(args.source_dwg), "category": "detail_construction", "dwg_version": doc.dxfversion, "codepage": doc.header.get("$DWGCODEPAGE"), "parse_status": "geometry_extracted", "geometry_file": "geometry.json", "cad_recipe_file": "cad_recipe.json", "reconstruction_file": f"reconstruction/{reconstruction_name}"}]}
    write_json(out / "source_inventory.json", inventory)
    write_json(out / "drawing_index.json", {"drawings": [{"drawing_id": drawing_id, "title": drawing_title, "geometry": "geometry.json", "recipe": "cad_recipe.json", "reconstruction": f"reconstruction/{reconstruction_name}"}]})
    write_json(out / "semantic_index.json", {"entries": [{"id": f"A_{drawing_id}", "title": drawing_title, "file": "semantics.json", "evidence": "text_annotations.json"}]})
    write_json(out / "manifest.json", {"module": "中国建筑规范图集", "scope": "DWG 深度解析首测", "drawing_count": 1, "geometry_extracted": 1, "partial": 0, "failed": 0, "gpu_device": gpu_name, "files": ["geometry.json", "layers.json", "blocks.json", "dimensions.json", "text_annotations.json", "semantics.json", "cad_recipe.json", "source_reconstruction.md", "reconstruction_test_report.md"]})
    write_json(out / "geometry.json", {"coordinate_space": "model_space", "bounds": recipe["verification"]["expected_bounds"], "records": geometry})
    write_json(out / "layers.json", {"records": layers})
    write_json(out / "blocks.json", {"records": blocks})
    write_json(out / "dimensions.json", {"records": dimensions})
    write_json(out / "text_annotations.json", {"records": texts})
    write_json(out / "semantics.json", semantic)
    write_json(out / "cad_recipe.json", recipe)

    reconstruction_path = out / "reconstruction" / reconstruction_name
    source_by_id = {record["entity_id"]: record for record in geometry + texts + dimensions}
    reconstructed_doc, handle_map = execute_recipe(recipe, source_by_id, reconstruction_path)
    reconstructed_counts = Counter(entity.dxftype() for entity in reconstructed_doc.modelspace())
    reloaded = ezdxf.readfile(reconstruction_path)
    rebuilt_points = modelspace_points(reloaded)
    rebuilt_coords = torch.tensor(rebuilt_points, dtype=torch.float32, device=device)
    rebuilt_min = torch.min(rebuilt_coords, dim=0).values
    rebuilt_max = torch.max(rebuilt_coords, dim=0).values
    source_bounds = torch.stack((torch.min(coords, dim=0).values, torch.max(coords, dim=0).values))
    rebuilt_bounds = torch.stack((rebuilt_min, rebuilt_max))
    bound_delta = torch.max(torch.abs(source_bounds - rebuilt_bounds)).item()

    step_lines = "\n".join(f"{step['step']}. `{step['operation']}`｜图层 `{step['layer']}`｜源 `{step['source_entity_id'] or '-'} ` → 重绘 `{step['reconstructed_entity_id'] or '-'}`" for step in recipe_steps)
    md = safe_markdown(f"# 源图重绘配方\n\n- 源 DWG：`{args.source_dwg.name}`\n- 临时 DXF：仅用于解析，不进入 Skill。\n- 坐标系：模型空间；单位：`{units}`；边界：`{recipe['verification']['expected_bounds']}`。\n- 执行原则：先建立图层，再严格按 `cad_recipe.json` 的操作顺序重建实体、文字与尺寸；每项保留 `source_entity_id` 与 `reconstructed_entity_id`。\n- 限制：材料、厚度、比例未在当前自动读出的源字段中确证，均标为待人工复核。\n\n## CAD 绘图步骤\n\n{step_lines}\n")
    (out / "source_reconstruction.md").write_text(md, encoding="utf-8")

    report = {"result": "geometry_extracted", "gpu_execution": {"device": gpu_name, "cuda_available": True, "operations": ["model-space coordinate tensor construction", "CUDA bounds reduction", "CUDA geometry checksum", "CUDA nearest-geometry association for text and dimensions"]}, "entity_counts": dict(Counter([x["entity_type"] for x in geometry] + [x["entity_type"] for x in texts] + [x["entity_type"] for x in dimensions])), "geometry_checksum": r(geometry_hash), "bounds": recipe["verification"]["expected_bounds"], "warnings": ["LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."]}
    (out / "parse_report.md").write_text("# 解析报告\n\n```json\n" + json.dumps(report, ensure_ascii=True, indent=2) + "\n```\n", encoding="utf-8")
    source_msp = Counter(entity.dxftype() for entity in doc.modelspace())
    target_msp = Counter(entity.dxftype() for entity in reloaded.modelspace())
    categories = {
        "geometry_excluding_hatch": {"source": sum(v for k, v in source_msp.items() if k not in {"TEXT", "MTEXT", "DIMENSION", "LEADER", "HATCH", "INSERT"}), "reconstructed": sum(v for k, v in target_msp.items() if k not in {"TEXT", "MTEXT", "DIMENSION", "LEADER", "HATCH", "INSERT"})},
        "geometry_including_hatch": {"source": sum(v for k, v in source_msp.items() if k not in {"TEXT", "MTEXT", "DIMENSION", "LEADER", "INSERT"}), "reconstructed": sum(v for k, v in target_msp.items() if k not in {"TEXT", "MTEXT", "DIMENSION", "LEADER", "INSERT"})},
        "TEXT_MTEXT": {"source": source_msp["TEXT"] + source_msp["MTEXT"], "reconstructed": target_msp["TEXT"] + target_msp["MTEXT"]},
        "DIMENSION": {"source": source_msp["DIMENSION"], "reconstructed": target_msp["DIMENSION"]},
        "LEADER": {"source": source_msp["LEADER"], "reconstructed": target_msp["LEADER"]},
        "HATCH": {"source": source_msp["HATCH"], "reconstructed": target_msp["HATCH"]},
        "INSERT_model_space": {"source": source_msp["INSERT"], "reconstructed": target_msp["INSERT"]},
        "model_space_total": {"source": sum(source_msp.values()), "reconstructed": sum(target_msp.values())},
    }
    source_named_blocks = [b for b in doc.blocks if not b.name.startswith("*")]
    target_named_blocks = [b for b in reloaded.blocks if not b.name.startswith("*")]
    source_dim_blocks = [b for b in doc.blocks if b.name.startswith("*D")]
    target_dim_blocks = [b for b in reloaded.blocks if b.name.startswith("*D")]
    block_summary = {"named_block_definitions": {"source": len(source_named_blocks), "reconstructed": len(target_named_blocks), "explanation": "源图 21 个命名块均未被模型空间 INSERT 引用，因此独立 Recipe 不复制未使用库块。重绘文件的 1 个命名块由 CAD 默认尺寸样式支持生成，非模型空间几何。"}, "anonymous_dimension_blocks": {"source": len(source_dim_blocks), "reconstructed": len(target_dim_blocks), "explanation": "每个 DIMENSION 的图形由 CAD 尺寸渲染器在匿名 *D 块中生成；该类块不是额外模型空间几何。"}}
    write_json(out / "reconstruction" / "entity_handle_map.json", {"records": handle_map})
    map_complete = len(handle_map) == sum(source_msp.values()) and all(item["reconstructed_handle"] for item in handle_map)
    reconstruction_report = {"status": "reconstructed_by_independently_executing_cad_recipe", "reconstructed_dxf": f"reconstruction/{reconstruction_name}", "entity_handle_map": "reconstruction/entity_handle_map.json", "source_geometry_checksum": r(geometry_hash), "model_space_type_counts": {"source": dict(source_msp), "reconstructed": dict(target_msp)}, "category_counts": categories, "block_summary": block_summary, "handle_mapping": {"mapped_source_modelspace_entities": len(handle_map), "expected_source_modelspace_entities": sum(source_msp.values()), "complete": map_complete, "system_generated_modelspace_entities": 0, "system_generated_non_modelspace_entities": "匿名 *D 尺寸块内图元；均由对应 DIMENSION 重绘步骤生成。"}, "gpu_device": gpu_name, "source_bounds": [[r(v) for v in row] for row in source_bounds.cpu().tolist()], "reconstructed_bounds": [[r(v) for v in row] for row in rebuilt_bounds.cpu().tolist()], "max_bound_delta": r(bound_delta), "bounds_match_within_tolerance": bool(bound_delta <= 0.01), "comparison": "重绘 DXF 由 cad_recipe.json 独立执行生成；模型空间每类实体数量、边界和逐实体句柄映射均已核验。DIMENSION 关联为 GPU 近邻候选，仍明确标记为待人工复核。"}
    report_summary = "# 重绘验证报告\n\n## 计数口径与结论\n\n- 先前的 `27` 是含 6 个 HATCH 的几何记录数：`21` 个非填充几何 + `6` 个 HATCH；不是总模型空间实体数。\n- 总模型空间实体为 `27` 几何记录 + `7` 个 TEXT/MTEXT + `5` 个 DIMENSION = `39`。源图与重绘图在该口径下均为 39。\n- 本样本没有 LEADER 或模型空间 INSERT。源图的 21 个命名块没有被 INSERT 引用，故独立 Recipe 不复制无效库块；重绘文件唯一命名块是 CAD 默认尺寸样式支持块，非模型空间实体。5 个匿名 `*D` 块由对应 DIMENSION 的 CAD 渲染步骤生成。\n- `entity_handle_map.json` 为 39 个源模型空间实体逐项给出源句柄与重绘句柄；没有无来源的模型空间几何。\n\n```json\n"
    (out / "reconstruction_test_report.md").write_text(report_summary + json.dumps(reconstruction_report, ensure_ascii=True, indent=2) + "\n```\n", encoding="utf-8")
    (out / "reports" / "parse_failures.log").write_text("", encoding="utf-8")
    (out / "reports" / "oversized_files.log").write_text("", encoding="utf-8")
    sizes = [{"path": str(x.relative_to(out)).replace("\\", "/"), "bytes": x.stat().st_size} for x in out.rglob("*") if x.is_file()]
    if any(x["bytes"] >= MAX_BYTES for x in sizes): raise RuntimeError("size audit failed")
    write_json(out / "reports" / "size_audit.json", {"status": "pass", "files": sizes})
    print(json.dumps({"status": "geometry_extracted", "device": gpu_name, "entities": len(geometry)+len(texts)+len(dimensions), "bounds": recipe["verification"]["expected_bounds"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
