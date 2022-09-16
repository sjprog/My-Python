# ======================================= Laços de Repetição / iteração (for) ========================================

# =======================================FOR SIGNIFICA (PARA) =========================================================

# ============================================= Fazer loop ao seu código com for
# Outro tipo de loop disponível em Python vem da observação de que por vezes é mais importante contar as "voltas"
# do loop do que verificar as condições.

# Imagine que o corpo de um loop precisa de ser executado exatamente cem vezes. Se desejar utilizar o
# loop while para o fazer, pode ser assim:
#
i = 0
while i < 100:
    # do_something()
    i += 1

# Seria bom se alguém pudesse fazer esta contagem aborrecida por si. Isso é possível?

# Claro que é - há um loop especial para estes tipos de tarefas, e é chamado for.
#
# Na verdade, o loop for foi concebido para realizar tarefas mais complicadas - pode "navegar" por grandes coleções
# de dados item por item. Mostraremos como fazê-lo em breve, mas neste momento vamos apresentar uma variante mais
# simples da sua aplicação.

# Dê uma vista de olhos no snippet:

for i in range(100):
    # do_something()
    pass

# Existem alguns novos elementos. Deixe-nos falar sobre eles:

# ===> a keyword for abre o loop for ; nota - não há nenhuma condição depois; não é preciso pensar nas condições,
#   uma vez que são verificadas internamente, sem qualquer intervenção;
# ===> qualquer variável após a keyword for é a variável de controlo do loop; conta as voltas do loop, e fá-lo
#   automaticamente;
# ===> a keyword in introduz um elemento de sintaxe que descreve a gama de valores possíveis que estão a ser atribuídos
#   à variável de controlo;
# ===> a função range() (esta é uma função muito especial) é responsável por gerar todos os valores desejados da variável
#   de controlo; no nosso exemplo, a função irá criar (podemos mesmo dizer que irá alimentar o loop com) valores
#   subsequentes a partir do conjunto seguinte: 0, 1, 2 .. 97, 98, 99; nota: neste caso, a função range() começa o
#   seu trabalho a partir do 0 e termina um passo (um número inteiro) antes do valor do seu argumento;
# ===> note a keyword pass dentro do corpo do loop - não faz nada; é uma instrução vazia - colocamo-la aqui porque a for
#   sintaxe do laço exige pelo menos uma instrução dentro do corpo (a propósito - if, elif, else e while
#   expressam a mesma coisa)

for i in range(10):
    print("The value of i is currently", i)

# Execute o código para verificar se estava certo.

# Nota:

# ===> o loop foi executado dez vezes (é o argumento da função range() )
# ===> o valor da última variável de controlo é 9 (não 10, visto começar a partir de 0, não a partir de 1)

# A função range() pode ser equipada com dois argumentos, e não apenas um:

for i in range(2, 8):
    print("The value of i is currently", i)

# Neste caso, o primeiro argumento determina o (primeiro) valor inicial da variável de controlo.

# O último argumento mostra o primeiro valor que a variável de controlo não será atribuída.

# Nota: a função range() aceita apenas inteiros como seus argumentos, e gera sequências de inteiros.

# Consegue adivinhar o output do programa? Execute-o para verificar se também estava certo agora.

# O primeiro valor mostrado é 2 (retirado do primeiro argumento range().)

# O último é 7 (embora o range()segundo argumento seja 8).

# ============================================== Mais sobre o loop for e a range() função com três argumentos
range()
# A função range() também pode aceitar três argumentos - dê uma vista de olhos ao código no editor.

# O terceiro argumento é um incremento - é um valor acrescentado para controlar a variável em cada volta do loop
# (como se pode suspeitar, o valor por defeito do incremento é 1).

# Consegue dizer-nos quantas linhas irão aparecer na consola, e que valores irão conter?

# Execute o programa para saber se estava certo.

# Deve ser capaz de ver as seguintes linhas na janela da consola:

The value of i is currently 2
The value of i is currently 5

# Sabe porquê? O primeiro argumento passado para a função range() diz-nos qual o número inicial da sequência
# (logo, 2 no output). O segundo argumento informa à função onde parar a sequência (a função gera números até
# ao número indicado pelo segundo argumento, mas não o inclui). Finalmente, o terceiro argumento indica a etapa,
# que na realidade significa a diferença entre cada número na sequência de números gerados pela função.

# 2 (número inicial) → 5 (2 incremento de 3 é igual a 5 - o número está dentro do intervalo de 2 a 8) → 8
# (5 incremento de 3 é igual a 8 - o número não está dentro do intervalo de 2 a 8, porque o parâmetro stop
# não está incluído na sequência de números gerados pela função.)

