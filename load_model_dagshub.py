import configparser
import dagshub
import mlflow

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

dagshub.auth.add_app_token(config_ini["dagshub"]["token"], host=None)
dagshub.init(repo_owner=config_ini["dagshub"]["user_name"], repo_name=config_ini["dagshub"]["project_name"], mlflow=True)

client = mlflow.MlflowClient()
version = client.get_latest_versions(name=config_ini["dagshub"]["experiment_name"])[0].version
model_uri = f'models:/{config_ini["dagshub"]["experiment_name"]}/{version}'

model = mlflow.sklearn.load_model(model_uri)
