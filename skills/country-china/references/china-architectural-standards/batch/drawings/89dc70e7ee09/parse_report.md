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
    "LWPOLYLINE": 331,
    "LINE": 2799,
    "CIRCLE": 103,
    "HATCH": 177,
    "ARC": 74,
    "TEXT": 272,
    "DIMENSION": 307
  },
  "geometry_checksum": 77206592159744.0,
  "bounds": [
    [
      702971.69,
      -131042.32
    ],
    [
      809036.06,
      -37369.97
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
