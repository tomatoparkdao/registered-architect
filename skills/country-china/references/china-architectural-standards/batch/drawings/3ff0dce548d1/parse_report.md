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
    "LWPOLYLINE": 4,
    "INSERT": 9,
    "TEXT": 11,
    "DIMENSION": 4
  },
  "geometry_checksum": 491486656.0,
  "bounds": [
    [
      6487.24,
      19296.92
    ],
    [
      8072.1,
      21537.63
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
