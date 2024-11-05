# shiertier_modelscope

[English](https://github.com/shiertier-utils/shiertier_modelscope/blob/main/README.md) | 中文

## 简介

`shiertier_modelscope` 是一个用于与 ModelScope 平台交互的 Python 客户端。它提供了一个简单的接口，用于下载和上传模型，并支持使用环境变量进行自动登录。该库旨在简化在 ModelScope 上管理模型的过程。

## 安装

您可以通过 `pip` 安装 `shiertier_modelscope`：

```bash
pip install git+https://github.com/shiertier/shiertier_modelscope.git
```

请注意，该项目仍在开发中。

## 使用方法

### 下载模型

您可以使用 `download` 方法从 ModelScope 下载模型。该方法需要仓库名称和保存模型文件的目录。您还可以使用 `file_path` 参数指定要下载的特定文件。从公共仓库下载模型不需要令牌。

```python
from shiertier_modelscope import easy_modelscope

# 下载整个仓库
easy_modelscope.download(repo_name='my_public_model_repo', save_dir='path/to/save_directory')

# 从仓库中下载特定文件
easy_modelscope.download(repo_name='my_public_model_repo', save_dir='path/to/save_directory', file_path='path/to/file_in_repo')

# 从私有仓库下载（需要令牌）
client = ModelScopeClient(MODELSCOPE_TOKEN='your_token_here')
client.download(repo_name='my_private_model_repo', save_dir='path/to/save_directory')
```

### 上传模型

您可以使用 `upload_models` 方法将模型上传到 ModelScope。该方法需要包含模型文件的本地目录和仓库名称。请注意，上传模型需要有效的令牌。

```python
from shiertier_modelscope import ModelScopeClient

# 使用令牌初始化
client = ModelScopeClient(MODELSCOPE_TOKEN='your_token_here')

# 上传模型
client.upload_models(model_dir='path/to/model_directory', repo_name='my_model_repo')
```

### 初始化

要使用 `ModelScopeClient`，您需要使用您的 ModelScope 令牌进行初始化。如果在初始化时未提供令牌，它将尝试从 `MODELSCOPE_TOKEN` 环境变量中检索。

```python
from shiertier_modelscope import ModelScopeClient, easy_modelscope

# 使用令牌初始化
client = ModelScopeClient(MODELSCOPE_TOKEN='your_token_here')

# 或者使用 easy_modelscope 快捷方式
# easy_modelscope
```

### 环境变量

- `MODELSCOPE_TOKEN`: 用于与 ModelScope 平台进行身份验证的令牌。如果在初始化时未提供，客户端将尝试从该环境变量中检索。

## 依赖

- `modelscope`

## 许可证

本项目基于 MIT 许可证发布。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。