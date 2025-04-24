import os,sys
import pandas as pd
import numpy as np


TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
FILE_NAME: str = "phisingData.csv"
ARTIFACT_DIR: str = "Artifacts"


TRAIN_DATA: str = "train.csv"
TEST_DATA: str = "test.csv"

DATA_INGESTION_DATABASE: str = "SURYA"
DATA_INGESTION_COLLECTION: str = "NetworkData"
DATA_INGESTION_DIR: str = "data_ingestion"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_TEST_SIZE: float = 0.2


