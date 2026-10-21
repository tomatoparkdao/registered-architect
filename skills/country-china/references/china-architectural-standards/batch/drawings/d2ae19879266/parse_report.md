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
    "LWPOLYLINE": 24,
    "INSERT": 99,
    "LINE": 960,
    "ARC": 26,
    "CIRCLE": 17,
    "SOLID": 5,
    "HATCH": 11,
    "TEXT": 132,
    "MTEXT": 1
  },
  "geometry_checksum": 847378120704.0,
  "bounds": [
    [
      2849.52,
      -10932.16
    ],
    [
      127669.12,
      43275.33
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
