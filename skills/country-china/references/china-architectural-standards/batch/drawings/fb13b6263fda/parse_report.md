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
    "LINE": 412,
    "HATCH": 10,
    "LWPOLYLINE": 50,
    "ARC": 4,
    "INSERT": 106,
    "TEXT": 93
  },
  "geometry_checksum": 13788367872.0,
  "bounds": [
    [
      1189.98,
      261.56
    ],
    [
      7935.27,
      6726.64
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
