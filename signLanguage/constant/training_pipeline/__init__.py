import os
# Inside artifact folder we'll store the data
ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
# Here in data_ingestion folder we'll download the data
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

# Here we'll do the unzip operation on the downloaded data
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://github.com/Ishita2407/data/raw/refs/heads/main/Sign%20language%20Model.v1i.yolov5pytorch.zip"



# """
# Data Validation realted contant start with DATA_VALIDATION VAR NAME
# """

# DATA_VALIDATION_DIR_NAME: str = "data_validation"

# DATA_VALIDATION_STATUS_FILE = 'status.txt'

# DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yaml"]



# """
# MODEL TRAINER related constant start with MODEL_TRAINER var name
# """
# MODEL_TRAINER_DIR_NAME: str = "model_trainer"

# MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

# MODEL_TRAINER_NO_EPOCHS: int = 1

# MODEL_TRAINER_BATCH_SIZE: int = 16




# """
# MODEL PUSHER related constant start with MODEL_PUSHER var name
# """
# BUCKET_NAME = "sign-lang-2024"
# S3_MODEL_NAME = "best.pt"