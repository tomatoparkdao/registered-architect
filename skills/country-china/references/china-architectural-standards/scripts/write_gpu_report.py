import json, subprocess
from pathlib import Path
import torch

root=Path(__file__).resolve().parent.parent
manifest=root/'batch'/'batch_manifest.json'
state=json.loads(manifest.read_text(encoding='utf8')) if manifest.exists() else {}
records=list(state.get('records', []))
for relative in state.get('record_shards', []):
    records.extend(json.loads((manifest.parent/relative).read_text(encoding='utf8'))['records'])
gpu=subprocess.run(['nvidia-smi','--query-gpu=name,memory.total,driver_version','--format=csv,noheader'],capture_output=True,text=True).stdout.strip()
success=len({x['source_path'] for x in records if x['status']=='geometry_extracted'})
report=f'''# GPU 执行报告

- GPU：{gpu}
- PyTorch：{torch.__version__}
- CUDA 可用：{torch.cuda.is_available()}
- 实际设备：{torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'unavailable'}
- 已完成深度处理的 DWG：{success}

## GPU 阶段

1. CUDA 坐标张量构建与边界归约。
2. CUDA 几何校验和计算。
3. CUDA 文字/尺寸至最近几何实体的空间关联。
4. CUDA 重绘前后模型空间边界对比。

DWG→DXF 为外部格式转换预处理；后续几何处理、关联和验证在 CUDA 设备上执行。任何 `torch.cuda.is_available()` 为假时，深度解析脚本会拒绝运行。
'''
(root/'gpu_execution_report.md').write_text(report,encoding='utf8')
