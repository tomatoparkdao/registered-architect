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
    "LINE": 225,
    "INSERT": 58,
    "HATCH": 11,
    "ARC": 13,
    "CIRCLE": 3,
    "LWPOLYLINE": 9,
    "MTEXT": 42
  },
  "geometry_checksum": 6674770944.0,
  "bounds": [
    [
      8495.45,
      3496.27
    ],
    [
      8822.99,
      3916.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
