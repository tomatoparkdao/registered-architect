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
    "INSERT": 3,
    "LINE": 201,
    "LWPOLYLINE": 11,
    "HATCH": 4,
    "ELLIPSE": 39,
    "CIRCLE": 1,
    "TEXT": 55,
    "DIMENSION": 4
  },
  "geometry_checksum": 14777519104.0,
  "bounds": [
    [
      5491.02,
      17078.38
    ],
    [
      19514.79,
      35166.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
