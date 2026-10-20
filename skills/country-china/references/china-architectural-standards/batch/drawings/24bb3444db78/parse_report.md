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
    "LINE": 118,
    "LWPOLYLINE": 85,
    "HATCH": 1,
    "POLYLINE": 75,
    "ARC": 28,
    "CIRCLE": 4
  },
  "geometry_checksum": 276939309056.0,
  "bounds": [
    [
      346.91,
      1381.1
    ],
    [
      6747.61,
      7650.61
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
