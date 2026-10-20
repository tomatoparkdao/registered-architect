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
    "LINE": 557,
    "ARC": 31,
    "INSERT": 22,
    "LWPOLYLINE": 22,
    "CIRCLE": 15,
    "HATCH": 7,
    "TEXT": 108,
    "MTEXT": 3
  },
  "geometry_checksum": 21410914304.0,
  "bounds": [
    [
      824.17,
      4747.34
    ],
    [
      10205.72,
      8413.26
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
