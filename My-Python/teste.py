# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.

soma = 0
cont = 0
for c in range(1, 501, 2): # contage de 1 ate 500
    if c % 3 == 0: # numeros divisiveis por 3
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')