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
    "ARC": 23,
    "CIRCLE": 20,
    "LINE": 1100,
    "LWPOLYLINE": 28,
    "SPLINE": 2,
    "INSERT": 21,
    "TEXT": 108,
    "MTEXT": 7
  },
  "geometry_checksum": 120164335616.0,
  "bounds": [
    [
      3117.18,
      9711.33
    ],
    [
      11207.69,
      13900.07
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
