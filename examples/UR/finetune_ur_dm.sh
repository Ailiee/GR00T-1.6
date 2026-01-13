#!/bin/bash
set -x -e

export NUM_GPUS=4
export CUDA_VISIBLE_DEVICES=0,1,2,3
# 添加这些环境变量
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128,expandable_segments:True

# ============ NCCL 通信优化 ============
export NCCL_P2P_DISABLE=0              # 启用 GPU 直接通信 (RTX 5090 支持 PCIe P2P)
export NCCL_IB_DISABLE=1               # 禁用 InfiniBand
export NCCL_SHM_DISABLE=0              # 启用共享内存加速
export CUDA_DEVICE_ORDER=PCI_BUS_ID    # 确保 GPU 顺序一致
export NCCL_DEBUG=WARN                 # 降低日志级别 (INFO 太吵，改为 WARN)
export NCCL_SOCKET_IFNAME=lo           # 使用本地回环

# ============ 数据加载优化 ============
export OMP_NUM_THREADS=8               # OpenMP 线程数

uv run deepspeed \
  --num_gpus=$NUM_GPUS \
  --master_port=29500 \
  gr00t/experiment/launch_finetune.py \
  --base-model-path nvidia/GR00T-N1.6-3B \
  --dataset-path /workspace1/data/UR_data_20260105_v2.1 \
  --embodiment-tag NEW_EMBODIMENT \
  --modality-config-path /workspace/gr00t/examples/UR/UR_config.py \
  --num-gpus $NUM_GPUS \
  --output-dir /workspace1/data/GR00T/UR_data_20260105_v2.1 \
  --deepspeed-config ds_config_zero3.json \
  --save-total-limit 5 \
  --save-steps 5000 \
  --max-steps 50000 \
  --global-batch-size 32 \
  --color-jitter-params brightness 0.3 contrast 0.4 saturation 0.5 hue 0.08 \
  --dataloader-num-workers 12