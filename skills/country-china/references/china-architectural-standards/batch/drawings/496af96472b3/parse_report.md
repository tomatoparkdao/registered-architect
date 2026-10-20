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
    "LINE": 53,
    "HATCH": 6,
    "INSERT": 5,
    "LWPOLYLINE": 2,
    "TEXT": 10
  },
  "geometry_checksum": 169331326976.0,
  "bounds": [
    [
      3378917.0,
      2252003.25
    ],
    [
      3388576.75,
      2265702.75
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
