# StudentCourses

🌍 软件工程课程设计大作业 第28组

基于`python3.8`和`Django3.0`的课表管理系统。   

## 主要功能：
- 实现学生对自己课表的查询

- 学生对课表的管理

- 学生对于开课信息的查询

- 查询教师课表

- 查询空闲教室与租借教室

- 加入微博热搜娱乐功能

- 学习笔记记录功能

  **功能详情请查看  [CONTENT_README](https://github.com/qingfusheng/StudentCourse/blob/master/content/README.md)**
  *已部署项目网址 [青青子衿的课表网站](http://162.14.80.178:8000/)*


## 安装
数据操作使用django原装数据库sqlite，不需要额外下载其他如MySQL等，数据文件保存本地

使用pip安装： `pip install -Ur requirements.txt`

如果你没有pip，使用如下方式安装：
- OS X / Linux 电脑，终端下执行: 

    ```
    curl http://peak.telecommunity.com/dist/ez_setup.py | python
    curl https://bootstrap.pypa.io/get-pip.py | python
    ```

- Windows电脑：

    下载 http://peak.telecommunity.com/dist/ez_setup.py 和 https://raw.github.com/pypa/pip/master/contrib/get-pip.py 这两个文件，双击运行。 


## 运行

### 首先创建应用
```bash
python manage.py startapp studentCourses
```
### 创建数据库
```bash
python manage.py makemigratioin studentCourses
python manage.py migrate
```
然后终端下执行:
```bash
./manage.py makemigrations
./manage.py migrate
```

**注意：** 在使用 `./manage.py` 之前需要确定你系统中的 `python` 命令是指向 `python 3.6` 及以上版本的。如果不是如此，请使用以下两种方式中的一种：

- 修改 `manage.py` 第一行 `#!/usr/bin/env python` 为 `#!/usr/bin/env python3`

- ```bash
  apt-get install python-is-python3
  ```

- 直接使用 `python3 manage.py makemigrations`

### 创建超级用户

 终端下执行:
```bash
python manage.py createsuperuser
```
### 开始运行：
执行： `python manage.py runserver`


浏览器打开: http://127.0.0.1:8000/  就可以看到效果了。  

## 服务器部署

本地安装部署请参考 [DjangoBlog部署教程](https://www.lylinux.net/article/2019/8/5/58.html)
有详细的部署介绍.    

## 问题相关

有任何问题欢迎提Issue,或者将问题描述发送至我邮箱 `2564526674@qq.com`.我会尽快解答.推荐提交Issue方式.  
