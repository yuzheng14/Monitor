import email
from log import log
from crawler import Crawler
from email import message
from email.mime import text
import smtplib
from urllib import request
from lxml import etree
from email.mime.text import MIMEText
import json


def send_email(content, titles):
    with open('config.json', 'r') as f:
        data = json.load(f)
    mail_host = data['host']
    mail_user = data['user']
    mail_password = data['password']
    sender = data['sender']
    receivers = data['receivers']
    email = []
    for i in range(len(content)):
        message = MIMEText(content[i], 'html', 'utf-8')
        message['From'] = sender
        message['To'] = ','.join(receivers)
        message['Subject'] = titles[i]
        email.append(message)
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_password)
        for message in email:
            smtpObj.sendmail(sender, receivers, message.as_string())
            title = message['Subject']
            log(f'[INFO]:推送通知“{title}”成功')
        smtpObj.quit()
    except smtplib.SMTPException as e:
        log(f'[error]:{e}')


if __name__ == '__main__':
    crawler = Crawler()
    crawler.crawl()
    titles = crawler.crawl_titles()
    content = crawler.crawl_content(1)
    send_email(content, titles)
