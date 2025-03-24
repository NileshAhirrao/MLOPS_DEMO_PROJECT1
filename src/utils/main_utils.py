import os
import sys
import yaml
import dill

import pandas as pd
from pandas import DataFrame
import numpy as np
from src.exception import MyException
from src.logger import logging



def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise MyException(e,sys) from e



def write_yaml_file(file_path:str,content:object,replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path),exist_ok=True)
            with open(file_path,'w') as file:
                yaml.dump(content,file)
    except Exception as e:
        raise MyException(e,sys) from e


def load_object(file_path:str)->object:
    try:
        with open(file_path,"rb") as file_obj:
            obj=dill.load(file_obj)
            return obj
    except Exception as e:
        raise MyException(e,sys) from e
    

def save_object(file_path:str,obj:object)->None:
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)   
        with open(file_path,"wb") as obj_file:
            dill.dump(obj,obj_file)
    except Exception as e:
        raise MyException(e,sys) from e
           
    

def load_numpy_array_data(file_path:str)->np.array:
    try:
        with open(file_path,'rb') as array_file:
            return np.load(array_file)
    except Exception as e:
        raise MyException(e,sys) from e


def save_numpy_array_data(file_path:str,array:np.array):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            return np.save(file_obj,array)
    except Exception as e:
        raise MyException(e,sys) from e