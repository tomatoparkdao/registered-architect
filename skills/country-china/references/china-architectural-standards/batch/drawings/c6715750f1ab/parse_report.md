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
    "LWPOLYLINE": 48,
    "LINE": 18,
    "HATCH": 2,
    "CIRCLE": 2,
    "ARC": 4
  },
  "geometry_checksum": 3054269440.0,
  "bounds": [
    [
      5411.06,
      3897.11
    ],
    [
      6471.06,
      6077.11
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
