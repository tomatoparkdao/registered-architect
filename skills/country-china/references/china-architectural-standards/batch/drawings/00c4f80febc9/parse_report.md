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
    "INSERT": 11,
    "LINE": 1062,
    "CIRCLE": 16,
    "ARC": 210,
    "LWPOLYLINE": 13,
    "TEXT": 74,
    "MTEXT": 9,
    "DIMENSION": 1
  },
  "geometry_checksum": 111273836544.0,
  "bounds": [
    [
      1809.39,
      7991.13
    ],
    [
      14071.96,
      24527.74
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
