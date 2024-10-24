#DECLARAÇÕES###########################################################

menu ="""
[1] DEPOSITAR VALOR
[2] REALIZAR SAQUE
[3] GERAR EXTRATO
[e] SAIR DA OPERAÇÃO
>>>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
mensagem_encerramento = "Obrigado volte sempre!".upper()
mensagem_opcao_invalida = ("Opção inválida, por favor selecione novamente a opção correta!".upper())
rodape ="".center(30,":")
sucesso = ("Operação realizada com sucesso".upper())


#CÓDIGO###########################################################

print("SEJA BEM VINDO".center(30,":"))
while True:
    opcao = input(menu)
    print()
    
    if opcao == "1":
        valor = float(input("INFORME O VALOR A SER DEPOSITADO: R$"))
        print()

        if valor > 0:
            saldo += valor
            extrato += (f"""Depósito: R$ {valor:.2f}\n""".upper())
            msg_saldo_atual = (f"Saldo atual: R${saldo:.2f}").upper()

            print(rodape)
            print(sucesso)
            print(msg_saldo_atual)
            print(rodape)

        else:
            print(rodape)
            print("VALOR INVÁLIDO! REFAÇA A OPERAÇÃO")
            print(rodape)

    elif opcao == "2":
        valor = float(input("INFORME O VALOR DO SAQUE: R$"))
        print()

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(rodape)
            print("Saque não permitido!Você não possui saldo suficiente.".upper())
            print(rodape)

        elif excedeu_limite:
            print(rodape)
            print("Saque não permitido! O valor do saque excede o limite permitido.".upper())
            print(rodape)
        elif excedeu_saques:
            print(rodape)
            print("Saque não permitido! Número máximo de saques diários foi excedido.".upper())
            print(rodape)

        elif valor > 0:
            saldo -= valor
            extrato += (f"""Saque: R$ {valor:.2f}\n""".upper())
            numero_saques += 1
            msg_saldo_atual = (f"Saldo atual: R${saldo:.2f}").upper()

            print(rodape)
            print(sucesso)
            print(msg_saldo_atual)
            print(rodape)

        else:
            print(rodape)
            print("Operação falhou! O valor informado é inválido.".upper())
            print(rodape)

    elif opcao == "3":
        cabecalho_extrato = "EXTRATO"
        rodape_extrato = "FIM DO EXTRATO"
        print(cabecalho_extrato.center(30,":"))
        print("Não foram realizadas movimentações." if not extrato else extrato)

        print(rodape)
        print(f"""Saldo: R$ {saldo:.2f}""".upper())
        print(rodape_extrato.center(30,":"))

    elif opcao == "e":
        print(rodape)
        print(mensagem_encerramento.center(30,":"))
        print(rodape)
        break

    else:
        print(rodape)
        print(mensagem_opcao_invalida)
        print(rodape)

