from src.logger import logging
from src.exception import CustomException

import os,sys
import yaml
import pickle,dill


def read_yaml(file_path:str)->dict:
    try:
        with open(file_path,"rb") as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise CustomException(e,sys)
    
def write_yaml(file_path,report,replace:bool=False):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(report,file)
    except Exception as e:
        raise CustomException(e,sys)

