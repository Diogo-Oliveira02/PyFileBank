from datetime import datetime # Fornece classes para manipulação de datas e horas
import csv                    # Implementa classes para ler e gravar dados tabulares em formato CSV
import os                     # Interagir com o sistema operaciona, executa comando no terminal


# Lê o arquivo CSV, transforma cada linha em um dicionário e cria um grande dicionário clientes
try:
    with open('cadastro.csv', newline='', encoding="utf-8-sig") as FileCSV:
        leitor_arquivo = csv.DictReader(FileCSV, delimiter=";")
        clientes = {}
        for linha in leitor_arquivo:
            chave = linha["nome"]
            clientes[chave] = linha
except FileNotFoundError:
    print("Arquvo csv não encontrado!")

# Salva todos os clientes no arquivo CSV, sobrescrevendo os dados antigos
def alterar_saldo_csv():
    with open('cadastro.csv', 'w', newline='', encoding='utf-8-sig') as FileCSV:
        escrever_arquivo = csv.DictWriter(FileCSV, fieldnames=clientes[chave],delimiter=";")
        escrever_arquivo.writeheader()
        for cliente in clientes.values():
            escrever_arquivo.writerow(cliente)
            
def exibir_menu():
    print("""
        ========== Banco Digital ==========
        [1] - Deposito dinheiro
        [2] - Sacar dinheiro
        [3] - Trasferir dinheiro para outra conta
        [4] - Extrato de conta
        [5] - Consulta Saldo
        [0] - Sair
    """)