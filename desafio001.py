menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Depósito')
        deposito = float(input('Digite o valor de depósito:\nR$'))
        if deposito <= 0:
            print('Depósito inválido')
        else:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print('Saldo atual: R$'+ str(saldo))
    
    elif opcao == 's':
        print('Saque')
        saque = float(input('Digite o valor de saque:\nR$'))
        if numero_saques >= LIMITE_SAQUES:
            print('Limite de saques diários atingido.')
        elif saque > saldo:
            print('Saldo insuficiente')
        elif saque > 500:
            print('Valor máximo de R$500,00 por saque atingido.')
        else:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1
            print('Saldo atual: R$' + str(saldo))
    
    elif opcao == 'e':
        print('----Extrato----')
        if not extrato:
            print('Não foram realizadas movimentações.')
            print('Saldo atual: R$' + str(saldo))
        else:
            print(extrato)
            print('Saldo atual: R$' + str(saldo))
        
    
    elif opcao == 'q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
