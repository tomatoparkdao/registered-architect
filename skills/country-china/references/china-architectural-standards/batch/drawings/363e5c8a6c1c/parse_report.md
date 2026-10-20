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
    "INSERT": 1,
    "CIRCLE": 7,
    "LINE": 206,
    "ARC": 18,
    "SOLID": 41,
    "TEXT": 51
  },
  "geometry_checksum": 158912864.0,
  "bounds": [
    [
      0.0,
      0.0
    ],
    [
      395.82,
      247.97
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
