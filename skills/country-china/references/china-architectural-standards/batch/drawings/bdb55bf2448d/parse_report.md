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
    "ARC": 33,
    "LINE": 244,
    "CIRCLE": 8,
    "HATCH": 4,
    "MTEXT": 92
  },
  "geometry_checksum": Infinity,
  "bounds": [
    [
      3249.08,
      0.0
    ],
    [
      Infinity,
      2784.08
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
