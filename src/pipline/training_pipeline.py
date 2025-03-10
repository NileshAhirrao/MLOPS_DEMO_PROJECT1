import sys
from src.exception import MyException
from src.logger import logging

from src.components.data_ingestion import DataIngestion

from src.entity.config_entity import (DataIngestionConfig,)


from src.entity.artifact_entity import (DataIngestionArtifact,)



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()




    def start_data_ingestion(self)->DataIngestionArtifact:

        try:
            logging.info(f"Entered into start_data_ingestion method of TrainPipeline")   
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config) 
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("Received Train and Test Data from MongoDB")
            logging.info(f"Exited into start_data_ingestion method of TrainPipeline")

            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e, sys) from e
        


    def run_pipeline(self,)->None:
        try:
          data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise MyException(e,sys)
          


