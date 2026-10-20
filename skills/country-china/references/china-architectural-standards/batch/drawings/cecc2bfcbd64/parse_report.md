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
    "LINE": 501,
    "CIRCLE": 13,
    "INSERT": 22,
    "LWPOLYLINE": 49,
    "ARC": 30,
    "HATCH": 6,
    "TEXT": 86,
    "MTEXT": 9
  },
  "geometry_checksum": 23084959744.0,
  "bounds": [
    [
      -576.67,
      5379.37
    ],
    [
      11702.98,
      7439.05
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
