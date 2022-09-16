# ====================================================== while (enquanto) =========================================================

# =========================================== Fazer loop ao seu código com while

# Concorda com a declaração apresentada abaixo?

while there is something to do
    do it

# Note-se que este registo também declara que se não houver nada a fazer, nada acontecerá.

# Em geral, em Python, um loop pode ser representado da seguinte forma:

while conditional_expression:
    instruction

# Se notar algumas semelhanças com a instrução if, não há problema. De facto, a diferença sintática é apenas uma:
# usa-se a palavra while em vez da palavra if.

# A diferença semântica é mais importante: quando a condição é cumprida, if executa as suas declarações apenas
# uma vez; while repete a execução enquanto a condição se avalie a True.

# Nota: todas as regras relativas à indentação são aplicáveis também aqui. Vamos mostrar-lhe isso em breve.

# Veja o algoritmo abaixo:

while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    :
    :
    instruction_n

# Agora é importante lembrar que:

# ===> se quiser executar mais do que uma declaração dentro de um while, deve (como com if) indentar todas as
#       instruções da mesma forma;
# ===> uma instrução ou conjunto de instruções executadas no interior do loop while é chamada corpo do loop;
# ===> se a condição é False (igual a zero) logo que é testada pela primeira vez, o corpo não é executado nem uma
#       vez (note-se a analogia de não ter de fazer nada se não houver nada a fazer);
# ===> o corpo deve ser capaz de alterar o valor da condição, porque se a condição estiver True no início, o
#       corpo pode correr continuamente até ao infinito - repare que fazer uma coisa normalmente diminui o número
#       de coisas a fazer).

# ========================================================= Um loop infinito

# Um loop infinito, também chamado endless loop, é uma sequência de instruções num programa que se repete
# indefinidamente (loop interminável).

# Eis um exemplo de um loop que não é capaz de terminar a sua execução:

while True:
    print("I'm stuck inside a loop.")

# Este loop será infinitamente imprimido === ("I'm stuck inside a loop.") === no ecrã.

NOTA

# Se quiser obter a melhor experiência de aprendizagem ao ver como se comporta um loop infinito, lance o IDLE, crie
# um New File, copie-cole o código acima, guarde o seu ficheiro, e execute o programa. O que irá ver é a sequência
# interminável de strings === ("I'm stuck inside a loop.") === impressas na janela da consola do Python. Para terminar o seu
# programa, basta premir Ctrl-C (ou Ctrl-Break em alguns computadores). Isto causará a chamada exceção
# ===(KeyboardInterrupt) === e deixa o seu programa sair do loop. Falaremos sobre isso mais tarde no curso.

# Voltemos ao esboço do algoritmo que lhe mostrámos recentemente. Vamos mostrar-lhe como utilizar este loop
# recentemente aprendido para encontrar o maior número a partir de um grande conjunto de dados introduzidos.

# Analise o programa com cuidado. Veja onde o loop começa (linha 8). Localize o corpo do loop e descubra como
# é que o corpo sai:

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

# Verifique como este código implementa o algoritmo que lhe mostrámos anteriormente.

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

# Certas expressões podem ser simplificadas sem alterar o comportamento do programa.

# Tente lembrar-se de como o Python interpreta a verdade de uma condição e observe que estas duas formas
# são equivalentes:
# while number != 0: e while number:.
# A condição que verifica se um número é ímpar também pode ser codificada nestas formas equivalentes:
# if number % 2 == 1: e if number % 2:.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)
# Enter a number or type 0 to stop: 10
# Enter a number or type 0 to stop: 20
# Enter a number or type 0 to stop: 30
# Enter a number or type 0 to stop: 20
# Enter a number or type 0 to stop: 10
# Enter a number or type 0 to stop: 50
# Enter a number or type 0 to stop: 1
# Enter a number or type 0 to stop: 6
# Enter a number or type 0 to stop: s
# Traceback (most recent call last):
#   File "main.py", line 21, in <module>
#     number = int(input("Enter a number or type 0 to stop: "))
# ValueError: invalid literal for int() with base 10: 's'

# =========================================================

# ======================================================= Usar uma variável counter para sair de um loop

# Veja o snippet abaixo:
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)
# Inside the loop. 5
# Inside the loop. 4
# Inside the loop. 3
# Inside the loop. 2
# Inside the loop. 1
# Outside the loop. 0

# Este código destina-se a imprimir a string "Inside the loop." e o valor armazenado na variável counter durante um
# determinado loop exatamente cinco vezes. Uma vez que a condição não foi atendida (a variável counter atingiu 0),
# o loop é encerrado, e a mensagem "Outside the loop." bem como o valor armazenado em counter é impresso.

# Mas há uma coisa que pode ser escrita de forma mais compacta - a condição do loop while .

# Consegue ver a diferença?

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)
# Inside the loop. 5
# Inside the loop. 4
# Inside the loop. 3
# Inside the loop. 2
# Inside the loop. 1
# Outside the loop. 0

# É mais compacto do que anteriormente? Um pouco. É mais legível? Isso é discutível.

# LEMBRE-SE

# Não se sinta obrigado a codificar os seus programas de uma forma que seja sempre a mais curta e a mais compacta.
# A legibilidade pode ser um fator mais importante. Mantenha o seu código preparado para um novo programador.

# =========================================================

# A sua tarefa é ajudar o mágico a completar o código no editor, de modo a que o código:

# ===> peça ao utilizador para introduzir um número inteiro;
# ===> utilize um loop while ;
# ===> verifique se o número introduzido pelo utilizador é o mesmo que o número escolhido pelo mágico. Se o número
# escolhido pelo utilizador for diferente do número secreto do mágico, o utilizador deve ver a mensagem "Ha ha!
# You're stuck in my loop!" e ser solicitado a introduzir novamente um número. Se o número introduzido pelo utilizador
# corresponder ao número escolhido pelo mágico, o número deve ser impresso no ecrã, e o mágico deve dizer as seguintes
# palavras: "Well done, muggle! You are free now."

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input("Enter the number: "))

while user_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_number = int(input("Enter the number again: "))
print(secret_number, "Well done, muggle! You are free now.")
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
#
# Enter the number: 50
# Ha ha! You're stuck in my loop!
# Enter the number again: 777
# 777 Well done, muggle! You are free now.

# =========================================================

# ================================================================= Os loops while e o ramo else .

# Ambos os loops, while e for, têm uma característica interessante (e raramente usada).
# Vamos mostrar-lhe como funciona - tente julgar por si próprio se é utilizável e se pode viver sem ela ou não.
# Por outras palavras, tente convencer-se se a característica é valiosa e útil, ou se é apenas açúcar sintático.
# Veja o snippet no editor. Há algo estranho no final - a keyword else .
# Como pode ter suspeitado, os loops podem ter o ramo else também, como if.
# O ramo do loop else é sempre executado uma vez, independentemente de o loop ter entrado no seu corpo ou não.
# Consegue adivinhar o output? Execute o programa para verificar se estava certo.
# Modifique um pouco o anippet para que o loop não tenha hipótese de executar o seu corpo nem mesmo uma vez:
#
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
# 1
# 2
# 3
# 4
# else: 5

