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
    "LINE": 2178,
    "LWPOLYLINE": 22,
    "INSERT": 41,
    "HATCH": 2,
    "ARC": 1,
    "TEXT": 51,
    "MTEXT": 1,
    "DIMENSION": 1
  },
  "geometry_checksum": 238474362880.0,
  "bounds": [
    [
      2379.84,
      721.62
    ],
    [
      11514.7,
      9531.06
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
