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
    "LINE": 109,
    "HATCH": 5,
    "ARC": 11,
    "CIRCLE": 2,
    "LWPOLYLINE": 1,
    "TEXT": 12,
    "DIMENSION": 11
  },
  "geometry_checksum": 2806113280.0,
  "bounds": [
    [
      166764.56,
      -145106.62
    ],
    [
      168027.7,
      -144236.95
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
