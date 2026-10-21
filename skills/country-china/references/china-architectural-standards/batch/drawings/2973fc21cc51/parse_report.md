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
    "LINE": 303,
    "INSERT": 36,
    "HATCH": 20,
    "LWPOLYLINE": 24,
    "ARC": 12,
    "CIRCLE": 10,
    "TEXT": 52
  },
  "geometry_checksum": 156638150656.0,
  "bounds": [
    [
      5005.11,
      2376.8
    ],
    [
      79939.03,
      108372.54
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
