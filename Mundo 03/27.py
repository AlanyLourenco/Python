def notas(*n,sit=False):
    r={}
    r['total']=len(n)
    r['Maior']=max(n)
    r['Menor']=min(n)
    r['Média']=sum(n)/len(n)
    if sit:
        if r['Média']>= 7:
            r['Situação']='Boa'
        elif r['Média']>= 5:
            r['Situação']='Razoavel'
        else:
            r['Situação']='Ruim'
    return r


resp=notas(5,10,9, sit=True)
print(resp)
