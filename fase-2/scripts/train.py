import argparse
import numpy as np
import xgboost as xgb
from loguru import logger
import os
import pandas as pd
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('--data_file', required=True, type=str, help='a csv file with train data')
parser.add_argument('--model_file', required=True, type=str, help='where the trained model will be stored')
parser.add_argument('--overwrite_model', default=False, action='store_true', help='if sets overwrites the model file if it exists')

args = parser.parse_args()

model_file = args.model_file
data_file  = args.data_file
overwrite = args.overwrite_model

if os.path.isfile(model_file):
    if overwrite:
        logger.info(f"overwriting existing model file {model_file}")
    else:
        logger.info(f"model file {model_file} exists. exitting. use --overwrite_model option")
        exit(-1)

logger.info("loading train data")
z = pd.read_csv(data_file).values
Xtr = z[:,:-1]
ytr = z[:,-1]

logger.info("fitting model")
gbm = xgb.XGBClassifier(max_depth=3, n_estimators=10, learning_rate=0.05, use_label_encoder=False)
gbm = gbm.fit(X_train, y_train)

logger.info(f"saving model to {model_file}")
with open(model_file, "wb") as f:
    pickle.dump(gbm, f)
