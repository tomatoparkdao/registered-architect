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
    "LINE": 2066,
    "CIRCLE": 10,
    "ARC": 12,
    "INSERT": 74,
    "TEXT": 97
  },
  "geometry_checksum": 2601326215168.0,
  "bounds": [
    [
      -3982.2,
      2504.41
    ],
    [
      122908.47,
      182624.17
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
