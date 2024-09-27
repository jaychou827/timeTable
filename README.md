# 微信课程表

#### 简介

###### 这是一款在线的微信课程表提醒系统

###### 基于wcferry库开发

###### 会根据users.csv和table.csv俩个文件进行主动和被动的上课提醒



#### 目录结构

###### main.py			主程序

> 主要分为俩个功能部分，由俩个线程多线程完成主动和被动的上课提醒功能
>
> ​		主动：根据user.csv数据，定时定点定用户发送上课提醒信息
>
> ​		被动：监测微信私聊信息，当接受到table.csv中用户的私聊信息，并匹配关键					字“课表”后，发送课表图片

###### Utils.py			自建工具类

> 构造了三个用于其他程序的辅助函数
>
> * def read_csv_to_dict(file_path)		从csv中读取数据
>
> * def get_welcome_msg(name)		构造欢迎语句
>  
> * def get_good_bye_msg(name)		构造再见语句

###### bye.py				结束程序

###### test.py				测试程序（获取指定用户wxid）

###### logs					wcferry库运行日志

###### user.csv			课程信息

###### tables.csv			课程表图片与用户配对信息



## 使用方法

1. 安装依赖库：`pip install wcferry`
2. 将user.csv和tables.csv文件放在同一目录下。
3. 运行main.py启动程序。
4. 使用test.py获取指定用户的wxid。
5. 在微信中向指定的wxid发送关键字“课表”，即可收到对应的课程表图片。

