m=0
maiorim=0
nv=''
m20=0
for c in range(1,5):
   n=str(input('Nome: ')).strip()
   i=int(input('Idade: '))
   s=str(input('Sexo [M/F]: ')).strip()
   m=m+i
   if c==1 and s in 'Mm':
    maiorim=i
    nv=n
   if s in 'Mm' and i>maiorim:
    maiorim= i
    nv= n
   if s in 'Ff' and i<20:
    m20=m20+1
print('Média é igual a {}'.format(m/4))
print('O nome do homem mais velo é {} e tem {} anos'.format(nv, maiorim))
print('Ao todo são {} mulheres com menos de 20 anos'.format(m20))
