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
    "LINE": 315,
    "LWPOLYLINE": 12,
    "ARC": 34,
    "INSERT": 51,
    "CIRCLE": 21,
    "TEXT": 83
  },
  "geometry_checksum": 43439861760.0,
  "bounds": [
    [
      22553.06,
      1171.6
    ],
    [
      41289.72,
      49277.4
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
