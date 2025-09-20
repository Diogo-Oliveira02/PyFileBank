from datetime import datetime # Fornece classes para manipulação de datas e horas
import csv                    # Implementa classes para ler e gravar dados tabulares em formato CSV
try:
    # Lê o arquivo CSV, transforma cada linha em um dicionário e cria um grande dicionário CLIENTES
    try:
        with open('cadastro.csv', newline='', encoding="utf-8-sig") as FileCSV:
            leitor_arquivo = csv.DictReader(FileCSV, delimiter=";")
            CLIENTES = {}
            for linha in leitor_arquivo:
                chave = linha["conta"]
                CLIENTES[chave] = linha
    except FileNotFoundError:
        print("Arquvo .csv não encontrado!")
    # Salva todos os CLIENTES no arquivo CSV, sobrescrevendo os dados antigos
    def alterar_saldo_csv():
        with open('cadastro.csv', 'w', newline='', encoding='utf-8-sig') as FileCSV:
            escrever_arquivo = csv.DictWriter(FileCSV, fieldnames=CLIENTES[chave],delimiter=";")
            escrever_arquivo.writeheader()
            for cliente in CLIENTES.values():
                escrever_arquivo.writerow(cliente)
    # Função que envia as operação feito pelo usuario para o arquivo TXT 
    def enviar_para_extrato(nome1, operacao, valor, nome2):
        data_hora = datetime.now().strftime('[%d/%m/%Y][%H:%M]')
        try:
            with open ('extrato.txt', 'a', encoding="utf-8-sig") as ExtractFile:
                if (operacao == "depositou") or (operacao == "sacou"):
                    ExtractFile.write(f"{data_hora};{nome1};{operacao};{str(valor)}\n")
                else:
                    ExtractFile.write(f"{data_hora};{nome1};{operacao};{str(valor)};{nome2}\n")
        except FileNotFoundError:
            print("Arquvo .txt não encontrado!")
    # Função para consutar o saldo do CSV
    def consulta_saldo(id):
        if id not in CLIENTES:
            print("\nCliente não encontrado!\n")
        else:
            print(f"""
                Nome:  {CLIENTES[id]["nome"]}
                Saldo: {CLIENTES[id]["saldo_inicial"]}
            """)
    #Função para exibir quando iniciar o loop do while
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
    #Função para depositar valor na conta
    def depositar_valor(id_cliente,valor_depoisito):
        if not id_cliente in CLIENTES:
            print("\nCliente não encontrado!\n") 
        elif (valor_depoisito <= 0):
            print("\nValor deve ser maior que zero!\n")
        else:
            if float(CLIENTES[id_cliente]["saldo_inicial"]) < 10:
                print("Saldo deve ser maior que R$10,00")
            else: 
                CLIENTES[id_cliente]["saldo_inicial"] = float(CLIENTES[id_cliente]["saldo_inicial"]) + valor_depoisito
                enviar_para_extrato(CLIENTES[id_cliente]["nome"],"deposito",valor_depoisito,"")
                alterar_saldo_csv()
                consulta_saldo(id_cliente)
    #Função de sacar valor da conta
    def sacar_valor(id_cliente,valor_sacar):
        if not id_cliente in CLIENTES:
            print("\nCliente não encontrado!\n")
        elif valor_sacar <= 0:
            print("\nValor deve ser maior que zero!\n")
        else:
            if float(CLIENTES[id_cliente]["saldo_inicial"]) < 10:
                print("Saldo deve ser maior que R$10,00")
            else:
                CLIENTES[id_cliente]["saldo_inicial"] = float(CLIENTES[id_cliente]["saldo_inicial"]) - valor_sacar
                enviar_para_extrato(CLIENTES[id_cliente]["nome"],"saque",valor_sacar,"")
                alterar_saldo_csv()
                consulta_saldo(id_cliente)
    #Função trensfere o valor de uma conta para outra
    def trasferir_valor(id_cliente_pagador, id_cliente_recebedor,valor_transferencia):
        if id_cliente_pagador not in CLIENTES:
            print("\nCliente pagador não encontrado!\n")
        elif id_cliente_recebedor not in CLIENTES:
            print("\nCliente recebedor não encontrado!\n")
        elif valor <= 0:
            print("\nValor deve ser maior que zero!\n")
        elif float(CLIENTES[id_cliente_pagador]["saldo_inicial"]) < 10:
          print("Saldo deve ser maior que R$10,00")  
        else:
            if CLIENTES[id_cliente_pagador]["banco"] == CLIENTES[id_cliente_recebedor]["banco"]:
                CLIENTES[id_cliente_pagador]["saldo_inicial"] = float(CLIENTES[id_cliente_pagador]["saldo_inicial"]) - valor_transferencia
            else:
                CLIENTES[id_cliente_pagador]["saldo_inicial"] = float(CLIENTES[id_cliente_pagador]["saldo_inicial"]) - (valor_transferencia * 1.05)
            CLIENTES[id_cliente_recebedor]["saldo_inicial"] = float(CLIENTES[id_cliente_recebedor]["saldo_inicial"]) + valor_transferencia
            enviar_para_extrato(CLIENTES[id_cliente_pagador]["nome"],"transferiu",valor_transferencia,CLIENTES[id_cliente_recebedor]["nome"])
            alterar_saldo_csv()
            consulta_saldo(id_cliente_pagador)
            print("\n============= TRANSFERIU PARA =============\n")
            consulta_saldo(id_cliente_recebedor)
    #Função consulta o extrato ataves do numero da conta
    def consulta_extrato(id_cliente):
        found = False
        with open('extrato.txt', "r", encoding="utf-8") as extrato:
            print("\n\n ========== EXTRATO BANCARIO ========== \n")
            for linha in extrato:
                valores = linha.strip().split(";")
                registro = list(valores)
                data = registro[0]
                nome = registro[1]
                operacao = registro[2]
                valor = registro[3]
                nome2 = registro[4]
                if id_cliente in nome:  
                    found = True
                    print(data, "\n", nome, operacao, nome2, "\n", "Valor de: R$", valor)
        if not found:
            print("Extrato ainda não possui movimentações")
    while True:
        exibir_menu()
        opcao_menu = int(input("Aperte o numero correspondete que deja fazer a operação --->"))
        match opcao_menu:
            case 1:
                id = input("Digite o numero da conta que deseja depositar >>")
                valor = float(input("Digite o valor que deseja depositar: "))
                depositar_valor(id,valor)
            case 2:
                id = input("Digite o numero da conta que deseja sacar >>")
                valor = float(input("Digite o valor que deseja sacar: "))
                sacar_valor(id,valor)
            case 3:
                id_pagador = input("Digite o numero da conta do cliente que ira ser o pagador >>")
                id_recebedor = input("Digite o numero da conta do cliente que ira receber >>")
                valor = float(input("Qual o valor que deseja trasferir: "))
                trasferir_valor(id_pagador,id_recebedor,valor)
            case 4:
                id = input("Digite o nome do cliente que deseja ver o extrato bancario >>")
                consulta_extrato(id)
            case 5:
                id = input("Digite o nome que seja consultar o saldo >>")
                consulta_saldo(id)
            case 0:
                print("\nObrigado por utilizar o PyFileBank! Até a próxima.\n")
                break
            case _:
                print("Operação não valida!\n")
except Exception as e:
    with open("erros.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {type(e).__name__}: {e}\n")
    print("Ocorreu um erro!")