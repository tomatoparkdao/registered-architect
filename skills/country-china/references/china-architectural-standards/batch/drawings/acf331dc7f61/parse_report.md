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
    "LINE": 221,
    "LWPOLYLINE": 59,
    "INSERT": 16,
    "HATCH": 36,
    "ARC": 2,
    "TEXT": 36
  },
  "geometry_checksum": 19433455616.0,
  "bounds": [
    [
      1344.09,
      2052.0
    ],
    [
      13282.29,
      23271.27
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
