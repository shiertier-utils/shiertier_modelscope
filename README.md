# shiertier_modelscope

English | [中文](https://github.com/shiertier-utils/shiertier_modelscope/blob/main/README_zh.md)

## Introduction

`shiertier_modelscope` is a Python client for interacting with the ModelScope platform. It provides a simple interface for downloading and uploading models, with support for automatic login using environment variables. This library is designed to streamline the process of managing models on ModelScope.

## Installation

You can install `shiertier_modelscope` via `pip`:

```bash
pip install git+https://github.com/shiertier/shiertier_modelscope.git
```

Please note that this project is still under development.

## Usage

### Downloading Models

You can download models from ModelScope using the `download` method. This method requires the repository name and the directory where the model files should be saved. You can also specify a specific file to download using the `file_path` parameter. Downloading models from public repositories does not require a token.

```python
from shiertier_modelscope import easy_modelscope

# Download the entire repository
easy_modelscope.download(repo_name='my_public_model_repo', save_dir='path/to/save_directory')

# Download a specific file from the repository
easy_modelscope.download(repo_name='my_public_model_repo', save_dir='path/to/save_directory', file_path='path/to/file_in_repo')

# Download from a private repository (requires token)
client = ModelScopeClient(MODELSCOPE_TOKEN='your_token_here')
client.download(repo_name='my_private_model_repo', save_dir='path/to/save_directory')
```

### Uploading Models

You can upload models to ModelScope using the `upload_models` method. This method requires the local directory containing the model files and the repository name. Note that uploading models requires a valid token.

```python
from shiertier_modelscope import ModelScopeClient

# Initialize with a token
client = ModelScopeClient(MODELSCOPE_TOKEN='your_token_here')

# Upload models
client.upload_models(model_dir='path/to/model_directory', repo_name='my_model_repo')
```

### Initialization

To use the `ModelScopeClient`, you need to initialize it with your ModelScope token. If the token is not provided during initialization, it will attempt to retrieve it from the `MODELSCOPE_TOKEN` environment variable.

```python
from shiertier_modelscope import ModelScopeClient, easy_modelscope

# Initialize with a token
client = ModelScopeClient(MODELSCOPE_TOKEN='your_token_here')

# Or use the easy_modelscope shortcut
# easy_modelscope
```

### Environment Variables

- `MODELSCOPE_TOKEN`: The token used for authentication with the ModelScope platform. If not provided during initialization, the client will attempt to retrieve it from this environment variable.

## Dependencies

- `modelscope`

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.