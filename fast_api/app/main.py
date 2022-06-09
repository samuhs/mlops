from typing import Union

from fastapi import FastAPI
from mlflow.sklearn import load_model

import mlflow as ml
import os

app = FastAPI()


@app.get("/")
def read_root():
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-3"
    os.environ["AWS_REGION"] = "eu-west-3"
    os.environ["AWS_ACCESS_KEY_ID"] = "admin"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "adminadmin"
    os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://192.168.0.26:9020"
    ml.set_tracking_uri("http://192.168.0.26:5000")
    print('Carregando modelo')

    # Load model as a PyFuncModel.
    # loaded_model = ml.pyfunc.load_model(logged_model)
    nome_registro_modelo = 'logistic_regression'
    model_uri = "models:/{nome_registro_modelo}/Staging".format(nome_registro_modelo=nome_registro_modelo)
    modelo = load_model(model_uri)

    print(modelo)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}