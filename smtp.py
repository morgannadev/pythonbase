"""Exemplos de envio de e-mail"""

import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "morg@gmail.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """
Este é o meu e-mail enviado pelo Python
<b>Olá mundo</b>
"""

# para rodar um server python -m smtpd -c DebuggingServer -n localhost:8025

message = f"""
From: {FROM}
To: {TO}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))