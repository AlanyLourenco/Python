v=float(input('Qual a velocidade do carro? '))
if v>80:
    print('você sera multado')
    print('Sua multa custará {}'.format((v-80)*7))
else:
    print('Sua velocidade esta dentro dos parametros legais para esta estrada')

