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
    "LINE": 40,
    "LWPOLYLINE": 12,
    "HATCH": 16,
    "ARC": 391,
    "CIRCLE": 100
  },
  "geometry_checksum": 1723735296.0,
  "bounds": [
    [
      -1282.16,
      2.18
    ],
    [
      1392.06,
      2162.49
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
