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
    "LINE": 330,
    "LWPOLYLINE": 40,
    "CIRCLE": 3,
    "TEXT": 4,
    "DIMENSION": 4
  },
  "geometry_checksum": 31587155968.0,
  "bounds": [
    [
      21231.44,
      25988.6
    ],
    [
      24828.14,
      27662.96
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
