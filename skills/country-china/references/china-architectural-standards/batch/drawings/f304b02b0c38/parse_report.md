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
    "LINE": 982,
    "SPLINE": 17,
    "CIRCLE": 6,
    "INSERT": 56,
    "ARC": 5,
    "TEXT": 69,
    "MTEXT": 1
  },
  "geometry_checksum": 227785211904.0,
  "bounds": [
    [
      -9188.74,
      45877.91
    ],
    [
      6000.59,
      62969.25
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
