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
    "INSERT": 248,
    "LINE": 1591,
    "LWPOLYLINE": 710,
    "ARC": 16,
    "CIRCLE": 42,
    "POLYLINE": 10,
    "HATCH": 4,
    "TEXT": 2522
  },
  "geometry_checksum": -10561794342912.0,
  "bounds": [
    [
      -358145.34,
      -348100.34
    ],
    [
      133602.5,
      111822.5
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
