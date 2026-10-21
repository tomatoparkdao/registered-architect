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
    "LINE": 58,
    "INSERT": 12,
    "LWPOLYLINE": 23,
    "HATCH": 7,
    "TEXT": 7,
    "MTEXT": 6,
    "DIMENSION": 15
  },
  "geometry_checksum": -62399062016.0,
  "bounds": [
    [
      -442679.78,
      -33848.24
    ],
    [
      893.58,
      187654.91
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
