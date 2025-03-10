#from src.logger import logging

#logging.debug("This is debug message")
#logging.info("This is info message")
#logging.warning("This is warning message")
#logging.error("This is error message")
#logging.critical("This is critical message")





#######################---------------------------------####################


# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a=1+'Z'
# except Exception as e:
#     raise MyException(e,sys) from e    

from src.pipline.training_pipeline import TrainPipeline

pipeline=TrainPipeline()
pipeline.run_pipeline()