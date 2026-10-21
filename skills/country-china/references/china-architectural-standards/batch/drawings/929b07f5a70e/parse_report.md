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
    "LINE": 1895,
    "INSERT": 95,
    "ARC": 9,
    "LWPOLYLINE": 3,
    "HATCH": 1,
    "CIRCLE": 6,
    "TEXT": 109
  },
  "geometry_checksum": 5315250094080.0,
  "bounds": [
    [
      309939.66,
      -1030.49
    ],
    [
      327987.75,
      22546.16
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
