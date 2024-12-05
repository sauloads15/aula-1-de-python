# minha_lista = []

# dados = input("Digite algo")

# minha_lista.append(dados)

# print(f"sua nova lista é: {minha_lista}")

# minha_lista = [1,2,3,4,5]

# print(minha_lista[4])

# minha_lista = [10,True,"sdvsea",5]

# novo_item = input("Digite Algo: ")

# minha_lista.append(novo_item)

# minha_lista.pop(1)
# print(minha_lista)

# numeros = [1, 2, 3, 4, 5]
# numeros.append(6)
# print(numeros)

# numeros = [10, 30, 40, 50]
# letras = ['a', 'e', 'o', 'u']
# pesos= [1.2, 3.4, 5.3, 6.7]

# numeros.insert(1, 20)
# letras.insert(2, 'i')
# pesos.insert(2, 4.0)

# print(numeros)
# print(letras)
# print(pesos)
# minha_lista= [
# "Arroz",
# "Feijao",
# "Paçoca",
# "Pudim",
# "Panetone"
# ]

# for item in minha_lista:
#     print("[]", item)

# frutas = ("maçã", "banana", "laranja", "abacaxi")

# maca, banana, laranja, abacaxi = frutas
# print("Fruta 1:", maca)
# print("Fruta 2:", banana)
# print("Fruta 3:", laranja)
# print("Fruta 4:", abacaxi)

resultados = [
    ("Equipe A", [8, 7, 9, 10]),
    ("Equipe B", [6, 5, 8, 7]),
    ("Equipe C", [9, 10, 8, 10]),
    ("Equipe D", [7, 8, 7, 6]),
]

medias = []  
for equipe, pontuacoes in resultados:
    media = sum(pontuacoes) / len(pontuacoes) 
    medias.append((equipe, media))  

medias.sort(key=lambda x: x[1], reverse=True) 


classificacao = medias  
print("Classificação Final:")
for posicao, (equipe, media) in enumerate(classificacao, start=1):
    print(f"{posicao}º lugar: {equipe} - Média: {media:.2f}")
