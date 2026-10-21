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
    "LINE": 130,
    "LWPOLYLINE": 5,
    "HATCH": 12,
    "CIRCLE": 2,
    "INSERT": 2,
    "TEXT": 22
  },
  "geometry_checksum": 2189634048.0,
  "bounds": [
    [
      319.16,
      3463.92
    ],
    [
      1455.73,
      8232.62
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
