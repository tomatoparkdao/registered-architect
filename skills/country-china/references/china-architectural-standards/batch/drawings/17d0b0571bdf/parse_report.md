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
    "LINE": 3016,
    "ARC": 11,
    "CIRCLE": 8,
    "HATCH": 7,
    "SOLID": 1,
    "INSERT": 75,
    "TEXT": 165,
    "MTEXT": 4
  },
  "geometry_checksum": 4341183545344.0,
  "bounds": [
    [
      43088.94,
      39205.92
    ],
    [
      72192.08,
      80489.42
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
