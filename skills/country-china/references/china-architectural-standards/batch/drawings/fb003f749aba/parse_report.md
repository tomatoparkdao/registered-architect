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
    "LINE": 253,
    "LWPOLYLINE": 34,
    "CIRCLE": 2,
    "HATCH": 5,
    "TEXT": 10,
    "DIMENSION": 42
  },
  "geometry_checksum": 804167424.0,
  "bounds": [
    [
      -3162.36,
      -3305.95
    ],
    [
      6620.47,
      1624.65
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
