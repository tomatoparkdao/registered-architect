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
    "LWPOLYLINE": 17,
    "INSERT": 3,
    "LINE": 224,
    "LEADER": 16,
    "CIRCLE": 7,
    "ARC": 12,
    "HATCH": 5,
    "MTEXT": 17,
    "TEXT": 164,
    "DIMENSION": 15
  },
  "geometry_checksum": 150280175616.0,
  "bounds": [
    [
      186845.86,
      -21297.17
    ],
    [
      188945.86,
      -19812.17
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
