"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes.py read tech
...
...
"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)

if not arguments[0] in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    # leitura das notas
    for line in open(filepath):
        titulo, tag, texto = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Título: {titulo}")
            print(f"Texto: {texto}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    # criação da nota
    titulo = arguments[1] # TODO: Tratar exception
    text = [
        f"{titulo}",
        input("tag: ").strip(),
        input("text:\n").strip()
    ]
    # \t - tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")