from http import HTTPStatus
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(args):
    
    with open('emailTemplate.html', 'r') as file:
        html_content = file.read()

    name = args.get("name")
    #! SUBSTITUIR ANTES DA PRODUCAO
    verification_link = "https://google.com"

    key = os.getenv('API_KEY')
    user_to = args.get("to")


    # Inserir variaveis no html
    html_content = html_content.replace("{{name}}", name).replace("{{verification_link}}", verification_link)

    if not user_to:
        return {
            "statusCode" : HTTPStatus.BAD_REQUEST,
            "body" : "no receiver email provided"
        }
    if not name:
        return {
            "statusCode" : HTTPStatus.BAD_REQUEST,
            "body" : "no name provided"
            }

    sg = SendGridAPIClient(key)
    message = Mail(
        from_email = "melocardozo.video@gmail.com",
        to_emails = user_to,
        subject = name + ", Conclua seu cadastro verificando este email",
        html_content = html_content
        )
    response = sg.send(message)

    if response.status_code != 202:
        return {
            "statusCode" : response.status_code,
            "body" : "email failed to send"
        }
    return {
        "statusCode" : HTTPStatus.ACCEPTED,
        "body" : "success"
    }