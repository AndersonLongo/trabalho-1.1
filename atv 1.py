# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

numero = int(input('me diga um numero inteiro:'))
resultado = numero % 2
if resultado == 0:
    print('o numero e par'.format (numero))
else:
    print('o numero e impar'.format (numero))

