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
    "LINE": 4181,
    "ARC": 49,
    "CIRCLE": 7,
    "INSERT": 5,
    "HATCH": 8,
    "TEXT": 66
  },
  "geometry_checksum": 1978095239168.0,
  "bounds": [
    [
      -10675.33,
      4539.27
    ],
    [
      26042.44,
      30955.6
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
