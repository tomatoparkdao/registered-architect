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
    "LINE": 970,
    "CIRCLE": 31,
    "SOLID": 3,
    "INSERT": 70,
    "LWPOLYLINE": 4,
    "TEXT": 394,
    "MTEXT": 6
  },
  "geometry_checksum": 188412674048.0,
  "bounds": [
    [
      1.98,
      4383.9
    ],
    [
      29870.8,
      29128.11
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
