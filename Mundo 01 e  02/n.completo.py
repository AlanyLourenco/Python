n=str(input('Digite o seu nome: ')).strip()
print(('Seu nome em maiusculo é:'), (n.upper()))
print(('Seu nome em minusculo é :'), (n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n)- n.count(' ')))
#print ('Seu primeiro nome tem {} letras'.format(n.find(' ')))
sep= n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(sep[0], len(sep[0])))
