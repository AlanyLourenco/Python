aluno1={}
aluno1['Nome']=str(input('Nome do aluno: '))
aluno1['Média']=float(input('Média do aluno: '))
if aluno1['Média']>=7:
    aluno1['Situação']='Aprovado'
else:
    aluno1['Situação']='Reprovado'
for k,v in aluno1.items():
    print(f'{k} = {v}')
print('')