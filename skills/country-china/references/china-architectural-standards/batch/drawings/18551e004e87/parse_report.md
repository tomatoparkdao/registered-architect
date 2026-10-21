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
    "CIRCLE": 1,
    "LWPOLYLINE": 18,
    "LINE": 156,
    "ARC": 2,
    "INSERT": 4,
    "DIMENSION": 7
  },
  "geometry_checksum": 5101165568.0,
  "bounds": [
    [
      18281.81,
      9139.42
    ],
    [
      19474.49,
      10046.47
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
