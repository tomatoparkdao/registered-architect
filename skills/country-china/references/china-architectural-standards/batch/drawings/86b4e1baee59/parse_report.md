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
    "LWPOLYLINE": 13,
    "LINE": 64,
    "ARC": 13,
    "ELLIPSE": 1,
    "HATCH": 3
  },
  "geometry_checksum": 403277216.0,
  "bounds": [
    [
      2017.74,
      327.92
    ],
    [
      3437.74,
      1527.92
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
