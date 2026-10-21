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
    "LINE": 10874,
    "LWPOLYLINE": 138,
    "INSERT": 9,
    "HATCH": 12,
    "ARC": 448,
    "CIRCLE": 13,
    "TEXT": 38,
    "DIMENSION": 54
  },
  "geometry_checksum": -144022700032.0,
  "bounds": [
    [
      -253.1,
      -33.72
    ],
    [
      -243.03,
      -25.37
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
