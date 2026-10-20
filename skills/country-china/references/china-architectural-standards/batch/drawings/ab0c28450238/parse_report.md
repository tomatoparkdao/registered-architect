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
    "LINE": 51,
    "HATCH": 2,
    "LWPOLYLINE": 39,
    "ARC": 15,
    "CIRCLE": 2
  },
  "geometry_checksum": 883903232.0,
  "bounds": [
    [
      1.1,
      3047.91
    ],
    [
      2065.53,
      5789.91
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
