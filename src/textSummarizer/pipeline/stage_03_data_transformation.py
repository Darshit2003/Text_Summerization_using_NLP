from src.textSummarizer.logging import logger
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_transformation import DataTransformation
import os


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e
    