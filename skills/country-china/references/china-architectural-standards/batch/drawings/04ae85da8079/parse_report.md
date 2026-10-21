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
    "LINE": 149,
    "HATCH": 22,
    "CIRCLE": 4,
    "ARC": 12,
    "TEXT": 36
  },
  "geometry_checksum": 7654078464.0,
  "bounds": [
    [
      -29.29,
      -7349.98
    ],
    [
      13595.74,
      25667.73
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
