n=int(input('Primo ou não? '))
t=0
for c in range (1,n+1):
  if n%c==0:
    print('\033[34m', end=' ')
    t=t+1
  else:
    print('\033[31m', end=' ')
  print('{}'.format(c), end=' ')
print('O número {} foi divisível {} vezes'.format(n,t))
if t>2:
  print('Não primo')
else:
  print('Primo')
  