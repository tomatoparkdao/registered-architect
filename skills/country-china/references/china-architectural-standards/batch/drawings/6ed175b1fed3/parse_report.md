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
    "LINE": 467,
    "CIRCLE": 5,
    "ARC": 50,
    "LWPOLYLINE": 17,
    "SOLID": 18,
    "INSERT": 16,
    "TEXT": 54
  },
  "geometry_checksum": 1053293824.0,
  "bounds": [
    [
      -322.69,
      -305.78
    ],
    [
      1051.7,
      832.48
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
