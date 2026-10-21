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
    "LINE": 1331,
    "LWPOLYLINE": 443,
    "HATCH": 26,
    "CIRCLE": 110,
    "ARC": 26,
    "INSERT": 2,
    "MTEXT": 15,
    "DIMENSION": 52
  },
  "geometry_checksum": 11033329532928.0,
  "bounds": [
    [
      17436.26,
      112185.84
    ],
    [
      686466.0,
      155218.3
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
