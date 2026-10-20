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
    "LINE": 705,
    "CIRCLE": 96,
    "ARC": 84,
    "LWPOLYLINE": 168,
    "INSERT": 18,
    "TEXT": 316,
    "MTEXT": 12,
    "DIMENSION": 66
  },
  "geometry_checksum": 2886842974208.0,
  "bounds": [
    [
      286950.62,
      63783.01
    ],
    [
      370692.28,
      91916.04
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
