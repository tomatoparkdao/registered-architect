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
    "LINE": 1408,
    "CIRCLE": 26,
    "HATCH": 1,
    "INSERT": 165,
    "TEXT": 84,
    "MTEXT": 55
  },
  "geometry_checksum": 11911083065344.0,
  "bounds": [
    [
      1299989.38,
      -130601.59
    ],
    [
      1317976.75,
      -106634.63
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
