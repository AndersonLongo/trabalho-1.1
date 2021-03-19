combustivel = print(input ("Digite o tipo de combustível que você colocou:"))
litro = print(input ("Digite a quantidade de litros que você colocou:"))
desconto1 = int(input('3%'))
desconto2 = int(input('5%'))
desconto3 = int(('4%'))
desconto4 = int(input('6%'))
if combustivel == "A":
    alcool = 3.5
    custo = litro * alcool
if litro == 20:
   desconto1 = (custo * 3)/100
print("O desconto de combustivel foi de : {} e o preço agora é {}".format(desconto1,custo-desconto1))
if litro == 20:
    desconto2 = (custo * 5)/100
print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto2,custo-desconto2))
if combustivel == "G":
    gasolina = 4.6
    custo = (litro * gasolina)
if litro <= 20:
   desconto3 = (custo * 4)/100
print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto3,custo-desconto3))
if litro > 20:
     desconto4 = (custo * 6)/100
print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto4,custo-desconto4))