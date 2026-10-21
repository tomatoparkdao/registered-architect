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
    "INSERT": 5,
    "LINE": 93,
    "LWPOLYLINE": 31,
    "HATCH": 17,
    "ARC": 83,
    "MTEXT": 3,
    "TEXT": 9
  },
  "geometry_checksum": 715697152.0,
  "bounds": [
    [
      2108.98,
      364.4
    ],
    [
      2656.09,
      1082.56
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
