import datetime
ano=int(input('Que ano quer analisar?  Coloque 0 para analisar o ano atual '))
if ano == 0:
    ano= datetime.date.today().year
if ano%4==0 and ano%100 != 0 or ano%400==0:
    print(' O ano',(ano), 'é bissexto')
else:
    print(' O ano',(ano), 'não é bissexto')
