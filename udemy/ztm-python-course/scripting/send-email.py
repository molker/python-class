import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # similar to os.path
# SMTP Simple Mail Transfer Protocol

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'First Last'
email['to'] = 'email@email.com'
email['subject'] = 'Congratulations! You\'ve Won!'

email.set_content(html.substitute({'name': 'Kevin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('user', 'pass')
    smtp.send_message(email)
