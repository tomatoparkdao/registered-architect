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
    "LINE": 233,
    "ARC": 18,
    "INSERT": 18,
    "CIRCLE": 1,
    "LWPOLYLINE": 1,
    "TEXT": 11,
    "MTEXT": 6
  },
  "geometry_checksum": 2102268928.0,
  "bounds": [
    [
      3856.14,
      2158.97
    ],
    [
      4802.83,
      4017.67
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