# Nota: se o conjunto gerado pela função range() está vazio, o loop não irá executar de todo o seu corpo.

# Tal como aqui - não haverá output:

for i in range(1, 1):
    print("The value of i is currently", i)


# Nota: o conjunto gerado pelo range() tem de estar ordenado por ordem crescente. Não há como forçar o range()
# a criar um conjunto de uma forma diferente quando a função range() aceita exatamente dois argumentos. Isto
# significa que o segundo argumento de range()deve ser maior que o primeiro.

# Logo, também não haverá output aqui:

for i in range(2, 1):
    print("The value of i is currently", i)


# Vamos dar uma vista de olhos num programa curto, cuja tarefa é escrever algumas das primeiras potências de dois:

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2
# 2 to the power of 0 is 1
# 2 to the power of 1 is 2
# 2 to the power of 2 is 4
# 2 to the power of 3 is 8
# 2 to the power of 4 is 16
# 2 to the power of 5 is 32
# 2 to the power of 6 is 64
# 2 to the power of 7 is 128
# 2 to the power of 8 is 256
# 2 to the power of 9 is 512
# 2 to the power of 10 is 1024
# 2 to the power of 11 is 2048
# 2 to the power of 12 is 4096
# 2 to the power of 13 is 8192
# 2 to the power of 14 is 16384
# 2 to the power of 15 is 32768


# A expo variável é usada como uma variável de controlo para o loop, e indica o valor atual do expoente.
# A exponenciação em si é substituída pela multiplicação por dois. Uma vez que 20 é igual a 1, então 2 x;
# 1 é igual a 21, 2 x; 21 é igual a 22, e assim por diante.

# ====================================================

import time

for second in range(1, 6):
    print(second, "Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")
# 1 Mississippi
# 2 Mississippi
# 3 Mississippi
# 4 Mississippi
# 5 Mississippi
# Ready or not, here I come!

# ====================================================

# ================================================================= Os loops break e declarações continue .

# Até agora, temos tratado o corpo do loop como uma sequência indivisível e inseparável de instruções que
# são executadas completamente a cada volta do loop. No entanto, como programador, poderá ser confrontado
# com as seguintes escolhas:

# =====> parece que é desnecessário continuar o loop como um todo; deve abster-se de continuar a execução do corpo do
#   loop e continuar;
# =====> parece que é necessário iniciar a próxima volta do loop sem completar a execução da volta atual.

# O Python fornece duas instruções especiais para a execução de ambas estas tarefas. Digamos, por uma questão de
# precisão, que a sua existência na linguagem não é necessária - um programador experiente é capaz de codificar
# qualquer algoritmo sem estas instruções. Tais adições, que não melhoram o poder expressivo da linguagem, mas
# apenas simplificam o trabalho do programador, são por vezes chamadas de doces sintáticos, ou açúcar sintático.

# Estas duas instruções são:

# =====> break - sai imediatamente do loop, e termina incondicionalmente a operação do loop; o programa começa
#   a executar a instrução mais próxima após o corpo do loop;
# =====> continue - comporta-se como se o programa tivesse subitamente chegado ao fim do corpo; inicia-se a volta
#   seguinte e a expressão da condição é testada imediatamente.

# Ambas as palavras são keywords.
#
# Agora vamos mostrar-lhe dois exemplos simples para ilustrar como as duas instruções funcionam. Veja o código no
# editor. Execute o programa e analise o output. Modifique o código e experimente.

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")
# The break instruction:
# Inside the loop. 1
# Inside the loop. 2
# Outside the loop.
#
# The continue instruction:
# Inside the loop. 1
# Inside the loop. 2
# Inside the loop. 4
# Inside the loop. 5
# Outside the loop.

# ====================================================

# ===================================================== Os loops break e declarações continue : mais exemplos

# Voltemos ao nosso programa que reconhece o maior entre os números introduzidos. Iremos convertê-lo duas vezes,
# utilizando as instruções break e continue .

# Analise o código, e julgue se e como utilizaria qualquer um deles.

# A variante break vai aqui:

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

# ====================================================

# =================================================== E agora a variante continue :
#
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


# Olhe cuidadosamente, o utilizador introduz o primeiro número antes de o programa entrar no loop while .
# O número subsequente é inserido quando o programa já está em loop.

# =====================================================================

# Crie um programa que use um loop while e pede continuamente ao utilizador para introduzir uma palavra, a menos que o
# utilizador introduza "chupacabra" como a palavra secreta de saída, caso em que a mensagem "You've successfully left
# the loop." deve ser impressa para o ecrã, e o loop deve terminar.

