import sys
import os
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]

if not arguments:
    print("Informe o nome do arquivo de e-mails.")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt

clientes = []

with smtplib.SMTP(host="localhost", port=8025) as server:

    for line in open(filepath):
        nome, email = line.split(",")
        text = (
            open(templatepath).read() % {
                "nome": nome,
                "produto": "caneta",
                "texto": "Escrever muito bem",
                "link": "https://canetaslegais.com",
                "quantidade": 1,
                "preco": 50.5
            }
        )

        from_ = "morg@gmail.com"
        to = ", ".join([email])
        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())

        