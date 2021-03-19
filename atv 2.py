#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

num = float(input('informe um numero: '))
if int(num) == num:
    print('numero inteiro :')
else:
    print('numero decimal')