# Não imprima nenhuma das palavras introduzidas pelo utilizador. Utilize o conceito de execução condicional e a break declaração.

while True:
    word = input("You're stuck in an infinite loop!\nEnter the secret word to leave the loop: ")
    if word == "chupacabra":
        break
print("You've successfully left the loop!")
# You're stuck in an infinite loop!
# Enter the secret word to leave the loop: 1000
# You're stuck in an infinite loop!
# Enter the secret word to leave the loop:
# KeyboardInterrupt

# =====================================================================

# A sua tarefa aqui é muito especial: tem de conceber um vowel eater (comedor de vogais)! Escreva um programa que use:

# um loop for ;
# o conceito de execução condicional (if-elif-else)
# a declaração continue .
# O seu programa deve:

# pedir ao utilizador para introduzir uma palavra;
# usar user_word = user_word.upper() para converter a palavra introduzida pelo utilizador em maiúsculas;
# falaremos sobre os chamados métodos de strings e o método upper() muito em breve - não se preocupe;
# usar execução condicional e a declaração continue para “comer” as seguintes vogais A, E, I, O, U da
# palavra introduzida;
# imprimir as letras não comidas para o ecrã, cada uma delas numa linha separada.

user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
# Enter your word: Gregory
# G
# R
# G
# R
# Y

# =====================================================================

# O seu programa deve:

# pedir ao utilizador para introduzir uma palavra;
# usar user_word = user_word.upper() para converter a palavra introduzida pelo utilizador em maiúsculas;
# falaremos sobre os chamados métodos de strings e o método upper() muito em breve - não se preocupe;
# usar execução condicional e a declaração continue para “comer” as seguintes vogais A, E, I, O, U da
# palavra introduzida;
# atribuir as letras não comidas à variável word_without_vowels e imprimir a variável para o ecrã.
# Veja o código no editor. Criámos word_without_vowels e atribuimos-lhe uma string vazia. Utilize a
# operação de concatenação para pedir ao Python que combine as letras selecionadas numa string mais longa durante
# os loops subsequentes, e atribua-a à variável word_without_vowels .

word_without_vowels = ""

user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)
# Enter your word: Gregory
# GRGRY

# =====================================================================

# ====================================================================== Os loops for e o ramo else .

# for os loops comportam-se de forma um pouco diferente - dê uma vista de olhos ao snippet no editor e execute-o.

# O output pode ser um pouco surpreendente.
# A variável i retém o seu último valor.

# Modifique um pouco o código para levar a cabo mais uma experiência.

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
# 0
# 1
# 2
# 3
# 4
# else: 4

# Consegue adivinhar o output?
# O corpo do loop não será executado aqui. Nota: atribuímos a variável i antes do loop.
# Execute o programa e verifique o seu output.
# Quando o corpo do loop não é executado, a variável de controlo retém o valor que tinha antes do loop.

# Nota: se a variável de controlo não existir antes do início do loop, não existirá quando a execução atingir o
# ramo else .

# O que acha desta variante de else?

# Agora vamos falar-lhe de alguns outros tipos de variáveis. As nossas variáveis atuais só podem armazenar
# um valor de cada vez, mas há variáveis que podem fazer muito mais - podem armazenar tantos valores quantos
# você quiser.

# =====================================================================

# A sua tarefa é escrever um programa que leia o número de blocos que os construtores têm, e que produza a altura
# da pirâmide que pode ser construída utilizando estes blocos.

# Nota: a altura é medida pelo número de camadas completamente preenchidas - se os construtores não tiverem um
# número suficiente de blocos e não conseguirem completar a camada seguinte, terminam o seu trabalho imediatamente.

blocks = int(input("Enter the number of blocks: "))

height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1

print("The height of the pyramid:", height)
# Enter the number of blocks: 6
# The height of the pyramid: 3

# =====================================================================

# Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante (ainda não provada)
# que pode ser descrita da seguinte forma:

# tomar qualquer número inteiro não-negativo e não-nulo e nomeá-lo c0;
# se for par, avalie um novo c0 como c0 ÷ 2;
# caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
# Se c0 ≠ 1, saltar para o ponto 2.
# A hipótese diz que, independentemente do valor inicial de c0, irá sempre para 1.

# É claro que é uma tarefa extremamente complexa utilizar um computador para provar a hipótese de qualquer número
# natural (pode até requerer inteligência artificial), mas pode usar o Python para verificar alguns números
# individuais. Talvez até encontre o que possa refutar a hipótese.

# Escreva um programa que leia um número natural e execute os passos acima indicados, desde que c0 permaneça
# diferente de 1. Também queremos que conte os passos necessários para alcançar o objetivo. O seu código deve
# fazer output de todos os valores intermédios de c0, também.

