import textwrap

#### VARIAVEIS GLOBAIS ####
mensagem_encerramento = "Obrigado volte sempre!".upper()
mensagem_opcao_invalida = ("Opção inválida, por favor selecione novamente a opção correta!".upper())
rodape ="".center(30,":")
sucesso = ("Operação realizada com sucesso".upper())

def menu():
    menu = """
    ::::: MENU PRINCIPAL :::::
    
    [1]\tDEPOSITAR VALOR
    [2]\tREALIZAR SAQUE
    [3]\tGERAR EXTRATO
    [4]\tNOVA CONTA
    [5]\tLISTA DE CONTAS
    [6]\tNOVO USUARIO
    [s]\tSAIR DA OPERAÇÃO
    >>>"""

    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato, /):
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
        
    return saldo, extrato,

def sacar(*, saldo, valor,extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(rodape)
        print("Saque não permitido! Você não possui saldo suficiente.".upper())
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

    return saldo, extrato

def exibir_extrato(saldo, /,*, extrato):
    cabecalho_extrato = "EXTRATO"
    rodape_extrato = "FIM DO EXTRATO"
    
    print(cabecalho_extrato.center(30,":"))
    print() #PULA UMA LINHA
    print("Não foram realizadas movimentações." if not extrato else extrato)

    print() #PULA UMA LINHA
    print(rodape)
    print(f"""Saldo: R$ {saldo:.2f}""".upper())
    print(rodape_extrato.center(30,":"))

def criar_usuario (usuarios):
    cpf = input("INFORME O CPF PARA CADASTRO (ACEITO SOMENTE NÚMEROS): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuario com esse CPF!".upper())
        return

    nome = input("INFORME O NOME COMPLETO: ")
    data_nascimento = input("INFORME A DATA DE NASCIMENTO (DD-MM-YYYY): ")
    endereco = input("INFORME O ENDEREÇO (RUA, Nº - BAIRRO - CIDADE/SIGLA DO ESTADO): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "usuarios": usuarios})
    print(f"Cadastro de usuario: {sucesso}".upper())

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia, numero_conta, usuarios):
    cpf = input("INFORME O CPF DE USUÁRIO: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"Criação de usuário: {sucesso}".upper())
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não localizado, operação não realizada!".upper())

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Títular: {conta ['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
        
    print("SEJA BEM VINDO".center(30,":"))
    while True:
            opcao = menu()
                    
            if opcao == "1":
                valor = float(input("INFORME O VALOR A SER DEPOSITADO: R$"))
                print() #PULA UMA LINHA
                
                saldo, extrato = depositar(saldo, valor, extrato)
            
            elif opcao == "2":
                valor = float(input("INFORME O VALOR DO SAQUE: R$"))
                print() #PULA UMA LINHA
                
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
            elif opcao == "3":
                exibir_extrato(saldo, extrato=extrato)

            elif opcao == "4":
                numero_conta = len(contas) +1
                conta = criar_conta(AGENCIA,numero_conta,usuarios, contas)

                if conta: 
                    contas.append(conta)
            
            elif opcao == "5":
                listar_contas(contas)

            
            elif opcao == "6":        
                criar_usuario(usuarios)

            elif opcao == "s":
                print(rodape)
                print(mensagem_encerramento.center(30,":"))
                print(rodape)
                break

            else:
                print(rodape)
                print(mensagem_opcao_invalida)
                print(rodape)
main()