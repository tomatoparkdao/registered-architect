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
    "LINE": 8,
    "LWPOLYLINE": 30,
    "HATCH": 1,
    "CIRCLE": 2
  },
  "geometry_checksum": -235532704.0,
  "bounds": [
    [
      -4533.39,
      0.01
    ],
    [
      -3573.39,
      2180.01
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
