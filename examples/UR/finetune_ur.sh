set -x -e

export NUM_GPUS=1

CUDA_VISIBLE_DEVICES=7 uv run python gr00t/experiment/launch_finetune.py \
  --base-model-path nvidia/GR00T-N1.6-3B \
  --dataset-path /workspace1/data/UR_data_20260105_v2.1 \
  --embodiment-tag NEW_EMBODIMENT \
  --modality-config-path /workspace/gr00t/examples/UR/UR_config.py \
  --num-gpus $NUM_GPUS \
  --output-dir /workspace1/data/GR00T/UR_data_20260105_v2.1 \
  --save-total-limit 5 \
  --save-steps 5000 \
  --max-steps 200000 \
  --global-batch-size 32 \
  --color-jitter-params brightness 0.3 contrast 0.4 saturation 0.5 hue 0.08 \
  --dataloader-num-workers 4 \
  --use-wandb 
    #  --no-tune-diffusion-model \