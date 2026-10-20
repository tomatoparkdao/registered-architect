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
    "INSERT": 7,
    "LINE": 17,
    "LWPOLYLINE": 20,
    "HATCH": 6,
    "TEXT": 5,
    "MTEXT": 6,
    "DIMENSION": 6
  },
  "geometry_checksum": -13654980608.0,
  "bounds": [
    [
      -249261.23,
      -33933.97
    ],
    [
      -182065.84,
      188072.44
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
