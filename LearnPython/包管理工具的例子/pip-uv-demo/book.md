


# 原始人阶段

## 打印当前虚拟环境的依赖，并输出到文件 requirements.txt 中
pip freeze > requirements.txt
PS: pip freeze会打印全部的依赖，包括间接依赖

## 别人拿到项目时，这样使用
pip install -r requirements.txt



# 早期人类阶段

## 创建虚拟环境
python -m venv .venv

## 激活虚拟环境
source .venv/bin/activate

## 创建并编辑  pyproject.toml 文件

## 通用依赖配置文件  pyproject.toml
pip install . # 拿到新项目时安装依赖，打包所有为安装包并安装
pip install -e . # 开发内容不打包 【推荐使用】


# 现代人阶段

## 创建 main.py 和基础的 pyproject.toml 文件

pyproject.toml
```toml
[project]
name = "proj"
version = "0.1.0"
```

## 安装uv
brew install uv

## 查看安装的 uv 版本
v -V   # uv 0.9.26 (Homebrew 2026-01-15)

## 安装依赖  自动创建虚拟环境并修改 pyproject.toml 文件中依赖
uv add flask   


pyproject.toml 配置文件自动增加内容：
```text

dependencies = [
    "flask>=3.1.2",
]

```


```text
Using CPython 3.12.9 interpreter at: /Users/tokumi/miniconda3/bin/python3
Creating virtual environment at: .venv
warning: No `requires-python` value found in the workspace. Defaulting to `>=3.12`.
Resolved 9 packages in 1.07s
Prepared 7 packages in 496ms
Installed 7 packages in 7ms
 + blinker==1.9.0
 + click==8.3.1
 + flask==3.1.2
 + itsdangerous==2.2.0
 + jinja2==3.1.6
 + markupsafe==3.0.3
 + werkzeug==3.1.5
```