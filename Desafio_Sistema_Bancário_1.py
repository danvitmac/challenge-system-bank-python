menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Chave Pix
[9] Sair

=> """

saldo = 0
limite_operacao = 500
extrato = ""
chave_pix = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"\n+    Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_operacao

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente para realizar a operação.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite por operação.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de operações de saque ao dia excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"\n-    Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")
            

    elif opcao == "2":
        print("\n==================== CHAVE PIX ====================\n")
        print("Não foi cadastrada nenhuma Chave Pix até o momento." if not chave_pix else f"Sua Chave Pix {chave_pix}")
        print("\n===================== EXTRATO =====================")
        print("\nNão foram realizadas operações.\n" if not extrato else f"{extrato}")
        print("====================== SALDO ======================")
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("===================================================")

    elif opcao == "3":
        chave_pix = input("Informe a sua Chave Pix: ")

    
    elif opcao == "9":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")