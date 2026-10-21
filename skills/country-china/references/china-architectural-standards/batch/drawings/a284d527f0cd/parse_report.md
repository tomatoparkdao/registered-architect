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
    "LWPOLYLINE": 653,
    "LINE": 7045,
    "HATCH": 607,
    "ARC": 149,
    "POLYLINE": 26,
    "CIRCLE": 106,
    "INSERT": 18,
    "TEXT": 272,
    "MTEXT": 261,
    "DIMENSION": 141
  },
  "geometry_checksum": 51366173081600.0,
  "bounds": [
    [
      -156263.52,
      117060.36
    ],
    [
      -8544.22,
      261912.84
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
