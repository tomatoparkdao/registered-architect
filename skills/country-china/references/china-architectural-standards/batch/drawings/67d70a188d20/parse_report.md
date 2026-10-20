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
    "LINE": 63,
    "LWPOLYLINE": 65,
    "HATCH": 6,
    "CIRCLE": 14,
    "ARC": 4
  },
  "geometry_checksum": 1370481536.0,
  "bounds": [
    [
      194.86,
      942.87
    ],
    [
      3795.14,
      3542.87
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
