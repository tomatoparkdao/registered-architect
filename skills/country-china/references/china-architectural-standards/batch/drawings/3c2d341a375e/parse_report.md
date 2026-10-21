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
    "LWPOLYLINE": 4,
    "INSERT": 96,
    "LINE": 1050,
    "HATCH": 21,
    "ARC": 37,
    "CIRCLE": 17,
    "TEXT": 127
  },
  "geometry_checksum": 973600784384.0,
  "bounds": [
    [
      21271.71,
      17412.82
    ],
    [
      79728.36,
      92748.7
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
