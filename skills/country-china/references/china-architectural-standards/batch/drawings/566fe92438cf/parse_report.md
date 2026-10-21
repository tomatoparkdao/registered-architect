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
    "LINE": 1526,
    "LWPOLYLINE": 5,
    "ARC": 4,
    "CIRCLE": 8,
    "HATCH": 1,
    "INSERT": 54,
    "TEXT": 68
  },
  "geometry_checksum": 2326710976512.0,
  "bounds": [
    [
      -54692.84,
      -34676.72
    ],
    [
      188801.59,
      263857.69
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
