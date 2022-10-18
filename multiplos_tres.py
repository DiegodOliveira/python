soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i
print(f"A soma de todos os {cont} valores solicitados é {soma}")

'''Este código irá somar apenas os números pares vindos do input'''
'''soma = 0
cont = 0
for i in range(1, 7):
    num = int(input(f"Digite o {i}° valor: "))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f"Você informou {cont} e a soma foi {soma}")'''