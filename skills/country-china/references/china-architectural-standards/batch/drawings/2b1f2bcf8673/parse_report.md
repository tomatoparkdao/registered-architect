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
    "LINE": 202,
    "LEADER": 5,
    "INSERT": 4,
    "HATCH": 5,
    "LWPOLYLINE": 2,
    "TEXT": 5,
    "MTEXT": 5,
    "DIMENSION": 4
  },
  "geometry_checksum": 16618946560.0,
  "bounds": [
    [
      54417.12,
      11207.99
    ],
    [
      56870.78,
      12375.8
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
