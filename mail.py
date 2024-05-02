import smtplib


def send_email(recipient, subject, body):
    FROM = 'mathup.help@gmail.com'
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(FROM, 'fubt tijc dfgz zzlw')
        server.sendmail(FROM, TO, message)
        server.close()
    except Exception:
        print('Ошибка отправки!')


send_email("почта пользователя", 'Сброс пароля MathUp!', 'текст сброса пароля')

