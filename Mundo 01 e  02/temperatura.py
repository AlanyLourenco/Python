c=float(input('informe a temperatura em cº: '))
f=((c*9)/5)+32
k=c+273
print('A temeratura de {}ºC corresponde a {} F!'.format(c, f))
print('A temperatura de {}ºC corresponde a {} K'.format (c, k))
f1=float(input('informe a temperatura em F!: '))
c1=(f1-32)/1.8
k1=(f1-32)*(5/9)+273
print('A temeratura de {}F! corresponde a {:.2f} Cº '.format(f1,c1))
print('A temperatura de {}F! corresponde a {:.2f} K'.format (f1, k1))
k2=float(input('informe a temperatura em K: '))
c2=k2-273
f2=(k2-273)*1.8+32
print('A temeratura de {}k corresponde a {:.2f} Cº '.format(k2,c2))
print('A temeratura de {}k corresponde a {:.2f} F! '.format(k2,f2))
