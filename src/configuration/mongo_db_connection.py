import os
import sys
import pymongo
import certifi


from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME,MONGODB_URL_KEY


#Load the certificate autherity to avoid timeout error while connecting to MongoDB
ca=certifi.where()

class MongoDBClient:
    def __init__(self,database_name:str=DATABASE_NAME)->None:
        
        try:
            if MongoDBClient.client is None:
                mongo_db_url=os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environemnt Variable '{MONGODB_URL_KEY}' is not set")
                MongoDBClient.client=pymongo.MongoClient(mongo_db_url,tlscafile=ca)
            self.client=MongoDBClient.client
            self.database_name=self.client[database_name] 
            self.database=database_name
            logging.info("MONGO DB Connection Succesful") 
        except Exception as e:
            raise MyException(e,sys)      
