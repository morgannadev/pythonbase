Problema: Ir a padaria e comprar pão: Premissa: Padaria da Esquina abre fds: até 12h, semana até 19h, feriado (exceto Natal) não abre.

A padaria está aberta?
Se é feriado e NÃO é natal: não
Senão, Se é sábado OU domingo E antes do meio dia: sim
Senão, se é dia de semana E antes das 19h: sim
senão: não
Se padaria está aberta E:
Se está chovendo: Pegar guarda-chuvas
Se está chovendo E calor: Pegar guarda-chuvas e garrafa de agua
Se está chovendo E frio OU nevando: pegar guarda chuva, blusa e botas
Ir até a padaria:
Se tem pao integral E baguete: Pedir 6 de cada
Senão, se tem apenas pao integral OU baguete: Pedir 12
Senão: Pedir 6 de qualquer pão
Senão
Ficar em casa em comer bolachas

# PSEUDOCÓDIGO

import pegar, ir, pedir, tem, comer, ficar

# Premissas
today = "Segunda"
hora_atual = 15
natal = False
chovendo = True
frio = False
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriados = ["Quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12,
}

# Algoritmo

# A padaria está aberta?
if today in feriados and not natal:
    padaria_aberta = False
elif today not in semana and hora_atual < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora_atual < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and (frio or nevando):
        pegar("guarda chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda chuva")
        pegar("agua")
    elif chovendo:
        pegar("guarda chuva")
    ir("padaria")

    if tem("pao integral") and tem("baguete"):
        pedir(6, "pao integral")
        pedir(6 "baguete")
    elif tem("pao integral") or tem("baguete"):
        pedir(12, "pao integral ou baguete")
    else:
        pedir(6, "qualquer pao")
else:
    ficar("casa")
    comer("bolachas")