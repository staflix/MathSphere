import smtplib
from email.mime.text import MIMEText


def send_email(recipient, subject, body):
    FROM = 'mathup.help@gmail.com'
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    msg = MIMEText(message, 'plain', 'utf-8')
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(FROM, 'fubt tijc dfgz zzlw')
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
    except Exception as e:
        print('Ошибка отправки!', e)


send_email("staflix@yandex.ru", 'Сброс пароля MathUp!', 'Приветик')

