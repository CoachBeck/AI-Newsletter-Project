import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
