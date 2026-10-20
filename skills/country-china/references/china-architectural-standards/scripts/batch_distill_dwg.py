"""Resumable DWG-only batch driver. Temporary DXF files never enter the Skill."""
import argparse, hashlib, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONVERTER = Path(os.environ.get("DWG2DXF", r"C:\Users\Administrator\AppData\Local\libredwg\dwg2dxf.exe"))
ODA = Path(r"C:\Program Files\ODA\ODAFileConverter 27.9.0\ODAFileConverter.exe")
DEEP = Path(__file__).with_name("deep_distill_dwg.py")
MAX = 1024 * 1024
RECORDS_PER_SHARD = 500

def put(path, data):
    text=json.dumps(data,ensure_ascii=False,separators=(",",":"));
    if len(text.encode())>=MAX: raise RuntimeError(f"oversize: {path}")
    path.write_text(text,encoding="utf8")

def valid_dwg(path):
    try: return path.read_bytes()[:2] == b"AC"
    except OSError: return False

def load_state(manifest):
    state=json.loads(manifest.read_text(encoding="utf8")) if manifest.exists() else {}
    records=list(state.get("records", []))
    for relative in state.get("record_shards", []):
        shard=manifest.parent/relative
        records.extend(json.loads(shard.read_text(encoding="utf8"))["records"])
    return state, records

def save_state(manifest, records, total, processed):
    """Keep each generated audit artifact under the one-megabyte ceiling."""
    records_dir=manifest.parent/"record_shards"; records_dir.mkdir(exist_ok=True)
    names=[]
    for index in range(0, len(records), RECORDS_PER_SHARD):
        name=f"record_shards/records-{index // RECORDS_PER_SHARD + 1:04d}.json"
        put(manifest.parent/name, {"records": records[index:index + RECORDS_PER_SHARD]})
        names.append(name)
    put(manifest, {"record_shards": names, "total_dwg_discovered": total, "processed_this_run": processed})

def main():
    p=argparse.ArgumentParser(); p.add_argument("--source",action="append",required=True,type=Path); p.add_argument("--limit",type=int,default=25); a=p.parse_args()
    out=ROOT/"batch"; drawings=out/"drawings"; drawings.mkdir(parents=True,exist_ok=True)
    files=[]
    for source in a.source:
        files.extend(sorted(x for x in source.rglob("*") if x.is_file() and x.suffix.lower()==".dwg"))
    manifest=out/"batch_manifest.json"; prior, records=load_state(manifest)
    # Each non-terminal drawing gets two full converter/parse attempts.  This
    # preserves a retry after parser fixes without letting persistent failures
    # starve the still-unseen DWG inventory forever.
    attempts={}
    for item in records:
        if item["status"] not in {"geometry_extracted", "invalid_dwg"}:
            attempts[item["source_path"]] = attempts.get(item["source_path"], 0) + 1
    done={x["source_path"] for x in records if x["status"] in {"geometry_extracted","invalid_dwg"}}
    done.update(path for path, count in attempts.items() if count >= 2)
    selected=[x for x in files if str(x) not in done][:a.limit]
    for source in selected:
        digest=hashlib.sha1(str(source).encode("utf8")).hexdigest()[:12]; drawing_id=f"CN-DWG-{digest.upper()}"; target=drawings/digest
        if not valid_dwg(source): records.append({"source_path":str(source),"drawing_id":drawing_id,"status":"invalid_dwg"}); continue
        with tempfile.TemporaryDirectory(prefix="dwg-batch-") as temp:
            dxf=Path(temp)/"input.dxf"
            convert=subprocess.run([str(CONVERTER),"-y","-o",str(dxf),str(source)],capture_output=True,text=True,encoding="utf8",errors="replace")
            converter="libredwg"
            if convert.returncode or not dxf.exists():
                # ODA is a separate, installed converter; source is staged only in
                # the OS temp directory and is never copied into the Skill.
                stage=Path(temp)/"oda-in"; oda_out=Path(temp)/"oda-out"; stage.mkdir(); oda_out.mkdir()
                shutil.copy2(source, stage/"input.dwg")
                oda=subprocess.run([str(ODA),str(stage),str(oda_out),"ACAD2018","DXF","0","0","*.dwg"],capture_output=True,text=True,encoding="utf8",errors="replace")
                oda_dxf=oda_out/"input.dxf"
                if oda.returncode or not oda_dxf.exists():
                    records.append({"source_path":str(source),"drawing_id":drawing_id,"status":"conversion_failed","detail":(convert.stderr+" | ODA: "+oda.stderr)[-500:]}); continue
                shutil.copy2(oda_dxf,dxf); converter="oda"
            deep=subprocess.run([sys.executable,str(DEEP),"--dxf",str(dxf),"--source-dwg",str(source),"--output",str(target),"--drawing-id",drawing_id],capture_output=True,text=True,encoding="utf8",errors="replace")
            records.append({"source_path":str(source),"drawing_id":drawing_id,"status":"geometry_extracted" if deep.returncode==0 else "parse_failed","converter":converter,"output":str(target.relative_to(ROOT)).replace("\\","/"),"detail":deep.stderr[-500:]})
        save_state(manifest,records,len(files),len(selected))
    save_state(manifest,records,len(files),len(selected))
    print(json.dumps({"selected":len(selected),"total":len(files),"success":sum(x["status"]=="geometry_extracted" for x in records),"failures":sum(x["status"] not in {"geometry_extracted","invalid_dwg"} for x in records)},ensure_ascii=False))
if __name__=="__main__": main()
