produto = input("Por favor, informe o produto desejado(Morango ou Maçã):")
peso = input("Informe o peso do produto:")
preço1 = int(input(2.50))
preço2 = int(input(2.20))
preço3 = int(input(1.80))
preço4 = int(input(1.50))
if produto == "morango":
   morango = 2.50
   custo = 2.50
elif peso <= 5:
    print(f"O preço por kg de seu produto ficou:{preço1}")
elif peso >= 5:
    print(f"O preço por kg de seu produto ficou:{preço2}")

elif produto == "maçã":
   maçã = 1.80
   custo = preço3
elif peso <= 5:
    print(f"O preço de seu produto por kg ficou: {preço3}")
