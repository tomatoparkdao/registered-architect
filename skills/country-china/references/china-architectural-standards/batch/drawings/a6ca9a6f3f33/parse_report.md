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
    "LWPOLYLINE": 18,
    "LINE": 2363,
    "HATCH": 96,
    "ARC": 592,
    "CIRCLE": 30,
    "MTEXT": 32,
    "TEXT": 4,
    "DIMENSION": 19
  },
  "geometry_checksum": 22573635076096.0,
  "bounds": [
    [
      379991.34,
      134594.42
    ],
    [
      382504.84,
      136591.8
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
