import json
import smtplib
from email.message import EmailMessage
from os import getenv

from chalice import Chalice

# variaveis
QUEUE_NAME = 'bhub-email'
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_USER = getenv('EMAIL_USER')
EMAIL_PASS = getenv('EMAIL_PASS')
EMAIL_PORT = int(getenv('EMAIL_PORT'))

# Chalice
app = Chalice(app_name=f'{QUEUE_NAME}-lambda')
app.debug = True


def send_mail(to_email, subject, message):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = ', '.join(to_email)
    msg.set_content(message)
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        app.log.debug('successfully sent the mail.')


@app.on_sqs_message(queue=f'{QUEUE_NAME}')
def handle_sqs_message(event):
    for item in event:
        config = json.loads(item.body)
        try:
            to_email = [config['order']['buyer_email']]
            send_mail(to_email, config['subject'], config['text'])
        except Exception:
            app.log.debug(
                f'Error sending Email with following config: {config}'
            )
