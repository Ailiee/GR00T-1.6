from gr00t.configs.data.embodiment_configs import register_modality_config
from gr00t.data.embodiment_tags import EmbodimentTag
from gr00t.data.types import (
    ActionConfig,
    ActionFormat,
    ActionRepresentation,
    ActionType,
    ModalityConfig,
)

franka_dual_arm_config = {
    "video": ModalityConfig(
        delta_indices=[0],
        modality_keys=["right", "left", "head"],
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "left_arm",
            "left_gripper",
            "left_eef_pose",
            "right_arm",
            "right_gripper",
            "right_eef_pose",
        ],
    ),
    "action": ModalityConfig(
        delta_indices=list(range(16)),
        modality_keys=[
            "left_arm",
            "left_gripper",
            "left_eef_pose",
            "right_arm",
            "right_gripper",
            "right_eef_pose",
        ],
        # ✅ 必须和 modality_keys 一样多（6 个），并且你这份数据是 ABSOLUTE
        action_configs=[
            ActionConfig(rep=ActionRepresentation.ABSOLUTE, type=ActionType.NON_EEF, format=ActionFormat.DEFAULT),  # left_arm
            ActionConfig(rep=ActionRepresentation.ABSOLUTE, type=ActionType.NON_EEF, format=ActionFormat.DEFAULT),  # left_gripper
            ActionConfig(rep=ActionRepresentation.ABSOLUTE, type=ActionType.NON_EEF, format=ActionFormat.DEFAULT),  # left_eef_pose
            ActionConfig(rep=ActionRepresentation.ABSOLUTE, type=ActionType.NON_EEF, format=ActionFormat.DEFAULT),  # right_arm
            ActionConfig(rep=ActionRepresentation.ABSOLUTE, type=ActionType.NON_EEF, format=ActionFormat.DEFAULT),  # right_gripper
            ActionConfig(rep=ActionRepresentation.ABSOLUTE, type=ActionType.NON_EEF, format=ActionFormat.DEFAULT),  # right_eef_pose
        ],
    ),
    "language": ModalityConfig(
        delta_indices=[0],
        modality_keys=["annotation.human.task_description"],
    ),
}

register_modality_config(franka_dual_arm_config, embodiment_tag=EmbodimentTag.NEW_EMBODIMENT)
