from ex115.libr.interfac import*
from ex115.libr.arquivo import*
arq='Alany.txt'
if not arqexist(arq):
    criararq(arq)
while True:
    respost=menu(['VER PESSOAR CADASTRADAS','CADASTRAR PESSOAS','SAIR DO SISTEMA'])
    if respost==1:
        lerArq(arq)
    elif respost==2:
        cab('NOVO CADASTRO')
        Nome=str(input('Nome: '))
        idade=leiaint('Idade: ')
        cadastrar(arq,Nome,idade)
    elif respost==3:
        cab('Saindo do sistema')
        break
    else: 
        cab('ERRO! Digite uma opção válida! ')