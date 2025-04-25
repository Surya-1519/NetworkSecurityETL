import sys

from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig,DataValidationConfig
from src.entity.config_entity import TrainingPipelineConfig
from src.components.data_validation import DataValidation

from src.logger import logging
from src.exception import CustomException

if __name__=="__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        
        logging.info("Initiating data ingestion....")

        data_ingestion_artifact = data_ingestion.initialise_data_ingestion()
        
        logging.info("Data ingestion successful!")
        
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_validation_config,data_ingestion_artifact)
        logging.info("Initiating data validation....")
        data_validation_artifact = data_validation.initialise_data_validation()
        logging.info("Data validation successful!")
        

        print(data_validation_artifact)
        
    except Exception as e:
        raise CustomException(e,sys)


