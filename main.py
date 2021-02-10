from log import log
from crawler import Crawler
from send_email import send_email
import time
import json
crawler=Crawler()
last_first_title=''

def examine(titles):
    global last_first_title
    if len(last_first_title) != 0:
        for i in range(len(titles)):
            if titles[i] == last_first_title:
                last_first_title=titles[0]
                return i
    else:
        last_first_title=titles[0]
        return -1
    return -1
log('[INFO]:山东大学（威海）教务处工作通知监控系统已启动')
while(True):
    # 返回19个通知的title
    crawler.crawl()
    titles=crawler.crawl_titles()
    order=examine(titles)
    if order != 0 and order != -1:
        content=crawler.crawl_content(order)
        send_email(content,titles[:order])
        log(F'[INFO]:教务处工作通知已更新{order}条通知，并已发送邮件')
        
    elif order==-1:
        log('[INFO]:初始化系统')
    else:
        log('[INFO]:教务处工作通知未更新通知')
        
    with open('config.json','r') as f:
        data=json.load(f)
    
    time.sleep(data['interval'])