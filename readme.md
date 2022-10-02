## 一、pipenv的快速入门
#### 快速上手
###### 使用pipenv的操作步骤
1. cmd中输入命令 `pip install pipenv` 安装`pipenv`
2. cmd切换路径到需要建立虚拟环境的项目目录下
3. 初始化特定版本的环境pipenv --python 3.6 (可选，如果不初始，则跟随系统)
4. 输入命令 pipenv install 开始安装虚拟环境
5. 安装完毕后输入命令 pipenv shell 进入虚拟环境
6. pipenv install xxx 安装相关依赖包
7. pipenv graph 查看目前按照的依赖包

#### 常用命令一览
1 pipenv --where 列出本地工程路径

2 pipenv --venv 列出虚拟环境路径

3 pipenv --py 列出虚拟环境的Python可执行文件

4 pipenv install 安装包（创建虚拟环境）

5 pipenv install moduel --dev 在开发环境安装包

6 pipenv graph 查看包依赖

7 pipenv lock 生成lockfile

8 pipenv install --dev 安装所有开发环境包

9 pipenv uninstall --all 卸载所有包

10 pipenv --rm 删除虚拟环境

11 pipenv run python xxx.py 虚拟环境运行python

12 pipenv --rm 删除虚拟环境

13 pipenv uninstall 包名 删除部分包