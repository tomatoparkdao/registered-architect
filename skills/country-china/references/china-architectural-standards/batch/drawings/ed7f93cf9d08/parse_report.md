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
    "HATCH": 3,
    "LWPOLYLINE": 101,
    "LINE": 433,
    "CIRCLE": 1,
    "POLYLINE": 83,
    "ARC": 20
  },
  "geometry_checksum": 1618582700032.0,
  "bounds": [
    [
      -747.49,
      3278.44
    ],
    [
      1682.51,
      5498.44
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
