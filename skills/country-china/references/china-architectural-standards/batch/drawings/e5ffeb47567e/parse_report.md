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
    "LINE": 115,
    "LWPOLYLINE": 50,
    "CIRCLE": 1,
    "HATCH": 2,
    "TEXT": 22
  },
  "geometry_checksum": 136638000.0,
  "bounds": [
    [
      63.78,
      176.01
    ],
    [
      105.37,
      210.42
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
