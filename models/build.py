
from .as_mlp import AS_MLP

def build_model(config):
    model_type = config.MODEL.TYPE
    if model_type == 'asmlp':
        model = AS_MLP(img_size=config.DATA.IMG_SIZE,
                                patch_size=config.MODEL.ASMLP.PATCH_SIZE,
                                in_chans=config.MODEL.ASMLP.IN_CHANS,
                                num_classes=config.MODEL.NUM_CLASSES,
                                embed_dim=config.MODEL.ASMLP.EMBED_DIM,
                                depths=config.MODEL.ASMLP.DEPTHS,
                                shift_size=config.MODEL.ASMLP.SHIFT_SIZE,
                                mlp_ratio=config.MODEL.ASMLP.MLP_RATIO,
                                drop_rate=config.MODEL.DROP_RATE,
                                drop_path_rate=config.MODEL.DROP_PATH_RATE,
                                patch_norm=config.MODEL.ASMLP.PATCH_NORM,
                                use_checkpoint=config.TRAIN.USE_CHECKPOINT)
    else:
        raise NotImplementedError(f"Unkown model: {model_type}")

    return model

