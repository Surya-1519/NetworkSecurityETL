from src.logger import logging
from src.exception import CustomException

import os,sys
import yaml
import pickle
import numpy as np


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

def save_numpy_array(file_path:str,data:np.array):
    try:
        logging.info("Entering folder to save the array...")
        folder = os.path.dirname(file_path)
        os.makedirs(folder,exist_ok=True)
        with open(file_path,"wb") as f:
            np.save(f,data)
        logging.info("Array saved!")
    except Exception as e:
        raise CustomException(e,sys)

def save_pickle_file(file_path:str,pkl_file:object):
    try:
        logging.info("Entering folder to save the object...")
        folder = os.path.dirname(file_path)
        os.makedirs(folder,exist_ok=True)
        with open(file_path,"wb") as f:
            pickle.dump(pkl_file,f)
        logging.info("Pickle file saved successfully!")
    except Exception as e:
        raise CustomException(e,sys)


