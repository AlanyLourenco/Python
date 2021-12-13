f=str(input('Digite para saber se é um palindromo: ')).strip().upper()
#separar a frase em palavras, formar lista
p= f.split()
#juntar a lista 
j="".join(p)
inverso=''
for c in range(len(j)-1,-1,-1):
    inverso= inverso+j[c]
print(j,inverso)
if inverso== j:
    print('Palindromo')
else:
    print('Não é um palindromo')
#outra maneira 
f=str(input('Digite para saber se é um palindromo: ')).strip().upper()
#separar a frase em palavras, formar lista
p= f.split()
#juntar a lista 
j="".join(p)
inverso=j[::-1]
if inverso== j:
    print('Palindromo')
else:
    print('Não é um palindromo')
