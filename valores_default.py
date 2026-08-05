import time

def imprime_nome(nome, sobrenome="Sabugosa"):
    # escopo local {nome: .., sobrenome: ..}
    print(f"Seu nome é {nome} {sobrenome}")

imprime_nome("Bruno", "Rocha")
imprime_nome("Linus")

def conecta(host, timeout=10):
    print(f"Conectando com {host}")
    for i in range(1, timeout + 1):
        time.sleep(1)
        print("." * i)
    print("Erro ao conectar")

conecta("localhost")