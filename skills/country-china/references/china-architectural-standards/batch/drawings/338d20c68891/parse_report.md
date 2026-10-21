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
    "LINE": 126,
    "LWPOLYLINE": 29,
    "CIRCLE": 1,
    "HATCH": 3,
    "TEXT": 25
  },
  "geometry_checksum": 111078912.0,
  "bounds": [
    [
      508.51,
      276.82
    ],
    [
      541.51,
      314.24
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
