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
    "LINE": 93,
    "HATCH": 3,
    "LWPOLYLINE": 13,
    "INSERT": 3,
    "TEXT": 39,
    "DIMENSION": 19
  },
  "geometry_checksum": -584330182656.0,
  "bounds": [
    [
      -1760159.12,
      -1843686.12
    ],
    [
      860494.81,
      917268.5
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
