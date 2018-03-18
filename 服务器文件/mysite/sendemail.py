# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
def sendemail(email,code):
    _user = "1260952721@qq.com"
    _pwd  = "inmqagfxkkxvihie"
    _to   = email
    mail_msg = """
    <p style="FONT-SIZE: 12pt" align="center">【甘-Django-Apache】请记住验证码：</p>
    <br/>
    <p style="FONT-SIZE: 10pt" align="center">欢迎注册！验证码:【<a style="color: red"><b>%s</b></a>】</p>
    <p style="FONT-SIZE: 10pt" align="center">请在30分钟内完成注册。如非本人操作，请忽略。</p>
    """%code
    msg = MIMEText(mail_msg,'html')
    msg["Subject"] = "From:www.gyhdtc.cn"
    msg["From"]    = "ET"
    msg["To"]      = _to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        return True
    except smtplib.SMTPException:
        return False