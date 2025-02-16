import configparser
import dagshub
import mlflow
import json
import numpy as np
from mlflow.tracing.destination import MlflowExperiment

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

dagshub.auth.add_app_token(config_ini["dagshub"]["token"], host=None)
dagshub.init(repo_owner=config_ini["dagshub"]["user_name"], repo_name=config_ini["dagshub"]["project_name"], mlflow=True)

mlflow.set_tracking_uri(f"https://dagshub.com/{config_ini['dagshub']['user_name']}/{config_ini['dagshub']['project_name']}.mlflow")

client = mlflow.MlflowClient()
version = client.get_latest_versions(name=config_ini["dagshub"]["experiment_name"])[0].version
model_uri = f'models:/{config_ini["dagshub"]["experiment_name"]}/{version}'

model = mlflow.sklearn.load_model(model_uri)


# Ensure traces are logged to the same experiment
mlflow.tracing.set_destination(MlflowExperiment(experiment_id=mlflow.get_experiment_by_name("MLflow Quickstart").experiment_id))


@mlflow.trace
def predict(model, input_data):
    return model.predict(input_data)

print(predict(model, np.array([[5.1, 3.5, 1.4, 0.2]])))