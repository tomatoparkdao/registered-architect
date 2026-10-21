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
    "INSERT": 54,
    "LINE": 1859,
    "CIRCLE": 6,
    "ARC": 48,
    "LWPOLYLINE": 74,
    "POLYLINE": 1,
    "TEXT": 71
  },
  "geometry_checksum": 1136078880768.0,
  "bounds": [
    [
      -51759.64,
      -62494.35
    ],
    [
      123438.53,
      57998.96
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
