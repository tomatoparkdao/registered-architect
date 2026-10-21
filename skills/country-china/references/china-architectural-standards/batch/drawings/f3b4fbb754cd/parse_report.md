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
    "LINE": 181,
    "LWPOLYLINE": 26,
    "HATCH": 20,
    "INSERT": 20,
    "ARC": 4,
    "MTEXT": 12,
    "TEXT": 12
  },
  "geometry_checksum": 2624762880.0,
  "bounds": [
    [
      -2813.42,
      645.82
    ],
    [
      2825.48,
      1164.29
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
