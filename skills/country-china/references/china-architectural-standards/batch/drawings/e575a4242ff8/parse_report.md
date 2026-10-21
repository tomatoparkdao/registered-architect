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
    "LINE": 29,
    "LWPOLYLINE": 3,
    "INSERT": 1,
    "HATCH": 1,
    "TEXT": 4,
    "DIMENSION": 7
  },
  "geometry_checksum": 3168124.5,
  "bounds": [
    [
      -2531.18,
      1394.11
    ],
    [
      -966.37,
      2622.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
