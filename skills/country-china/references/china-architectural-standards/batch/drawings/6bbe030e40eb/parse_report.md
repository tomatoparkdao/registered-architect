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
    "LINE": 418,
    "HATCH": 27,
    "LWPOLYLINE": 51,
    "ARC": 78,
    "SPLINE": 8,
    "INSERT": 1,
    "TEXT": 34,
    "DIMENSION": 7
  },
  "geometry_checksum": -4306705055744.0,
  "bounds": [
    [
      -1400522.5,
      -495050.44
    ],
    [
      -1348838.62,
      -466227.69
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
