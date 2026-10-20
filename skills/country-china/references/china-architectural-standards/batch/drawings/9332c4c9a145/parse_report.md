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
    "LINE": 598,
    "CIRCLE": 23,
    "LWPOLYLINE": 23,
    "ARC": 41,
    "INSERT": 50,
    "TEXT": 150,
    "MTEXT": 8
  },
  "geometry_checksum": 43683332096.0,
  "bounds": [
    [
      1606.12,
      8096.3
    ],
    [
      11894.81,
      13394.44
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
