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
    "INSERT": 2,
    "LWPOLYLINE": 5,
    "LINE": 315,
    "TEXT": 13,
    "DIMENSION": 9
  },
  "geometry_checksum": 11392233472.0,
  "bounds": [
    [
      31986.5,
      -17704.01
    ],
    [
      44607.96,
      -9023.16
    ]
  ],
  "warnings": [
    "LibreDWG reported six HATCH handle warnings during temporary conversion; generated HATCH boundaries are retained only when present in DXF."
  ]
}
```
