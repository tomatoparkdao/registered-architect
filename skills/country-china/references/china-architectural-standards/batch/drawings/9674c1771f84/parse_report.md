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
    "LWPOLYLINE": 1208,
    "HATCH": 229,
    "LINE": 6727,
    "INSERT": 90,
    "LEADER": 41,
    "CIRCLE": 18,
    "ARC": 21,
    "TEXT": 120
  },
  "geometry_checksum": 4784092348416.0,
  "bounds": [
    [
      -71670.52,
      271.64
    ],
    [
      77977.3,
      7552.22
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
