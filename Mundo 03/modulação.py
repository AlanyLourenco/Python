from modu import moeda
from modu import dado
n=dado.leiadinhesgiro('Digite um preço: ')
aumento=int(input('Digite a porcentagem do aumento: '))
des=int(input('Digite a porcentagem do desconto: '))

moeda.resumo(n,aumento,des)