"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.1
"""
import pandas as pd

from ml_pipeline.entities.prepare_dataframe import PrepareDataframe
from ml_pipeline.entities.logistic_model import LogisticModel

def process_dataframe(dataframe: pd.DataFrame):
    prepare_dataframe = PrepareDataframe()

    logistic_dataframe = prepare_dataframe.process_dataframe_to_logistic(dataframe)
    return logistic_dataframe

def logistic_training(dataframe: pd.DataFrame):
    logistic = LogisticModel()

    logistic.train_logistic(dataframe, 'strategy')

    return True