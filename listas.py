''' frutas = ["pera","uva","maçã","abacaxi"]
print(frutas[1:3])

print(f"Matheus gosta de {frutas[3]}")

frutas.insert(4, "morango")

print(frutas)

frutas[1]="Kiwi"
print(frutas)
indice_fruta = frutas.index("Kiwi")
print(f"O índice da fruta é {indice_fruta}")
del frutas[indice_fruta]
print(frutas)'''

'''lista_mercado = []

while True:
    op = int(input("1 - Adicionar frutas\n \
                2 - Remover frutas \n \
                3 - Lista frutas \n \
                0 - Sair do programa \n \
                Digite a opção: "))

    if op == 1:
        # Adicionar objetos a lista
        item = input("Digite um item: ")
        lista_mercado.append(item)

    elif op == 2:
        # Remover objetos da lista
        item = input("Digite o item que será removido:")
        indice_item = lista_mercado.index(item)
        del lista_mercado[indice_item]

    elif op == 3:

        for item in lista_mercado:
            print(item)

    elif op == 0:
        break'''


#Tupla

'''tupla_teste = ("endpoint", 200)

tupla_teste = ("endpoint", 500)
print(tupla_teste[0])
print(tupla_teste[1])'''

dicionario = {
    1: {
        'nome':'João',
        'email':'balblabla@.com.br',
        'numero':'9999999',
        'qualificação':['1','2']
    },
    2: {
        'nome':'maria',
        'email':'blelele@kj.com.br',
        'numero':'12345667'
    }
}

print(dicionario[1]['qualificação'][0])

""" matriz = [
    [[4, 5, 6], [7, 8, 9], [10, 11, 12]],
    [2, 4, 6],
    [4, 8, 12]
]

print(matriz[0])
print(matriz[0][1])
print(matriz[0][2])
print(matriz[2][0])
matriz[0][1] = 3, 4, 5
print(matriz)
del matriz[2][1]
print(matriz) """

'''nome = ""
while len(nome)== 0:
    nome = input("Qual o seu nome?")
print(f"Olá, {nome}!")'''

'''matriz = [
    [4, 5, 6],
    [2, 4, 6],
    [4, 8, 12]
]'''

'''for linha in matriz:
    for coluna in linha:
        print(coluna)'''

'''for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriz)):
    for c in range(len(matriz[i])):
        if i == c:
            print(matriz[i][c])

        if (matriz[i][c] % 2) == 0:
            print(f"{matriz[i][c]} -> É par")
        else:
            print(f"{matriz[i][c]} -> É ímpar")
