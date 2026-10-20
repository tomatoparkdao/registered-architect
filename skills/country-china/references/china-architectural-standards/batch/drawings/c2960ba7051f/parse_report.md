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
    "CIRCLE": 12,
    "LINE": 723,
    "LWPOLYLINE": 20,
    "ARC": 36,
    "INSERT": 13,
    "HATCH": 9,
    "TEXT": 128
  },
  "geometry_checksum": 35343933440.0,
  "bounds": [
    [
      -105.32,
      6186.48
    ],
    [
      7886.44,
      11412.05
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
