# ======================================= Laços de Repetição / iteração (for) ========================================
# =======================================FOR SIGNIFICA PARA =========================================================

# ======================================= Significado =================================================================

# O loop for executa um conjunto de declarações várias vezes; é usado para iterar sobre uma sequência (por exemplo, uma lista,
# um dicionário, um tuple, ou um conjunto - aprenderá sobre eles em breve) ou outros objetos que são iteráveis (por exemplo, strings).
# Pode utilizar o loop for para iterar sobre uma sequência de números usando a função range

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")  # POR DEFINIÇAO O (end='') junta com o proximo texto (sep='') serve para separar os textos as strings separadas por virgula.

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# Pode utilizar as declarações break e continue para alterar o fluxo de um loop:

# Utilize break para sair de um loop, por exemplo:
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

# Utilize continue para ignorar a iteração atual e continuar com a próxima iteração, por exemplo:
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

# O objeto da exceção range() gera uma sequência de números. Aceita números inteiros e devolve objetos de range.
# A sintaxe de range() parece como se segue: range(start, stop, step), onde:

# start é um parâmetro opcional que especifica o número inicial da sequência (0 por padrão)
# stop é um parâmetro opcional que especifica o fim da sequência gerada (não está incluído),
# e step é um parâmetro opcional que especifica a diferença entre os números na sequência (1 por padrão.)

for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

# =========================================================================================================================

# essa é a estrutura basica do for, o (c) esta representando uma variavel, pode ser qualquer nome. (1,10) = intervalo de 1 a 10.
for c in range(1, 10):

# vai repetir o ('Oi') de 0 a 5 vezes, ele nao conta o ultimo numero, depois ele vai imprimir fim, por causa da identação
for c in range(0, 6):
    print('Oi')
print('FIM')

# contagem de 1 até 6
for c in range(1, 7):
    print(c)
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

# Crie um loop for que conta de 0 a 10, e imprime os números ímpares
for i in range(0, 11):
    if i % 2 != 0:
        print(i)

# Crie um programa com um loop for e uma declaração break . O programa deve iterar sobre os caracteres de um endereço de
# e-mail, sair do loop quando chegar ao símbolo @ , e imprimir a parte antes de @ numa linha.
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Crie um programa com um loop for e uma declaração continue . O programa deve iterar sobre uma string de dígitos, substituir
# cada 0 com xe imprimir a string modificada no ecrã.
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

# Calcular 3 numeros e fazer a media deles.
soma = 0
for i in range(1, 4):
    nota = (int(input(f'Digite um numero no posição {i}: ')))
    soma += nota
print(soma / 3)


# ===================================================Faça um programa que mostre uma contagem regresiva na tela para o estouro
# de fogos, indo de 10 até 0, com uma pausa de 1 segundo entre eles.=========================================================

# Minha resposta
import time
for i in range(0, 11):
    time.sleep(1)
    print(i)
print('Bommmmmmmmmmmm!!!!')

# Resposta
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('ACABOU!')


# ========================================Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# ===================================================================================================================

# Minha resposta numeros impares
for i in range(0, 51):
     if i % 2 != 0:
        print(i)
# Minha resposta numeros pares
for i in range(0, 51):
     if i % 2 == 0:
        print(i)

# Resposta mais produtiva
for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')

# =========================================Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.================================================================================================================

# Minha reposta
valores = 0
soma =0
for i in range(1, 501, 2):
    if i % 3 == 0:
        valores += i
        soma += 1
        print(i)
print (f' A soma de todos os {soma} valores é : {valores} ')

# Resposta
soma = 0
cont = 0
for c in range(1, 501, 2): # contage de 1 ate 500
    if c % 3 == 0: # numeros divisiveis por 3
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')



# ================================================================Refaça a tabuada, mostrando um número que o usuário escolher,
# só que agora utilizando um laço for.=====================================================================================


# ==================================================== Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsidere-o.======================================================