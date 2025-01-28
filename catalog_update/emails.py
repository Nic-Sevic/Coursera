#!/usr/bin/env python3
from email.message import EmailMessage
import smtplib


def generate_email(from_email, to_email, subject_line, email_body, report_path=None):
    # Generate the email
    message = EmailMessage()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject_line
    message.set_content(email_body)

    # Attach the file if report_path is provided
    if report_path:
        with open(report_path, "rb") as attachment:
            attachment_data = attachment.read()
            message.add_attachment(attachment_data, maintype="application", subtype="octet-stream", filename=report_path)

    return message


def send_email(message):
    # Send the email
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
