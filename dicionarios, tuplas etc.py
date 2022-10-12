'''frutas = ["pera","uva","maçã","abacaxi"]
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

