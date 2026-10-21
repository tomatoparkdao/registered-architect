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
    "LINE": 60,
    "INSERT": 6,
    "LWPOLYLINE": 8,
    "TEXT": 12,
    "DIMENSION": 9
  },
  "geometry_checksum": 552248832.0,
  "bounds": [
    [
      -10.0,
      -2504.39
    ],
    [
      14403.59,
      2449.98
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
