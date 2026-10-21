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
    "LINE": 196,
    "ARC": 4,
    "SPLINE": 11,
    "CIRCLE": 1,
    "INSERT": 6,
    "TEXT": 67
  },
  "geometry_checksum": 5730707456.0,
  "bounds": [
    [
      5860.02,
      -1365.27
    ],
    [
      24155.28,
      18901.25
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
