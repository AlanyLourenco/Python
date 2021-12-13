import datetime
a= datetime.date.today().year
d=int(input('Em que ano você nasceu? '))
if a-d<=9:
    print('Você tem {} anos'.format(a-d))
    print('Mirim')
elif 10<a-d<=14:
    print('Você tem {} anos'.format(a-d))
    print('Infantil')
elif 14<a-d<=19:
    print('Você tem {} anos'.format(a-d))
    print('Júnior')
elif 19<a-d<=25:
    print('Você tem {} anos'.format(a-d))
    print('Sênior')
else:
    print('Você tem {} anos'.format(a-d))
    print('Master')
