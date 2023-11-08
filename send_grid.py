import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(recipient_email, subject, content):
    message = Mail(
        from_email="your_email@example.com",
        to_emails=recipient_email,
        subject=subject,
        html_content=content
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f"Email sent. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Email could not be sent. Error: {str(e)}")
