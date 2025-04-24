import sys

from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import TrainingPipelineConfig

from src.logger import logging
from src.exception import CustomException

if __name__=="__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        
        logging.info("Initiating data ingestion....")

        path = data_ingestion.initialise_data_ingestion()
        
        print(path)

    except Exception as e:
        raise CustomException(e,sys)


