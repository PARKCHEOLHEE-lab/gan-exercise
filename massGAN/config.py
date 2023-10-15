import os
import torch
import numpy as np
import random


class ModelConfig:
    """Configuration related to the GAN models
    """

    DEVICE = "cpu"
    if torch.cuda.is_available():
        DEVICE = "cuda"
        
    SEED = 777
    
    GENERATOR_INIT_OUT_CHANNELS = 256
    DISCRIMINATOR_INIT_OUT_CHANNELS = 64
    
    BATCH_SIZE = 100
    
    @staticmethod
    def set_seed(seed: int = SEED):
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        np.random.seed(seed)
        random.seed(seed)
        
        print(
            f"""
            Seeds set for torch        : {torch.initial_seed()}
            Seeds set for torch on GPU : {torch.cuda.initial_seed()}
            Seeds set for numpy        : {seed}
            Seeds set for random       : {seed}
            """
        )
    

class PreprocessConfig:
    """Configuration related to the preprocessing data
    """
        
    OBJ_FORMAT = ".obj"
    BINVOX_FORMAT = ".binvox"
    
    BINVOX_RESOLUTION = 128

    ROTATION_MAX = 360
    ROTATION_INTERVAL = 36

    X = (1, 0, 0)
    Y = (0, 1, 0)
    Z = (0, 0, 1)

    DATA_BASE_DIR = "data"
    DATA_ORIGINAL_DIR = "original"
    DATA_PREPROCESSED_DIR = "preprocessed"

    DATA_ORIGINAL_DIR_MERGED = os.path.join(DATA_BASE_DIR, DATA_ORIGINAL_DIR)
    DATA_PREPROCESSED_DIR_MERGED = os.path.join(DATA_BASE_DIR, DATA_PREPROCESSED_DIR)
    
    
class Config(ModelConfig, PreprocessConfig):
    """Wrapper class
    """