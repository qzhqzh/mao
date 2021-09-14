""" 定时任务页面 """
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from notice.models import Notice


def my_scheduled_job():
    for x in Notice.objects.all():
        print(f'{x.name}[{x.platform}] => {x.remind_at}')


def email_remind():
    """ 邮件提示 """

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"
    mail_user = "28630707@qq.com"
    mail_pass = "ihmqewpnpmoobjai"  # 口令/授权码

    sender = '28630707@qq.com'
    receivers = ['28630707@qq.com']

    message = MIMEText('邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("测试", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = '邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP_SSL()
    smtpObj.connect(mail_host, 465)  # 465为SMTP加密端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
