def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO: Por favor, digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n


def lfloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO: Por favor, digite um número valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n
num=leiaint(('Digite um valor int: '))
num1=lfloat(('Digite um valor float: '))