# Dica: a parte mais importante do problema é como transformar a ideia de Collatz num loop while - esta é a
# chave para o sucesso

c0 = int(input("Enter c0: "))

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")
# Enter c0: 15
# 15
# 46
# 23
# 70
# 35
# 106
# 53
# 160
# 80
# 40
# 20
# 10
# 5
# 16
# 8
# 4
# 2
# steps = 17

# =======================================================Resumo ========================================================

# 1. Existem dois tipos de loops em Python: while e for:

# ===> o loop while executa uma declaração ou um conjunto de declarações, desde que uma condição booleana especificada
# seja verdadeira, por exemplo:

# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# ===> o loop for executa um conjunto de declarações várias vezes; é usado para iterar sobre uma sequência
# (por exemplo, uma lista, um dicionário, um tuple, ou um conjunto - aprenderá sobre eles em breve)
# ou outros objetos que são iteráveis (por exemplo, strings). Pode utilizar o loop for para iterar
# sobre uma sequência de números usando a função range . Veja os exemplos em baixo:

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# 2. Pode utilizar as declarações break e continue para alterar o fluxo de um loop:

# ===> Utilize break para sair de um loop, por exemplo:

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

# ===> Utilize continue para ignorar a iteração atual e continuar com a próxima iteração, por exemplo:

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

# 3. Os loops while e for também podem ter uma cláusula else em Python. A cláusula else executa-se após o loop
# terminar a sua execução, desde que não tenha sido terminado por break, por exemplo.:

n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")


# 4. O objeto da exceção range() gera uma sequência de números. Aceita números inteiros e devolve objetos de
# range. A sintaxe de range() parece como se segue: range(start, stop, step), onde:

# ===> start é um parâmetro opcional que especifica o número inicial da sequência (0 por padrão)
# ===> stop é um parâmetro opcional que especifica o fim da sequência gerada (não está incluído),
# ===> e step é um parâmetro opcional que especifica a diferença entre os números na sequência (1 por padrão.)

# Código de exemplo:

for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2
for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

# Crie um loop for que conta de 0 a 10, e imprime os números ímpares no ecrã. Use o esqueleto abaixo:
#
for i in range(1, 11):
    # Line of code.
        # Line of code.
# for i in range(0, 11):
#     if i % 2 != 0:
#         print(i)

# =====================================================================

# Crie um loop while que conta de 0 a 10, e imprime os números ímpares no ecrã. Use o esqueleto abaixo:

x = 1
while x < 11:
    # Line of code.
        # Line of code.
    # Line of code.
# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1

# =====================================================================

# Crie um programa com um loop for e uma declaração break . O programa deve iterar sobre os caracteres de um
# endereço de e-mail, sair do loop quando chegar ao símbolo @ , e imprimir a parte antes de @ numa linha.
# Use o esqueleto abaixo:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        # Line of code.
    # Line of code.
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")

# =====================================================================

# Crie um programa com um loop for e uma declaração continue . O programa deve iterar sobre uma string de dígitos,
# substituir cada 0 com xe imprimir a string modificada no ecrã. Use o esqueleto abaixo:

for digit in "0165031806510":
    if digit == "0":
        # Line of code.
        # Line of code.
    # Line of code.
# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

# =====================================================================

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
# 4
# 3
# 2
# 0

# =====================================================================

n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)
# -1
# 0
# 1
# 2
# 3

# =====================================================================

for i in range(0, 6, 3):
    print(i)
# 0
# 3

# ======================================= Significado =================================================================

# O loop for executa um conjunto de declarações várias vezes; é usado para iterar sobre uma sequência (por exemplo,
# uma lista,
# um dicionário, um tuple, ou um conjunto - aprenderá sobre eles em breve) ou outros objetos que são iteráveis
# (por exemplo, strings).
# Pode utilizar o loop for para iterar sobre uma sequência de números usando a função range

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")  # POR DEFINIÇAO O (end='') junta com o proximo texto (sep='') serve para separar os
    # textos as strings separadas por virgula.

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

# ==================================================================================================================

# essa é a estrutura basica do for, o (c) esta representando uma variavel, pode ser qualquer nome. (1,10) = intervalo
# de 1 a 10.
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


# ========================================Crie um programa que mostre na tela todos os números pares que estão no
# intervalo entre 1 e 50. ===========================================================================================

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

# =========================================Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.======================================================

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



# ================================================================Refaça a tabuada, mostrando um número que o
# usuário escolher,# só que agora utilizando um laço for.===============================================================


# ==================================================== Desenvolva um programa que leia seis números inteiros e mostre a
# soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.==================================