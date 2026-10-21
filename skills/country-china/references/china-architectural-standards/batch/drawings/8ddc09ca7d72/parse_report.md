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
    "LWPOLYLINE": 3,
    "LINE": 63,
    "CIRCLE": 2,
    "HATCH": 2,
    "ARC": 2,
    "INSERT": 10,
    "MTEXT": 13,
    "DIMENSION": 7
  },
  "geometry_checksum": 4300611584.0,
  "bounds": [
    [
      138647.7,
      -37027.97
    ],
    [
      139191.7,
      -35940.84
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
