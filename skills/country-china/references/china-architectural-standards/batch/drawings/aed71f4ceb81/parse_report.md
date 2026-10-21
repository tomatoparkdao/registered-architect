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
    "LWPOLYLINE": 19,
    "HATCH": 20,
    "LINE": 562,
    "ARC": 103,
    "CIRCLE": 10,
    "INSERT": 29,
    "TEXT": 2,
    "MTEXT": 22
  },
  "geometry_checksum": 18757922816.0,
  "bounds": [
    [
      4225.04,
      2743.2
    ],
    [
      4367.91,
      2917.39
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
