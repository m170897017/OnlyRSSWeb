##Only RSS Web 项目

一个 `RSS` 阅读器的 Web 版本，基于 `Python`、`Django` 和 `MySQL`。

![预览](http://tonghs-cdn-static.qiniudn.com/new_rss_style_20150213-1.png)

## 部署

有三种部署方式：

1. [下载 docker 镜像](#docker_image)
2. [使用 dockerfile 编译 docker 镜像](#dockerfile)
3. [手动部署](#manually)

<a name='docker_image'></a>
### 1. docker image

地址：[https://registry.hub.docker.com/u/tonghuashuai/rss-deploy/](https://registry.hub.docker.com/u/tonghuashuai/rss-deploy/)

``` shell
docker pull tonghuashuai/rss-deploy
```
<a name='dockerfile'></a>
### 2. dockerfile
dockerfile及相关文件：[https://github.com/tonghuashuai/OnlyRSSWeb/tree/master/dockerfile](https://github.com/tonghuashuai/OnlyRSSWeb/tree/master/dockerfile)

``` shell
cd DOCKERFILE DIR
docker build -t rss-demo .
```

<a name='manually'></a>
### 3. 手动部署

分 Web 端和后台脚本两部分。

#### 相关与依赖：
* django
* feedparser
* uwsgi
* nginx
* mysql


#### 后台脚本：

用于定时获取订阅内容，可配合任务计划工作。

    crontab -e

添加以下语句：

    */5 * * * * python /YOUR_RSS_DIR/misc/update_service.py

#### Web 端：

使用 `nginx` + `uWSGI` 部署，`ubuntu 12.10`, `debian 7.8`, `gentto` 测试可正常部署，其他发行版本未试。

**配置：**

1. 修改 `Django` 配置文件，配置数据库，以 `MySQL` 为例。
2. 执行安装脚本

    ./install.sh

脚本中会有如下动作：

    # mysql
    # 新建数据库 onlyrss 并同步数据表到 `MySQL`。
    CREATE USER 'rss'@'%' IDENTIFIED BY 'rstfsgbcedh';
    GRANT ALL PRIVILEGES ON *.* TO 'rss'@'%' IDENTIFIED BY 'rstfsgbcedh' WITH GRANT OPTION;
    CREATE DATABASE onlyrss DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
    
    # shell
    # 同步数据结构
    python manage.py syncdb

    # mysql
    # 新建用户。可执行以下 SQL 脚本添加用户。
    USE ONLYRSS;
    INSERT INTO OnlyRSS_user (username, password, name) VALUES ('username', 'password', 'name');

**启动**
    
    uwsgi -x misc/rss.xml
    nginx -s reload


**重启**

    uwsgi --reload misc/uwsgi.pid
    sudo nginx -s reload

    或者

    misc/restart.sh

    
**调试**

    python manage.py runserver 0.0.0.0:8080

    或者

    misc/dev.sh


**使用**

首次使用，使用用户名密码登录后可在设置中导入订阅列表或在首页输入订阅地址添加订阅。



## To do list

1. 密码加密
6. 订阅管理中可修改 url 和名称
7. 图标使用高清或 svg
8. 有可能加入分类
5. 有可能加入未读条数显示
6. setup.py
8. *删除动态效果*

## 已知问题

## License

Copyright (c) 2013-2015 tonghs.

This project is licensed under the terms of the MIT license.

See the [LICENSE.txt](LICENSE.txt) file for license rights and limitations.


