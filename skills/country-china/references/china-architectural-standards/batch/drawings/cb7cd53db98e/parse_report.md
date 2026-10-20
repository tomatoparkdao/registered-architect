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
    "LWPOLYLINE": 234,
    "CIRCLE": 45,
    "POLYLINE": 78,
    "ARC": 459,
    "LINE": 302,
    "HATCH": 3,
    "MTEXT": 2
  },
  "geometry_checksum": 4296729690112.0,
  "bounds": [
    [
      9270.86,
      7857.57
    ],
    [
      18140.01,
      23584.45
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
