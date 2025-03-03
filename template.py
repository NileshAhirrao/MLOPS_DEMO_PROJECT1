import os
from pathlib import Path

main_dir='src'

list_of_files=[


    f"{main_dir}/__init__.py",
    f"{main_dir}/components/__init__.py",
    f"{main_dir}/components/data_ingestion.py",
    f"{main_dir}/components/data_validation.py",
    f"{main_dir}/components/data_transformation.py",    
    f"{main_dir}/components/model_trainer.py",
    f"{main_dir}/components/model_evaluation.py",
    f"{main_dir}/components/model_pusher.py"
    f"{main_dir}/configuration/__init__.py"
    f"{main_dir}/configuration/mongo_db_connection.py",
    f"{main_dir}/configuration/aws_connection.py",
    f"{main_dir}/cloud_storage/__init__.py",
    f"{main_dir}/cloud_storage/aws_storage.py",
    f"{main_dir}/data_access/__init__.py",
    f"{main_dir}/data_access/proj1_data.py",
    f"{main_dir}/constants/__init__.py",
    f"{main_dir}/entity/__init__.py",
    f"{main_dir}/entity/config_entity.py",
    f"{main_dir}/entity/artifact_entity.py",
    f"{main_dir}/entity/estimator.py",
    f"{main_dir}/entity/s3_estimator.py",
    f"{main_dir}/exception/__init__.py",
    f"{main_dir}/logger/__init__.py",
    f"{main_dir}/pipline/__init__.py",
    f"{main_dir}/pipline/training_pipeline.py",
    f"{main_dir}/pipline/prediction_pipeline.py",
    f"{main_dir}/utils/__init__.py",
    f"{main_dir}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",

]


for filepaths in list_of_files:
    file_path=Path(filepaths)
    filedir,filename=os.path.split(file_path)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)

    if (not os .path.exists(file_path) or os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
    else:
        print(f"File is already prasent : {file_path}")
            

