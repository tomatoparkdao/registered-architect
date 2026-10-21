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
    "LINE": 631,
    "INSERT": 72,
    "ARC": 22,
    "LWPOLYLINE": 15,
    "CIRCLE": 11,
    "HATCH": 28,
    "TEXT": 77
  },
  "geometry_checksum": 86806159360.0,
  "bounds": [
    [
      3069.91,
      -2939.4
    ],
    [
      24687.89,
      20633.27
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
