import os

from random import random, randint
from mlflow import log_metric, log_param, log_artifacts
from mlflow.sklearn import load_model
import mlflow as ml

os.environ["AWS_DEFAULT_REGION"] = "eu-west-3"
os.environ["AWS_REGION"] = "eu-west-3"
os.environ["AWS_ACCESS_KEY_ID"] = "admin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "adminadmin"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9020"

ml.set_tracking_uri("http://localhost:5000")
# ml.set_experiment("my-experiment")

if __name__ == "__main__":
    # Log a parameter (key-value pair)
    # log_param("param1", randint(0, 100))

    # # Log a metric; metrics can be updated throughout the run
    # log_metric("foo", random())
    # log_metric("foo", random() + 1)
    # log_metric("foo", random() + 2)

    # # Log an artifact (output file)
    # if not os.path.exists("outputs"):
    #     os.makedirs("outputs")
    # with open("outputs/test.txt", "w") as f:
    #     f.write("hello world!")
    # log_artifacts("outputs")
    # logged_model = 'runs:/8706bf41d0704fa19cb72a346c2e9bd7/modelo'

    # Load model as a PyFuncModel.
    # loaded_model = ml.pyfunc.load_model(logged_model)
    nome_registro_modelo = 'logistic_regression'
    model_uri = "models:/{nome_registro_modelo}/Staging".format(nome_registro_modelo=nome_registro_modelo)
    modelo = load_model(model_uri)
    print(modelo)
