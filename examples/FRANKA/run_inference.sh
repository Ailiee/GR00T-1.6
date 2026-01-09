#!/bin/bash
# Franka双臂推理系统启动脚本

set -e

echo "========================================="
echo "Franka双臂GR00T推理系统"
echo "========================================="
echo ""

# 配置参数
CHECKPOINT_PATH="/workspace/gr00t/franka_checkpoints/checkpoint-200000"
SERVER_HOST="localhost"
SERVER_PORT=5555
CONTROL_FREQ=10
TASK_DESCRIPTION="Pick and place objects"

# ROS2话题配置（请根据实际情况修改）
CAMERA_RIGHT="/franka_right/camera/image_raw"
CAMERA_LEFT="/franka_left/camera/image_raw"
CAMERA_HEAD="/head_camera/image_raw"
LEFT_ARM_JOINT="/franka_left/joint_states"
RIGHT_ARM_JOINT="/franka_right/joint_states"
LEFT_EEF_POSE="/franka_left/end_effector_pose"
RIGHT_EEF_POSE="/franka_right/end_effector_pose"

# 帮助信息
show_help() {
    echo "使用方法: $0 [选项]"
    echo ""
    echo "选项:"
    echo "  --server-only          仅启动推理服务器"
    echo "  --client-only          仅启动ROS2客户端（需要服务器已运行）"
    echo "  --check-topics         检查ROS2话题"
    echo "  --task DESCRIPTION     设置任务描述"
    echo "  --help                 显示此帮助信息"
    echo ""
}

# 启动推理服务器
start_server() {
    echo "步骤 1/2: 启动推理服务器"
    echo "-----------------------------------------"
    echo "checkpoint路径: $CHECKPOINT_PATH"
    echo "服务器地址: $SERVER_HOST:$SERVER_PORT"
    echo ""
    
    if [ ! -d "$CHECKPOINT_PATH" ]; then
        echo "错误: checkpoint路径不存在: $CHECKPOINT_PATH"
        exit 1
    fi
    
    python /workspace/gr00t/gr00t/eval/run_gr00t_server.py \
        --embodiment-tag NEW_EMBODIMENT \
        --model-path "$CHECKPOINT_PATH" \
        --device cuda:0 \
        --host 0.0.0.0 \
        --port $SERVER_PORT \
        --strict False
}

# 启动ROS2客户端
start_client() {
    echo "步骤 2/2: 启动ROS2客户端"
    echo "-----------------------------------------"
    echo "服务器地址: $SERVER_HOST:$SERVER_PORT"
    echo "控制频率: $CONTROL_FREQ Hz"
    echo "任务描述: $TASK_DESCRIPTION"
    echo ""
    
    # 等待服务器启动
    if [ "$1" != "--skip-wait" ]; then
        echo "等待服务器启动..."
        sleep 5
    fi
    
    python /workspace/gr00t/examples/FRANKA/franka_ros2_client.py \
        --server-host "$SERVER_HOST" \
        --server-port $SERVER_PORT \
        --control-freq $CONTROL_FREQ \
        --task-description "$TASK_DESCRIPTION" \
        --camera-right "$CAMERA_RIGHT" \
        --camera-left "$CAMERA_LEFT" \
        --camera-head "$CAMERA_HEAD" \
        --left-arm-joint "$LEFT_ARM_JOINT" \
        --right-arm-joint "$RIGHT_ARM_JOINT" \
        --left-eef-pose "$LEFT_EEF_POSE" \
        --right-eef-pose "$RIGHT_EEF_POSE"
}

# 检查ROS2话题
check_topics() {
    echo "检查ROS2话题"
    echo "-----------------------------------------"
    python /workspace/gr00t/examples/FRANKA/check_ros2_topics.py
}

# 启动完整系统（服务器+客户端）
start_full_system() {
    echo "启动完整系统（服务器 + 客户端）"
    echo "========================================="
    echo ""
    echo "注意: 此脚本将在后台启动服务器，然后启动客户端"
    echo "按 Ctrl+C 将同时停止服务器和客户端"
    echo ""
    
    # 启动服务器（后台）
    start_server &
    SERVER_PID=$!
    
    # 等待服务器启动
    echo ""
    echo "等待服务器启动..."
    sleep 10
    
    # 检查服务器是否还在运行
    if ! kill -0 $SERVER_PID 2>/dev/null; then
        echo "错误: 服务器启动失败"
        exit 1
    fi
    
    echo "服务器已启动 (PID: $SERVER_PID)"
    echo ""
    
    # 启动客户端
    start_client --skip-wait
    
    # 客户端退出后，停止服务器
    echo ""
    echo "正在停止服务器..."
    kill $SERVER_PID 2>/dev/null || true
    wait $SERVER_PID 2>/dev/null || true
    echo "服务器已停止"
}

# 解析命令行参数
case "${1:-}" in
    --server-only)
        start_server
        ;;
    --client-only)
        start_client --skip-wait
        ;;
    --check-topics)
        check_topics
        ;;
    --task)
        if [ -z "${2:-}" ]; then
            echo "错误: --task 需要一个参数"
            exit 1
        fi
        TASK_DESCRIPTION="$2"
        shift 2
        start_full_system
        ;;
    --help|-h)
        show_help
        ;;
    "")
        start_full_system
        ;;
    *)
        echo "未知选项: $1"
        echo ""
        show_help
        exit 1
        ;;
esac




