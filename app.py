from datetime import datetime # Fornece classes para manipulação de datas e horas
import csv                    # Implementa classes para ler e gravar dados tabulares em formato CSV
import os                     # Interagir com o sistema operaciona, executa comando no terminal


# Esse código lê o arquivo CSV, transforma cada linha em um dicionário e cria um grande dicionário clientes
with open('cadastro.csv', newline='', encoding="utf-8-sig") as FileCSV:
    leitor_arquivo = csv.DictReader(FileCSV, delimiter=";")
    clientes = {}
    for linha in leitor_arquivo:
        chave = linha["nome"]
        clientes[chave] = linha
        print(clientes)