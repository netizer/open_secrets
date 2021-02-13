from google.cloud import secretmanager
import yaml
import os

PROJECT_ID_ENV_KEY = "GOOGLE_CLOUD_PROJECT"
LOCAL_ENV_VAR_FILE_PATH = "env_vars.yaml"

def env_var(key):
    if key in os.environ:
        return os.environ[key]
    else:
        raise Exception(f"Environment variable '{key}' should be set in the system.")

def has_env_var(key):
    if key in os.environ:
        return True
    else:
        return False

def get_from_secret_manager(key):
    client = secretmanager.SecretManagerServiceClient()
    project_id = env_var(PROJECT_ID_ENV_KEY)
    version_id = "latest"
    name = f"projects/{project_id}/secrets/{key}/versions/{version_id}"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode('UTF-8')

def get_from_local_file(key):
    result = None
    with open(LOCAL_ENV_VAR_FILE_PATH) as file:
        vars = yaml.load(file, Loader=yaml.BaseLoader)
        result = vars[key]
        if not result:
            raise Exception(f"Local environment variable: Put {key} in env_vars.yaml")
    return result

def get(key):
    """
    Gets environment variables from Google Cloud Secret Manager
    if
    """
    if has_env_var(PROJECT_ID_ENV_KEY):
        return get_from_secret_manager(key)
    else:
        return get_from_local_file(key)
