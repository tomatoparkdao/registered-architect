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
    "LINE": 560,
    "CIRCLE": 12,
    "INSERT": 126,
    "TEXT": 101,
    "MTEXT": 3
  },
  "geometry_checksum": 94820032512.0,
  "bounds": [
    [
      3034.61,
      42664.32
    ],
    [
      6062.32,
      49976.36
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
