import smtplib
from email.mime.text import MIMEText
from email.header import Header
from data.config import mail_password


def send_email(recipient, subject, body):
    msg = MIMEText(body, 'plain', 'windows-1251')
    msg['Subject'] = Header(subject, 'windows-1251')
    msg['From'] = 'mathup.help@gmail.com'
    msg['To'] = recipient
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login('mathup.help@gmail.com', mail_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.close()
    except Exception as e:
        print('Ошибка отправки!', e)
