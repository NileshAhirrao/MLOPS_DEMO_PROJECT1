import sys
import pandas as pd
from pandas import DataFrame
from sklearn.pipeline import Pipeline
from src.logger import logging
from src.exception import MyException


class MyModel:
    def __init__(self,preprocessing_object:Pipeline,trained_model_object:object):
        self.preprocessing_object=preprocessing_object
        self.trained_model_object=trained_model_object