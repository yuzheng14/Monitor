@[TOC]
# 项目简介
本项目用于爬取山东大学威海校区教务处网站工作通知并发送邮件进行通知
## 使用方法
1.安装python环境（开发环境为3.8.2）  
2.配置`config.json`[点此跳转配置详解](#json)  
2.Windows下双击run.bat  
2.1.Linux下打开run.sh  
2.2.(穷逼没苹果不知道苹果用啥启动，就bash `python main.py`叭)  
## 文件详解
>|文件名|作用|
>|---|:----:|
>|run.bat|Windows下运行程序批处理文件|
>|run.sh|Linux下运行程序批处理文件|
>|main.py|程序入口|
>|crawler.py|爬虫本体|
>|send_email.py|发送邮件方法|
>|util.py|生成config.py工具类|
>|log.py|输出日志|
>|config.json|配置文件|
>|log.out|日志文件|
>|test.py|测试文件（可忽略）|
## `config.json`文件的配置<span id="json"></span>  
```json
{
    "host": "smtp.qq.com",              设置服务器
    "user": "*********",                用户
    "password": "****************",     密码（授权码）
    "sender": "*********@qq.com",       发信者
    "receivers": [                      收信者（多个收信者用半角','隔开）
        "*********@qq.com"
    ],
    "interval": 3600                    监控时间间隔（建议1h起步，单位为秒）
}
```
