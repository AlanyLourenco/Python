def linha(tam=42):
    return '-'*tam


def cab(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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


def menu(lista):
    cab('Menu principal')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc=leiaint('Sua Opc: ')
    return opc
