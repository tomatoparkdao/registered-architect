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
    "LINE": 541,
    "CIRCLE": 7,
    "LWPOLYLINE": 18,
    "HATCH": 37,
    "INSERT": 119,
    "TEXT": 109
  },
  "geometry_checksum": 50180743168.0,
  "bounds": [
    [
      1982.39,
      8821.47
    ],
    [
      20338.46,
      20206.0
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
