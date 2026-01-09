set -x -e

export NUM_GPUS=1

# torchrun --nproc_per_node=$NUM_GPUS --master_port=29500 \
CUDA_VISIBLE_DEVICES=0 python \
    gr00t/experiment/launch_finetune.py \
    --base_model_path nvidia/GR00T-N1.6-3B \
    --dataset_path datasets/galaxea_R1/ \
    --modality_config_path examples/GALAXEA_R1/r1_config.py \
    --embodiment_tag GALAXEA_R1 \
    --num_gpus $NUM_GPUS \
    --output_dir gr00t/galaxea_r1_finetune \
    --save_steps 10 \
    --save_total_limit 5 \
    --max_steps 10000 \
    --warmup_ratio 0.05 \
    --weight_decay 1e-5 \
    --learning_rate 1e-4 \
    --global_batch_size 1 \
    --color_jitter_params brightness 0.3 contrast 0.4 saturation 0.5 hue 0.08 \
    --dataloader_num_workers 0
    # --use_wandb \
