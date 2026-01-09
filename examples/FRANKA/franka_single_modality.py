from gr00t.configs.data.embodiment_configs import register_modality_config
from gr00t.data.embodiment_tags import EmbodimentTag
from gr00t.data.types import ModalityConfig

# my_arm_config = {
#     "video": ModalityConfig(
#         delta_indices=[0],
#         modality_keys=["head", "hand"],
#     ),
#     "state": ModalityConfig(
#         delta_indices=[0],
#         modality_keys=["single_arm", "gripper"],
#     ),
#     "action": ModalityConfig(
#         delta_indices=[0],  # 单步动作：最稳
#         modality_keys=["single_arm", "gripper"],
#     ),
# }

# register_modality_config(my_arm_config, embodiment_tag=EmbodimentTag.NEW_EMBODIMENT)

my_arm_config = {
    "video": ModalityConfig(
        delta_indices=[0],
        modality_keys=["head", "hand"],
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=["single_arm", "gripper"],
    ),
    "action": ModalityConfig(
        delta_indices=[0],
        modality_keys=["single_arm", "gripper"],
    ),
    "language": ModalityConfig(
        delta_indices=[0],
        modality_keys=["task"],
    ),
}

register_modality_config(my_arm_config, embodiment_tag=EmbodimentTag.NEW_EMBODIMENT)
