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
    "LINE": 590,
    "CIRCLE": 31,
    "INSERT": 129,
    "ARC": 8,
    "TEXT": 86,
    "MTEXT": 24
  },
  "geometry_checksum": 14732611584.0,
  "bounds": [
    [
      1037.07,
      416.37
    ],
    [
      6011.09,
      6579.53
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
