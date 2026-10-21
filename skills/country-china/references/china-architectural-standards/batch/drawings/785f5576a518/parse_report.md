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
    "LINE": 91,
    "LWPOLYLINE": 29,
    "CIRCLE": 1,
    "HATCH": 3,
    "TEXT": 9,
    "DIMENSION": 22
  },
  "geometry_checksum": 2478240256.0,
  "bounds": [
    [
      3371.92,
      -549.71
    ],
    [
      8317.51,
      14998.5
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
