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
    "LINE": 20,
    "INSERT": 3,
    "ARC": 1,
    "LWPOLYLINE": 2,
    "HATCH": 2,
    "TEXT": 7,
    "DIMENSION": 2
  },
  "geometry_checksum": -1657714816.0,
  "bounds": [
    [
      -94751.41,
      -64366.59
    ],
    [
      -94299.18,
      -63980.44
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
