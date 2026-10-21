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
    "LWPOLYLINE": 29,
    "LINE": 178,
    "HATCH": 22,
    "CIRCLE": 5,
    "ARC": 4,
    "INSERT": 19,
    "TEXT": 32
  },
  "geometry_checksum": 10612559872.0,
  "bounds": [
    [
      9484.93,
      8035.25
    ],
    [
      12010.22,
      10644.57
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
