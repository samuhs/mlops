"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.1
"""
import pandas as pd

from ml_pipeline.entities.prepare_dataframe import PrepareDataframe
from ml_pipeline.entities.logistic_model import LogisticModel

def process_dataframe(dataframe: pd.DataFrame):
    """Função responsavel por prepara o DataFrame para o projeto

    Args:
        dataframe (pd.DataFrame): Dataframe bruto do projeto

    Returns:
        _type_: _description_
    """
    prepare_dataframe = PrepareDataframe()

    logistic_dataframe = prepare_dataframe.process_dataframe_to_logistic(dataframe)
    return logistic_dataframe

def logistic_training(dataframe: pd.DataFrame):
    """Função Resposavel por treinar a regressão logistica do projeto

    Args:
        dataframe (pd.DataFrame): Dataframe ja processado a ser avaliado pelo projeto

    Returns:
        _type_: _description_
    """
    logistic = LogisticModel()

    logistic.train_logistic(dataframe, 'strategy')

    return True