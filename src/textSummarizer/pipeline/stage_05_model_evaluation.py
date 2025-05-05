from src.textSummarizer.logging import logger
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_evaluation import ModelEvaluation
import os


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()
        except Exception as e:
            raise e
    