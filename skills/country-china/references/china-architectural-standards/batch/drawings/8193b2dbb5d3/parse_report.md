# 解析报告

```json
{
  "result": "geometry_extracted",
  "gpu_execution": {
    "device": "NVIDIA GeForce RTX 4070",
    "cuda_available": true,
    "operations": [
      "model-space coordinate tensor construction",
      "CUDA bounds reduction",
      "CUDA geometry checksum",
      "CUDA nearest-geometry association for text and dimensions"
    ]
  },
  "entity_counts": {
    "CIRCLE": 2,
    "ARC": 14,
    "LWPOLYLINE": 54,
    "POLYLINE": 6,
    "LINE": 7
  },
  "geometry_checksum": 676726592.0,
  "bounds": [
    [
      145.25,
      380.3
    ],
    [
      221.15,
      449.89
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
