set -x -e

export NUM_GPUS=1

CUDA_VISIBLE_DEVICES=0 uv run python gr00t/experiment/launch_finetune.py \
  --base-model-path nvidia/GR00T-N1.6-3B \
  --dataset-path demo_data/g1_pick_connector \
  --embodiment-tag NEW_EMBODIMENT \
  --modality-config-path examples/Genie1/g1_config.py \
  --num-gpus $NUM_GPUS \
  --output-dir /mnt/data1/gr00t_ckpt/g1_finetune \
  --save-total-limit 5 \
  --save-steps 5000 \
  --max-steps 200000 \
  --no-tune-diffusion-model \
  --global-batch-size 32 \
  --color-jitter-params brightness 0.3 contrast 0.4 saturation 0.5 hue 0.08 \
  --dataloader-num-workers 4
    # --use-wandb \