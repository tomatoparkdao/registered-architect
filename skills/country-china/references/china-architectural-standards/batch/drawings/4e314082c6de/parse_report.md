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
    "LINE": 391,
    "LWPOLYLINE": 70,
    "CIRCLE": 36,
    "ARC": 12,
    "TEXT": 7058
  },
  "geometry_checksum": 229195333632.0,
  "bounds": [
    [
      -117.58,
      -374.11
    ],
    [
      3955.46,
      2991.69
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
