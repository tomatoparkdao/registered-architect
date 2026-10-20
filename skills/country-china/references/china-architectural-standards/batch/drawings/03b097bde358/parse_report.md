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
    "ARC": 126,
    "LINE": 340,
    "SOLID": 79,
    "INSERT": 6,
    "CIRCLE": 2,
    "LWPOLYLINE": 5,
    "TEXT": 84
  },
  "geometry_checksum": 612415616.0,
  "bounds": [
    [
      -7.91,
      -18.66
    ],
    [
      390.98,
      289.16
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
