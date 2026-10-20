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
    "LWPOLYLINE": 142,
    "LINE": 84,
    "HATCH": 29,
    "ARC": 155,
    "CIRCLE": 33,
    "ELLIPSE": 6
  },
  "geometry_checksum": 121583763456.0,
  "bounds": [
    [
      45423.58,
      14578.66
    ],
    [
      48075.37,
      17363.97
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
