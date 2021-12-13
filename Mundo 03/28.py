from time import sleep
c=('\033[m', #0- Sem cores
'\033[0;30;41m', #vermelho
'\033[0;30;42m', #verde
'\033[0;30;43m', #amarelo
'\033[0;30;44m', #azul
'\033[0;30;45m', #roxo
'\033[7;30m', #branco 
)

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg,cor=0):
    tam=len(msg)
    print(c[cor], end='')
    print('~'*tam)
    print(msg)
    print('~'*tam)
    print(c[0], end='')
    sleep(1)


comando=''
while True:
    titulo('  Sistema de ajuda PyHelp  ',2)
    comando=str(input('Função ou biblioteca > '))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
titulo('  Até logo!  ',1)
