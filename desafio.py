menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposíto: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! o valor informado é invalido.")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        ultrapassou_saldo = valor > saldo
        
        ultrapassou_limite = valor > limite
        
        ultrapassou_saques = numero_saques >= LIMITES_SAQUES
        
        if ultrapassou_saldo:
            print("Operação falhou! você não tem saldo suficiente")
        
        elif ultrapassou_limite:
            print("Operação falhou! o valor do saque ultrapassou o limite.")
            
        elif ultrapassou_saques:
            print("Operação falhou! Número maximo de saques ultrapassado")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação falhou! o valor informado é invalido.")
            
    elif opcao == "e":
        print("\n=============== EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")
        
    elif opcao == "q":
        print("Obrigado por escolher nosso serviço, volte sempre!!!!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")