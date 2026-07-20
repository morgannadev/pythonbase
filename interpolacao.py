import sys
import os

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
for line in open(filepath):
    nome, email = line.split(",")

    # TODO: Substituir por envio de e-mail
    print(f"Enviando e-mail para: {email}")
    print()
    print(
        open(templatepath).read() % {
            "nome": nome,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5
        }
    )
    print("-" * 50)