from modelscope.hub.api import HubApi
from os import environ

__all__ = ["ModelScopeClient", "easy_modelscope"]

class ModelScopeClient:
    def __init__(self, MODELSCOPE_TOKEN: str = None):
        if not MODELSCOPE_TOKEN:
            self.MODELSCOPE_TOKEN = environ.get("MODELSCOPE_TOKEN")
        else:
            self.MODELSCOPE_TOKEN = MODELSCOPE_TOKEN
        self.api = HubApi()
        self.is_login = False
    
    def login(self):
        if self.MODELSCOPE_TOKEN:
            self.api.login(self.MODELSCOPE_TOKEN)
            self.is_login = True

    def upload_models(self, model_dir, repo_name):
        if not self.ModelScopeClient:
            raise Exception("Please enter MODELSCOPE_TOKEN")
        if not self.is_login:
            self.login()
        add_file = "configuration.json"
        # write {}
        # specify the local model directory, the directory must contain the configuration.json file
        with open(add_file, "w") as f:
            f.write("{}")

        self.api.push_model(
            # if the model library corresponding to model_id does not exist, it will be automatically created
            model_id=repo_name, 
            model_dir=model_dir 
        )
    
    def download(self, repo_name, save_dir, file_path=None):
        if self.MODELSCOPE_TOKEN:
            self.login()
        if not file_path:
            from modelscope.hub.snapshot_download import snapshot_download
            snapshot_download(model_id=repo_name, save_dir=save_dir)
        else:
            from modelscope.hub.file_download import model_file_download
            model_file_download(model_id=repo_name,file_path=file_path,save_dir=save_dir)

easy_modelscope = ModelScopeClient()