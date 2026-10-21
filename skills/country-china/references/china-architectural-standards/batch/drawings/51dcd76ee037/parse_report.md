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
    "LINE": 87,
    "LEADER": 11,
    "HATCH": 3,
    "INSERT": 33,
    "LWPOLYLINE": 10,
    "CIRCLE": 8,
    "ARC": 6,
    "MTEXT": 10,
    "TEXT": 3,
    "DIMENSION": 9
  },
  "geometry_checksum": 10760992768.0,
  "bounds": [
    [
      -994602.75,
      -1105949.0
    ],
    [
      1199564.25,
      189399.98
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
