from random import randint
computador = randint(0,5)
print('§'*40)
print('Vou pensar em um número entre 0 e 5, tente adivinhar, mero mortal...')
print('§'*40)
jogador = int(input("Em que número pensei?..."))
if jogador == computador:
    print("Derrotaste-me, mortal")
else:
    print("Escória, mortal...")
    