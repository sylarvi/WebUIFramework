# -*-coding:utf-8 -*-
"""
Created on: 2020-06-23
@author: lixiao
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:
    def __init__(self):
        self.poster = '306280101@qq.com' # 发件人
        self.password = 'rulajsdlajd' # QQ邮箱第三方登录的授权码
        self.msg_to = '156953630@qq.com' # 收件人
        self.subject = 'Web_UI自动化测试报告' # 邮件标题
        self.content = '已完成所有case执行，测试结果详见附件' # 邮件内容

    def send_email(self, file):
        atta_path = 'C:\\Users\\Administrator\\PycharmProjects\\HybridDrive-Framework\\TestReport\\' + file
        message = MIMEMultipart()
        message['Subject'] = self.subject
        message['From'] = self.poster
        message['To'] = self.msg_to
        message.attach(MIMEText(self.content, 'html', 'utf-8'))
        att = MIMEText(open(atta_path, 'rb').read(), 'base64', 'utf8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="%s"' % file
        message.attach(att)

        s = smtplib.SMTP_SSL("smtp.qq.com", 465) # 创建邮箱服务
        s.login(self.poster, self.password) # 登录邮箱
        s.sendmail(self.poster, self.msg_to, message.as_string()) # 发送邮件
        s.quit() # 关闭邮箱服务


if __name__ == '__main__':
    email = SendEmail()
    email.send_email('2020-09-03-15_40_55HTMLtemplate.html')
