# import os
# import sys
# import yaml
# import shutil
# import zipfile

# from signLanguage.utils.main_utils import read_yaml_file
# from signLanguage.logger import logging
# from signLanguage.exception import SignException
# from signLanguage.entity.config_entity import ModelTrainerConfig
# from signLanguage.entity.artifacts_entity import ModelTrainerArtifact


# class ModelTrainer:
#     def __init__(self, model_trainer_config: ModelTrainerConfig):
#         self.model_trainer_config = model_trainer_config

#     def initiate_model_trainer(self) -> ModelTrainerArtifact:
#         logging.info("Entered initiate_model_trainer method of ModelTrainer class")
#         try:
#             logging.info("Unzipping data...")

#             zip_path = "Sign_language_data.zip"
#             extract_to = "unzipped_data"

#             if not os.path.exists(zip_path):
#                 raise FileNotFoundError(f"{zip_path} not found")

#             # Unzip data
#             with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#                 zip_ref.extractall(extract_to)

#             os.remove(zip_path)  # Remove zip file after extraction

#             # Locate and read data.yaml
#             data_yaml_path = os.path.join(extract_to, "data.yaml")
#             if not os.path.exists(data_yaml_path):
#                 raise FileNotFoundError(f"{data_yaml_path} not found")

#             # with open(data_yaml_path, 'r') as stream:
#             #     num_classes = str(yaml.safe_load(stream)['nc'])
#             # Read and patch data.yaml with absolute paths
#             with open(data_yaml_path, 'r') as stream:
#                 data_yaml = yaml.safe_load(stream)
#                 num_classes = str(data_yaml['nc'])

#                 # Fix train and val paths
#                 data_yaml['train'] = os.path.abspath(os.path.join(extract_to, 'train'))
#                 data_yaml['val'] = os.path.abspath(os.path.join(extract_to, 'valid'))
#                 data_yaml['test'] = os.path.abspath(os.path.join(extract_to, 'test'))

#             # Save updated data.yaml
#             with open(data_yaml_path, 'w') as stream:
#                 yaml.dump(data_yaml, stream)


#             # Load model config
#             model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
#             config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
#             config['nc'] = int(num_classes)

#             # Write custom config
#             custom_model_cfg_path = f'yolov5/models/custom_{model_config_file_name}.yaml'
#             with open(custom_model_cfg_path, 'w') as f:
#                 yaml.dump(config, f)

#             # Train model using YOLOv5 CLI
#             os.system(
#                 f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} "
#                 f"--epochs {self.model_trainer_config.no_epochs} --data ../{data_yaml_path} "
#                 f"--cfg ./models/custom_{model_config_file_name}.yaml "
#                 f"--weights {self.model_trainer_config.weight_name} --name yolov5s_results --cache"
#             )

#             # Copy trained model
#             trained_model_path = "yolov5/runs/train/yolov5s_results/weights/best.pt"
#             if not os.path.exists(trained_model_path):
#                 raise FileNotFoundError(f"Trained model not found at {trained_model_path}")

#             shutil.copy(trained_model_path, "yolov5/")

#             # Copy model to final directory
#             os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
#             shutil.copy(
#                 trained_model_path,
#                 os.path.join(self.model_trainer_config.model_trainer_dir, "best.pt")
#             )

#             # Cleanup
#             shutil.rmtree("yolov5/runs", ignore_errors=True)
#             shutil.rmtree("train", ignore_errors=True)
#             shutil.rmtree("test", ignore_errors=True)
#             os.remove(data_yaml_path)

#             model_trainer_artifact = ModelTrainerArtifact(
#                 trained_model_file_path="yolov5/best.pt"
#             )

#             logging.info("Exited initiate_model_trainer method of ModelTrainer class")
#             logging.info(f"Model trainer artifact: {model_trainer_artifact}")

#             return model_trainer_artifact

#         except Exception as e:
#             raise SignException(e, sys)
import os
import sys
import yaml
import shutil
import zipfile

from signLanguage.utils.main_utils import read_yaml_file
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import ModelTrainerConfig
from signLanguage.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def get_latest_training_weights_path(self):
        try:
            runs_dir = os.path.join("yolov5", "runs", "train")
            if not os.path.exists(runs_dir):
                raise FileNotFoundError("Training runs directory not found.")

            # Get list of all subfolders
            folders = [
                os.path.join(runs_dir, d) for d in os.listdir(runs_dir)
                if os.path.isdir(os.path.join(runs_dir, d))
            ]
            if not folders:
                raise FileNotFoundError("No training folders found in runs/train.")

            # Sort by latest modified folder
            latest_folder = max(folders, key=os.path.getmtime)
            weights_path = os.path.join(latest_folder, "weights", "best.pt")

            if not os.path.exists(weights_path):
                raise FileNotFoundError(f"Trained model not found at {weights_path}")

            return weights_path

        except Exception as e:
            raise SignException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        try:
            logging.info("Unzipping data...")

            zip_path = "Sign_language_data.zip"
            extract_to = "unzipped_data"

            if not os.path.exists(zip_path):
                raise FileNotFoundError(f"{zip_path} not found")

            # Unzip data
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)

            os.remove(zip_path)  # Remove zip file after extraction

            # Locate and read data.yaml
            data_yaml_path = os.path.join(extract_to, "data.yaml")
            if not os.path.exists(data_yaml_path):
                raise FileNotFoundError(f"{data_yaml_path} not found")

            # Read and patch data.yaml with absolute paths
            with open(data_yaml_path, 'r') as stream:
                data_yaml = yaml.safe_load(stream)
                num_classes = str(data_yaml['nc'])

                data_yaml['train'] = os.path.abspath(os.path.join(extract_to, 'train'))
                data_yaml['val'] = os.path.abspath(os.path.join(extract_to, 'valid'))
                data_yaml['test'] = os.path.abspath(os.path.join(extract_to, 'test'))

            # Save updated data.yaml
            with open(data_yaml_path, 'w') as stream:
                yaml.dump(data_yaml, stream)

            # Load model config
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
            config['nc'] = int(num_classes)

            # Write custom config
            custom_model_cfg_path = f'yolov5/models/custom_{model_config_file_name}.yaml'
            with open(custom_model_cfg_path, 'w') as f:
                yaml.dump(config, f)

            # Train model using YOLOv5 CLI
            os.system(
                f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} "
                f"--epochs {self.model_trainer_config.no_epochs} --data ../{data_yaml_path} "
                f"--cfg ./models/custom_{model_config_file_name}.yaml "
                f"--weights {self.model_trainer_config.weight_name} --name yolov5s_results --cache"
            )

            # Get trained model path
            trained_model_path = self.get_latest_training_weights_path()

            # Copy trained model to yolov5 root
            shutil.copy(trained_model_path, "yolov5/")

            # Copy model to final directory
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            shutil.copy(
                trained_model_path,
                os.path.join(self.model_trainer_config.model_trainer_dir, "best.pt")
            )

            # Cleanup
            shutil.rmtree("yolov5/runs", ignore_errors=True)
            shutil.rmtree("train", ignore_errors=True)
            shutil.rmtree("test", ignore_errors=True)
            os.remove(data_yaml_path)

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt"
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)
