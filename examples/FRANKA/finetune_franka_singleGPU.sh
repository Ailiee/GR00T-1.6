set -x -e

export NUM_GPUS=1

CUDA_VISIBLE_DEVICES=0 uv run python gr00t/experiment/launch_finetune.py \
  --base-model-path nvidia/GR00T-N1.6-3B \
  --dataset-path /workspace2/franka_single_dataset/franka_1217_v3_200 \
  --embodiment-tag NEW_EMBODIMENT \
  --modality-config-path /workspace/gr00t/examples/FRANKA/franka_single_modality.py \
  --num-gpus $NUM_GPUS \
  --output-dir /workspace/gr00t/franka_checkpoints_1GPU \
  --save-total-limit 5 \
  --save-steps 10 \
  --max-steps 2000 \
  --no-tune-diffusion-model \
  --global-batch-size 64 \
  --color-jitter-params brightness 0.3 contrast 0.4 saturation 0.5 hue 0.08 \
  --dataloader-num-workers 4
    # --use-wandb \