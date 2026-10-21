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
    "LINE": 1130,
    "ARC": 183,
    "CIRCLE": 3,
    "INSERT": 48,
    "LWPOLYLINE": 22,
    "TEXT": 108
  },
  "geometry_checksum": 103682875392.0,
  "bounds": [
    [
      327.54,
      -26432.56
    ],
    [
      17581.89,
      21596.37
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
