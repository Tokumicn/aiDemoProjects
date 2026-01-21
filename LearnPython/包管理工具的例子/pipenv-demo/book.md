


## 进入shell并创建虚拟环境
pipenv shell # 创建虚拟环境并创建文件Pipfile

 
## 安装生产依赖
pipenv install flask

## 运行
pipenv run python demo.py


## 安装开发依赖
pipenv install pytest --dev





## 接受新项目时：
pipenv install # 运行依赖的安装
pipenv install --dev # 运行和开发需要的依赖都安装



## 查看依赖树
pipenv graph


## 删除虚拟环境
exit # 退出虚拟环境
pipenv --rm # 删除虚拟环境