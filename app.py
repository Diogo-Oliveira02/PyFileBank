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
    print("Arquvo .csv não encontrado!")

# Salva todos os clientes no arquivo CSV, sobrescrevendo os dados antigos
def alterar_saldo_csv():
    with open('cadastro.csv', 'w', newline='', encoding='utf-8-sig') as FileCSV:
        escrever_arquivo = csv.DictWriter(FileCSV, fieldnames=clientes[chave],delimiter=";")
        escrever_arquivo.writeheader()
        for cliente in clientes.values():
            escrever_arquivo.writerow(cliente)

# Função que envia as operação feito pelo usuario para o arquivo TXT 
def enviar_para_extrato(nome1, operacao, valor, nome2):
    data_hora = datetime.now().strftime('[%d/%m/%Y][%H:%M]')
    try:
        with open ('extrato.txt', 'a', encoding="utf-8-sig") as ExtractFile:
            if (operacao == "depositou") or (operacao == "sacou"):
                ExtractFile.write(f"{data_hora};{nome1};{operacao};{str(valor)}")
            else:
                ExtractFile.write(f"{data_hora};{nome1};{operacao};{str(valor)};{nome2}")
    except FileNotFoundError:
        print("Arquvo .txt não encontrado!")
        
def consulta_saldo(id):
    if id not in clientes:
        print("\nCliente não encontrado!\n")
    else:
        print(f"""
            Nome:  {clientes[id]["nome"]}
            Saldo: {clientes[id]["saldo_inicial"]}
        """)

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

def depositar_valor(id_cliente,valor_depoisito):
    if not id_cliente in clientes:
        print("\nCliente não encontrado!\n") 
    elif (valor_depoisito <= 0):
        print("\nValor deve ser maior que zero!\n")
    else:
        if float(clientes[id_cliente]["saldo_inicial"]) < 10:
            print("Saldo deve ser maior que R$10,00")
        else: 
            clientes[id_cliente]["saldo_inicial"] = float(clientes[id_cliente]["saldo_inicial"]) + valor_depoisito
            enviar_para_extrato(id_cliente,"deposito",valor_depoisito,None)
            alterar_saldo_csv()
            consulta_saldo(id_cliente)
def sacar_valor(id_cliente,valor_sacar):
    if not id_cliente in clientes:
        print("\nCliente não encontrado!\n")
    elif valor_sacar <= 0:
        print("\nValor deve ser maior que zero!\n")
    else:
        if float(clientes[id_cliente]["saldo_inicial"]) < 10:
            print("Saldo deve ser maior que R$10,00")
        else:
            clientes[id_cliente]["saldo_inicial"] = float(clientes[id_cliente]["saldo_inicial"]) + valor_sacar
            enviar_para_extrato(id_cliente,"saque",valor_sacar,None)
            alterar_saldo_csv()
            consulta_saldo(id_cliente)
def trasferir_valor(id_cliente_pagador, id_cliente_recebedor,valor_transferencia):
    if id_cliente_pagador not in clientes:
            print("\nCliente pagador não encontrado!\n")
    elif id_cliente_recebedor not in clientes:
            print("\nCliente recebedor não encontrado!\n")
    else:
        if valor <= 0:
            print("\nValor deve ser maior que zero!\n")
        else:
            if float(clientes[id_cliente_pagador]["saldo_inicial"]) < 10:
                print("Saldo deve ser maior que R$10,00")
            else:
                clientes[id_cliente_pagador]["saldo_inicial"] = float(clientes[id_cliente_pagador]["saldo_inicial"]) - valor
                clientes[id_cliente_recebedor]["saldo_inicial"] = float(clientes[id_cliente_recebedor]["saldo_inicial"]) + valor
                enviar_para_extrato(id_cliente_pagador,"transferiu",valor_transferencia,id_cliente_recebedor)
                alterar_saldo_csv()
                consulta_saldo(id_cliente_pagador)
                print("\n============= TRANSFERIU PARA =============\n")
                consulta_saldo(id_cliente_recebedor)