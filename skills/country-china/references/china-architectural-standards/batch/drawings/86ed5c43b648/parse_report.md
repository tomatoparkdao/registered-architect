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
    "LINE": 132,
    "LWPOLYLINE": 55,
    "HATCH": 5,
    "CIRCLE": 4
  },
  "geometry_checksum": 107785632.0,
  "bounds": [
    [
      -2247.86,
      -3.14
    ],
    [
      -807.86,
      2172.86
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
