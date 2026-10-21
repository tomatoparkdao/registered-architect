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
    "LINE": 1512,
    "LWPOLYLINE": 10,
    "CIRCLE": 45,
    "HATCH": 46,
    "INSERT": 107,
    "SOLID": 14,
    "ARC": 22,
    "TEXT": 114
  },
  "geometry_checksum": 128978337792.0,
  "bounds": [
    [
      -11394.92,
      603.34
    ],
    [
      6047.65,
      9349.54
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
