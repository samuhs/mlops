from typing import Union

from fastapi import FastAPI, HTTPException
from mlflow.sklearn import load_model
from .dataframe import Dataframe

import mlflow as ml
import os

app = FastAPI()

os.environ["AWS_DEFAULT_REGION"] = "eu-west-3"
os.environ["AWS_REGION"] = "eu-west-3"
os.environ["AWS_ACCESS_KEY_ID"] = "admin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "adminadmin"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://<SEU_IP>:9020"
ml.set_tracking_uri("http://<SEU_IP>:5000")

@app.get("/")
def read_root():
    return 'Bem vindo ao classificador de cards da magalu :)'

@app.get("/card_id/{card_id}")
def card_classify(card_id: int):

    nome_registro_modelo = 'logistic_regression'
    model_uri = "models:/{nome_registro_modelo}/Staging".format(nome_registro_modelo=nome_registro_modelo)
    modelo = load_model(model_uri)

    dataframe = Dataframe('challenge_process.csv')
    result = dataframe.search_dataframe('id_card',str(card_id))

    if result.empty:
       raise HTTPException(status_code=404, detail="Item not found")

    result_card_name = result['name'].iloc[0]
    result_input_dataframe = result.drop(['Unnamed: 0','id_card','name'],axis= 1)

    result_predict = modelo.predict(result_input_dataframe)

    return {"result_predict": result_predict[0], "card_name": result_card_name}
