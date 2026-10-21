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
    "LINE": 525,
    "ARC": 26,
    "LWPOLYLINE": 21,
    "CIRCLE": 10,
    "INSERT": 61,
    "SPLINE": 1,
    "HATCH": 7,
    "TEXT": 114,
    "MTEXT": 15
  },
  "geometry_checksum": 33063208960.0,
  "bounds": [
    [
      3493.73,
      9542.9
    ],
    [
      9436.16,
      13773.63
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
