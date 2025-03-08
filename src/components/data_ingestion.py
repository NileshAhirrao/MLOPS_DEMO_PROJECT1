import os
import sys
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.data_access.proj1_data import Proj1Data
from src.logger import logging
from src.exception import MyException
import pandas as pd
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise MyException(e, sys)


    def export_data_into_fearure_store(self)->pd.DataFrame:

        try:
            logging.info(f"Exporting data from MongoDB") 
            my_data=Proj1Data()
            dataframe=my_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            logging.info(f"Shape of the Dataframe: {dataframe.shape}")

            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            file_path=os.path.dirname(feature_store_file_path)
            os.makedirs(file_path,exist_ok=True)

            logging.info(f"Saving Exporting data into feature store path: {feature_store_file_path}")

            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise MyException(e, sys)
        


    def split_data_as_train_test(self,dataframe:pd.DataFrame)->None:

        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info(f"Split performed on Dataframe ") 

            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)

            logging.info(f"Exporting data ino train and test file path")

            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info(f"Exported train and test set to file path") 
        except Exception as e:
            raise MyException(e, sys) from e
        

    def initiate_data_ingestion(self)->DataIngestionArtifact:

        logging.info(f"Entered in initiate_data_ingestion method of DataIngestion Class")   
        try:
            dataframe=self.export_data_into_fearure_store()
            logging.info("Got the data from Mongo DB")

            self.split_data_as_train_test(dataframe)

            logging.info("Performed train and test on dataset")

            data_ingestion_artifact= DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,test_file_path=self.data_ingestion_config.testing_file_path)

            logging.info(f"Data Ingestion Artifact :{data_ingestion_artifact}")

            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e,sys) from e
        



            

            


            



        
        
