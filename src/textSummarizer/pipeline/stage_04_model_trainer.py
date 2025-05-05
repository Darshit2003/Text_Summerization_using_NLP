from src.textSummarizer.logging import logger
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_trainer import ModelTrainer
import os


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e
    