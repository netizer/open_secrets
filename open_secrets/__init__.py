from google.cloud import secretmanager
import yaml
import os

LOCAL_ENV_VAR_FILE_PATH = "env_vars.yaml"

def _default_project_id():
    google_run_value = os.environ.get("K_SERVICE")
    google_app_engine_value = os.environ.get("GOOGLE_CLOUD_PROJECT")
    return google_run_value or google_app_engine_value

def _default_is_prod():
    if _default_project_id():
        return True
    else:
        return False

def _default_prod_get(key):
    client = secretmanager.SecretManagerServiceClient()
    project_id = _default_project_id()
    version_id = "latest"
    name = f"projects/{project_id}/secrets/{key}/versions/{version_id}"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode('UTF-8')

def get(key):
    return OpenSecrets().get(key)

class OpenSecrets:
    def __init__(self, prod_get=_default_prod_get, is_prod=_default_is_prod):
        self.prod_get = prod_get
        self.is_prod = is_prod

    def get(self, key):
        if self.is_prod():
            return self.prod_get(key)
        else:
            return self.__local_get(key)

    def __local_get(self, key):
        result = None
        with open(LOCAL_ENV_VAR_FILE_PATH) as file:
            vars = yaml.load(file, Loader=yaml.BaseLoader)
            result = vars[key]
            if not result:
                raise Exception(f"Local environment variable: Put {key} in env_vars.yaml")
        return result
