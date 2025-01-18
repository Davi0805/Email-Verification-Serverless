import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

with open('Sat Jan 18 2025-V1 email.html', 'r') as file:
    html_content = file.read()

name = "Davi"
verification_link = "https://google.com"

# Inserir variaveis no html
html_content = html_content.replace("{{name}}", name).replace("{{verification_link}}", verification_link)

message = Mail(
    from_email='melocardozo.video@gmail.com',
    to_emails='dddpaypal@gmail.com',
    subject='Verificacao de email',
    html_content=html_content)

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))