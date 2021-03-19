perg1 = int(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
perg2 = int(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
perg3 = int(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
perg4 = int(input("Devia para a vítima? 1/Sim ou 0/Não: "))
perg5 = int(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
soma_respostas = 0
if (soma_respostas < 2):
 print("Inocente")
elif (soma_respostas == 2):
 print("Suspeita")
elif (3 <= soma_respostas <= 4):
 print("Cúmplice")
elif (soma_respostas == 5):
 print("Assassino")
res = []
for i in range(len("lista_perguntas")):
     print("lista_perguntas"[i])
     res.append(input())
     soma_respostas += int(res[i])
     status = ["Inocente", "Suspeita", "Cúmplice", "Cúmplice", "Assassino"]
if soma_respostas < 2:
     print(status[0])
else:
     print(status[soma_respostas - 1])

     res1 = int(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
     res2 = int(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
     res3 = int(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
     res4 = int(input("Devia para a vítima? 1/Sim ou 0/Não: "))
     res5 = int(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
     soma_respostas = res1 + res2 + res3 + res4 + res5
     if (soma_respostas < 2):
         print("Inocente")
     elif (soma_respostas == 2):
         print("Suspeita")
     elif (3 <= soma_respostas <= 4):
         print("Cúmplice")
     elif (soma_respostas == 5):
         print("Assassino")