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
    "CIRCLE": 17,
    "LINE": 1018,
    "ARC": 32,
    "SPLINE": 2,
    "LWPOLYLINE": 18,
    "INSERT": 17,
    "TEXT": 87,
    "MTEXT": 5
  },
  "geometry_checksum": 93531160576.0,
  "bounds": [
    [
      1418.96,
      6851.6
    ],
    [
      10216.03,
      13395.66
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
