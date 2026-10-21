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
    "LWPOLYLINE": 65,
    "LINE": 511,
    "ARC": 2,
    "CIRCLE": 5,
    "TEXT": 10,
    "DIMENSION": 4
  },
  "geometry_checksum": 29051125760.0,
  "bounds": [
    [
      -2624.64,
      19872.16
    ],
    [
      -530.04,
      22374.21
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
