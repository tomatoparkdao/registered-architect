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
    "LINE": 507,
    "INSERT": 59,
    "LWPOLYLINE": 30,
    "ARC": 8,
    "HATCH": 8,
    "CIRCLE": 4,
    "SOLID": 3,
    "TEXT": 87
  },
  "geometry_checksum": 19720626176.0,
  "bounds": [
    [
      1322.13,
      888.95
    ],
    [
      5754.78,
      8318.79
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
