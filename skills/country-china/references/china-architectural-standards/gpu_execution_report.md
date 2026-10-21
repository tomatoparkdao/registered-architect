# GPU 执行报告

- GPU：NVIDIA GeForce RTX 4070, 12282 MiB, 617.42
- PyTorch：2.11.0+cu128
- CUDA 可用：True
- 实际设备：NVIDIA GeForce RTX 4070
- 已完成深度处理的 DWG：4335

## GPU 阶段

1. CUDA 坐标张量构建与边界归约。
2. CUDA 几何校验和计算。
3. CUDA 文字/尺寸至最近几何实体的空间关联。
4. CUDA 重绘前后模型空间边界对比。

DWG→DXF 为外部格式转换预处理；后续几何处理、关联和验证在 CUDA 设备上执行。任何 `torch.cuda.is_available()` 为假时，深度解析脚本会拒绝运行。
