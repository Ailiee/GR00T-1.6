from gr00t.configs.data.embodiment_configs import register_modality_config
from gr00t.data.embodiment_tags import EmbodimentTag
from gr00t.data.types import (
    ActionConfig,
    ActionFormat,
    ActionRepresentation,
    ActionType,
    ModalityConfig,
)


UR_Config = {
    "video": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "cam_high", 
            "cam_left_wrist", 
            "cam_right_wrist"
        ],
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "left_arm_qpos",
            "left_arm_gripper",
            "right_arm_qpos",
            "right_arm_gripper",
            "left_arm_eef",
            "right_arm_eef",
        ],
    ),
    "action": ModalityConfig(
        delta_indices=list(range(16)),  # 对 16 维 action 序列做时间索引
        modality_keys=[
            "left_arm_qpos",
            "left_arm_gripper",
            "right_arm_qpos",
            "right_arm_gripper",
        ],
        action_configs=[
            # left_arm，对应 7 维关节角
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,   # 使用相对动作（推荐）
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # left_gripper，对应 1 维夹爪
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # right_arm，对应 7 维关节角
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # right_gripper，对应 1 维夹爪
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
        ],
    ),
    "language": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "annotation.human.task_description",
        ],
    ),
}

register_modality_config(
    UR_Config,
    embodiment_tag=EmbodimentTag.NEW_EMBODIMENT,
)
