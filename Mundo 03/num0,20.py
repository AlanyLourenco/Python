numero=('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
        num= int(input('Digite um numero ente 0 e 20: '))
        if 0<=num<=20:
                break
        print('tente novamente. ', end='')
print(f'O número {num} por extenso é {numero[num]}')
#num=int(input('Digite um número: '))
#while num>20 or num<0:
        #num=int(input('Digite um número'))
#if num>=0 and num<=20:
    #print(f'O número {num} por extenso é {numero[num]}')

#outro modo