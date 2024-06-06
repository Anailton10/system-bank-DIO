from colorama import Fore, init

menu = """########### MENU ##########

[ 0 ] Deposito
[ 1 ] Saque
[ 2 ] Extrato
[ 3 ] Sair

=>"""

saldo = 0
deposito = 0
cont_deposito = cont_saque = 0
limite = 500
extrato = ""
num_saques = 0
limite_saque = 3
historico_deposito = []
historico_saque = []

while True:
    init(autoreset=True)
    opcao = int(input(menu))

    if opcao == 0:
        deposito = float(input("Informe o valor do deposito: "))

        while deposito < 0:
            print(f"Você informou o valor R${deposito:.2f}. Impossível depositar valor negativo\n")
            deposito = float(input("Informe o valor do deposito: "))
        saldo += deposito
        historico_deposito.append(deposito)
        print("Deposito efetuado com sucesso!!\n")

    elif opcao == 1:
        saque = float(input('Informe o valor do saque: '))
        cont_saque += 1
        if cont_saque > limite_saque:
            print(Fore.RED + 'FOI ATINGIDO O LIMITE DE VEZES DIARIO')
            break
        elif saque > saldo:
            print(Fore.RED + f'ERRO!! Foi solicitado R${saque:.2f} mas seu saldo é de R${saldo:.2f}')
        elif saque > limite:
            print(Fore.RED + 'FOI ATINGIDO O LIMITE DE SAQUE DIARIO')
        else:
            saldo -= saque
            historico_saque.append(saque)

    elif opcao == 2:
        print(Fore.GREEN + "EXTRATO BANCARIO")
        if historico_deposito:
            print("\n".join([Fore.CYAN + f"DEPOSITO - R${x:.2f}" for x in historico_deposito]))
        else:
            print(Fore.CYAN + "DEPOSITO - R$ 0.00")
        if historico_saque:
            print("\n".join([Fore.BLUE + f"SAQUES - R${y:.2f}" for y in historico_saque]))
        else:
            print(Fore.YELLOW + "SAQUE - R$ 0.00")
        print(Fore.GREEN + f"SALDO EM CONTA - R${saldo:.2f}")
        print(f"Contador de saques: {cont_saque}")
    elif opcao == 3:
        print('Até mais!!')
        break

    else:
        print(Fore.RED + 'Opção inválida, tente novamente!!\n')
