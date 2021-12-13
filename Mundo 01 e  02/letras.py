a=str(input('Digitel algo: ').lower()).strip().upper()
print('A letra A aprece {} vezes'.format(a.count('A')))
print('A letra A aparece pela primeira vez na posição {}'. format(a.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}'. format(a.rfind('A')+1))