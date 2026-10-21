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
    "HATCH": 21,
    "ARC": 62,
    "LINE": 798,
    "CIRCLE": 30,
    "INSERT": 72,
    "TEXT": 128
  },
  "geometry_checksum": 108662628352.0,
  "bounds": [
    [
      -362.93,
      1575.26
    ],
    [
      22425.08,
      10584.62
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
