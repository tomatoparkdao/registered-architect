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
    "HATCH": 1,
    "LINE": 575,
    "INSERT": 22,
    "LWPOLYLINE": 21,
    "ARC": 54,
    "CIRCLE": 2,
    "TEXT": 16,
    "DIMENSION": 14
  },
  "geometry_checksum": 70967672832.0,
  "bounds": [
    [
      31158.3,
      -619.7
    ],
    [
      39558.3,
      2329.58
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
