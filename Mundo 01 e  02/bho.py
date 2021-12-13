n=int(input('Digite um número: '))
d=str(input('Digite "B" para converter para Binário \nDigite "O" para converter para Octal \nDigite "H" para converter para Hexadecimal ')).upper()
if d=='B':
 print('O numero {} em binario é: {}'.format(n, bin(n)[2:]))
elif d=='O':
    print('O numero {} em hexadecimal é: {}'.format(n, oct(n)[2:]))
elif d=='H':
    print('O numero {} em octal é: {}'.format(n, hex(n)[2:]))
