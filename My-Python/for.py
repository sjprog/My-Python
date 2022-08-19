# ======================================= Laços de Repetição / iteração (for) ========================================
# =======================================FOR SIGNIFICA PARA =========================================================
# essa é a estrutura basica do for, o (c) esta representando uma variavel, pode ser qualquer nome. (1,10) = intervalo de 1 a 10.
for c in range(1, 10):

# vai repetir o ('Oi') de 0 a 5 vezes, ele nao conta o ultimo numero, depois ele vai imprimir fim, por causa da identação
for c in range(0, 6):
    print('Oi')
print('FIM')

# contagem de 1 até 6
for c in range(1, 7):
    print(C)
print('FIM')

# contagem negativa, pra traz, tem que colocar negativo, esse -1 é o intervalo, pode ser positivo tambem
for c in range(6, 0, -1):
    print(c)
print('FIM')

# exemplo com o for, se digitar o numero 3 ele vai de 0 até 3
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

#  exemplo, otimo exemplo por sinal
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

# exemplo, o for vai ler o comando 3 vezes
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('fim')

# exemplo
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')

# ============================================= Praticar ==============================================

# Faça um programa que mostre uma contagem regresiva na tela para o estouro de fogos, indo de 10 até 0, com uma
# pausa de 1 segundo entre eles.
