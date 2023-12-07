import smtplib
import ssl

from celery import Celery

app = Celery('sender', broker='pyamqp://guest@localhost/')


@app.task
def send_sms():
    from_email = "akbaralisalohiddinov808@gmail.com"
    password = "nimmxwxmyflugslo"
    message = "Hello Module 6"
    emails = [
        'akbaralisalohiddinov808@gmail.com',
        'lama666python@gmail.com'
    ]
    for email in emails:
        to_email = email
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
                server.login(from_email, password)
                server.sendmail(from_email, to_email, message)
                print("SMS sent to email successfully.")
        except Exception as e:
            print(e)
