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
    "LINE": 101,
    "LWPOLYLINE": 27,
    "HATCH": 12,
    "CIRCLE": 1,
    "TEXT": 12,
    "DIMENSION": 29
  },
  "geometry_checksum": 3958459392.0,
  "bounds": [
    [
      -2298.53,
      -6652.85
    ],
    [
      13684.71,
      22050.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
