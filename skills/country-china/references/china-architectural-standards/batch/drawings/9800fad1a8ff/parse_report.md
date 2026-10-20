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
    "LINE": 633,
    "INSERT": 3,
    "LWPOLYLINE": 9,
    "HATCH": 1,
    "TEXT": 3,
    "MTEXT": 3,
    "DIMENSION": 2
  },
  "geometry_checksum": -410129989632.0,
  "bounds": [
    [
      -424001.75,
      -235581.16
    ],
    [
      -201764.64,
      -33691.4
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
