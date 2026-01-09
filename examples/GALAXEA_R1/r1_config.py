from gr00t.configs.data.embodiment_configs import register_modality_config
from gr00t.data.embodiment_tags import EmbodimentTag
from gr00t.data.types import (
    ActionConfig,
    ActionFormat,
    ActionRepresentation,
    ActionType,
    ModalityConfig,
)


r1_config = {
    "video": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "head",          # observation.images.head
            "hand_left",     # observation.images.hand_left
            "hand_right",    # observation.images.hand_right
        ],
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "left_arm",      # 0-6,   6维
            "left_hand",     # 6-8,   2维
            "right_arm",     # 8-14,  6维
            "right_hand",    # 14-16, 2维
            "head",          # 16-19, 3维
            "neck",          # 19-22, 3维
            "waist",         # 22-25, 3维
            "left_leg",      # 25-31, 6维
            "right_leg",     # 31-37, 6维
            "torso",         # 37-44, 7维
        ],
    ),
    "action": ModalityConfig(
        delta_indices=list(range(16)),  # 16 步 action horizon
        modality_keys=[
            "left_arm",      # 0-6,   6维
            "left_hand",     # 6-8,   2维
            "right_arm",     # 8-14,  6维
            "right_hand",    # 14-16, 2维
            "head",          # 16-19, 3维
            "neck",          # 19-22, 3维
            "waist",         # 22-25, 3维
            "left_leg",      # 25-31, 6维
            "right_leg",     # 31-37, 6维
            "torso",         # 37-44, 7维
        ],
        action_configs=[
            # left_arm, 6维
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # left_hand, 2维
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # right_arm, 6维
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # right_hand, 2维
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # head, 3维
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # neck, 3维
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # waist, 3维
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # left_leg, 6维
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # right_leg, 6维
            ActionConfig(
                rep=ActionRepresentation.RELATIVE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT,
            ),
            # torso, 7维
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
            "annotation.human.action.task_description",
        ],
    ),
}

register_modality_config(
    r1_config,
    embodiment_tag=EmbodimentTag.NEW_EMBODIMENT,
)
