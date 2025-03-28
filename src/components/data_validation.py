import sys
import os
import json
import pandas as pd
from pandas import DataFrame
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from src.exception import MyException
from src.logger import logging
from src.utils.main_utils import read_yaml_file,write_yaml_file
from src.constants import SCHEMA_FILE_PATH

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config=read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException(e,sys)
        

    def validate_number_of_columns(self,dataframe:DataFrame)->bool:
        try:
            status=len(dataframe.columns)==len(self._schema_config["columns"])
            logging.info(f"IS required Columns Present:[{status}]")
            return status
        except Exception as e:
            raise MyException(e,sys)

    def is_column_exist(self,df:DataFrame)->bool:
        try:
            dataframe_columns=df.columns
            missing_categorical_columns=[]
            missing_numerical_columns=[]
            for col in self._schema_config["numerical_columns"]:
                if col not in dataframe_columns:
                    missing_numerical_columns.append(col)
            if len(missing_numerical_columns)>0:
                logging.info(f"Missing Columns: {missing_numerical_columns}")


            for col1 in self._schema_config["categorical_columns"]:
                if col1 not in dataframe_columns:
                    missing_categorical_columns.append(col1)
            if  len(missing_categorical_columns)>0:
                logging.info(f"Missing Columns: {missing_categorical_columns}")       

            return False if len(missing_numerical_columns)>0 or len(missing_categorical_columns)>0 else True
        except Exception as e:
            raise MyException(e,sys) from e


    @staticmethod
    def read_data(file_path)->DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise MyException(e,sys)      
        
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            validation_error_msg=""
            logging.info("Start Data Validation")
            train_df,test_df=(DataValidation.read_data(file_path=self.data_ingestion_artifact.trained_file_path),
                              DataValidation.read_data(file_path=self.data_ingestion_artifact.test_file_path))  

            status= self.validate_number_of_columns(dataframe=train_df)
            
            if not status:
                validation_error_msg+=f"Columns are missing in Trained DataFrame"
            else:
                logging.info(f"All Columns are present in Trained DataFrame: {status}")   


            status=self.validate_number_of_columns(dataframe=test_df)
            if not status:
                validation_error_msg+=f"Columns are missing in Test DataFrame" 
            else:
                logging.info(f"All Columns are present in Test DataFrame: {status}")  


            status=self.is_column_exist(df=train_df)
            if not status:
                validation_error_msg+=f"Columns are missing in train DataFrame"
            else:
                logging.info(f"All Cat/Int Columns are present in Train DataFrame: {status}")

            status=self.is_column_exist(df=test_df)
            if not status:
                validation_error_msg+=f"Columns are missing in Test DataFrame"
            else:
                logging.info(f"All Cat/Int Columns are present in Test DataFrame: {status}")



            validation_status=len(validation_error_msg)==0

            data_validation_artifact=DataValidationArtifact(
                validation_status=validation_status,
                message=validation_error_msg,
                validation_report_file_path=self.data_validation_config.validation_report_file_path
            )   

            report_dir=os.path.dirname(self.data_validation_config.validation_report_file_path)
            os.makedirs(report_dir,exist_ok=True)

            validation_report={
                "validation_status":validation_status,
                "message":validation_error_msg.strip()
            }

            with open(self.data_validation_config.validation_report_file_path,"w") as report_file:
                json.dump(validation_report,report_file,indent=4)


            logging.info(f"Data Validation artifact created and saved on JSON")   
            logging.info(f"Data Validation Artifact: {data_validation_artifact}") 

            return data_validation_artifact
        except Exception as e:
            raise MyException(e,sys) from e
        












             


    






