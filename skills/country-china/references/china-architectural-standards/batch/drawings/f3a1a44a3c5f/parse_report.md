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
    "LINE": 2063,
    "ARC": 458,
    "CIRCLE": 43,
    "HATCH": 14,
    "INSERT": 6,
    "LWPOLYLINE": 106,
    "TEXT": 35,
    "MTEXT": 8
  },
  "geometry_checksum": 93042589696.0,
  "bounds": [
    [
      -1105.5,
      335.35
    ],
    [
      11064.87,
      7117.1
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
