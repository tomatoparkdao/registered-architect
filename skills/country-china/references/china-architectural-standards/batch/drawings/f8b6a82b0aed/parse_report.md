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
    "INSERT": 6,
    "LWPOLYLINE": 20,
    "LINE": 56,
    "SOLID": 12,
    "TEXT": 7,
    "DIMENSION": 8
  },
  "geometry_checksum": 1747183104.0,
  "bounds": [
    [
      -1155.93,
      14053.5
    ],
    [
      13054.46,
      19100.86
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
