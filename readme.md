## 一、为什么标准REST不适合内部开发

标准rest适合开放型api，比如豆瓣、github。

1. 标准的rest开发要求，资源只有CRUD，但是我们内部开发有很多复杂的业务逻辑，比如有分页、只查询部分数据、组合获取某些数据，这些场景，标准rest都无法实现。
2. 标准rest接口粒度比较粗，前端开发不方便。比如标准rest服务器端并不处理字段，会把所有的属性和数据放回给前端，由前端处理。
3. 标准rest会造成HTTP请求的数量大幅增加。当业务比较复杂，涉及多种资源，那就要调用多次http请求，比如需要组合book和user，就需要查询两次。

## 二、pipenv的快速入门

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