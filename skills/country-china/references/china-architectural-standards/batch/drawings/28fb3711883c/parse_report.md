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
    "LINE": 500,
    "HATCH": 4,
    "ARC": 216,
    "CIRCLE": 3,
    "INSERT": 111,
    "TEXT": 110,
    "MTEXT": 1
  },
  "geometry_checksum": 118309560320.0,
  "bounds": [
    [
      4039.75,
      32518.76
    ],
    [
      17972.19,
      55604.18
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
