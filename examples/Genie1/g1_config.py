from gr00t.configs.data.embodiment_configs import register_modality_config
from gr00t.data.embodiment_tags import EmbodimentTag
from gr00t.data.types import (
    ActionConfig,
    ActionFormat,
    ActionRepresentation,
    ActionType,
    ModalityConfig,
)


g1_config = {
    "video": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "head",
            "hand_left",
            "hand_right",
        ],
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "left_arm",
            "left_gripper",
            "right_arm",
            "right_gripper",
        ],
    ),
    "action": ModalityConfig(
        delta_indices=list(range(16)),  # 对 16 维 action 序列做时间索引
        modality_keys=[
            "left_arm",
            "left_gripper",
            "right_arm",
            "right_gripper",
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
                rep=ActionRepresentation.RELATIVE,
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
                rep=ActionRepresentation.RELATIVE,
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
    g1_config,
    embodiment_tag=EmbodimentTag.NEW_EMBODIMENT,
)
