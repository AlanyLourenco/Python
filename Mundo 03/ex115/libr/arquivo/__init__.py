from ex115.libr.interfac import *
def arqexist(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(nome):
    try:
        a=open(nome, 'wt+')
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArq(nome):
    try:
        a= open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cab('Pessoas cadastradas')
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a=open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
