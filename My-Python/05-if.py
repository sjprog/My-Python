# ================================================== if ( se ) =========================================================

# ====================================== Condições e execução condicional

# Já sabe como fazer perguntas ao Python, mas ainda não sabe como fazer um uso razoável das respostas. Tem de ter um
# mecanismo que lhe permita fazer algo === (se uma condição for cumprida, e não o fazer se não o for.) ===

# É como na vida real: faz-se ou não certas coisas quando uma condição específica é cumprida ou não, por
# exemplo, vai-se passear se o tempo estiver bom, ou fica-se em casa se estiver a chover e a fazer frio.

# Para tomar tais decisões, o Python oferece uma instrução especial. Devido à sua natureza e à sua aplicação, chama-se
# === (instrução condicional) === (ou declaração condicional).

# Existem várias variantes da mesma. Vamos começar com a mais simples, aumentando a dificuldade lentamente.

# A primeira forma de uma declaração condicional, que pode ver abaixo, é escrita de forma muito informal mas figurativa:

if true_or_not:
    do_this_if_true

# Esta declaração condicional consiste nos seguintes elementos, estritamente necessários, apenas nesta e nesta ordem:

# ===> a keyword if ;
# ===> um ou mais espaços em branco;
# ===> uma expressão (uma pergunta ou uma resposta) cujo valor será interpretado unicamente em termos de True
#       (quando o seu valor é diferente de zero) e False (quando é igual a zero);
# ===> um dois pontos seguido de uma newline;
# ===> uma instrução indentada ou conjunto de instruções (pelo menos uma instrução é absolutamente necessária); a
#       indentação pode ser conseguida de duas maneiras - inserindo um determinado número de espaços (a recomendação
#       é utilizar quatro espaços de indentação), ou utilizando o caratere tab; nota: se houver mais de uma instrução
#       na parte indentada, a indentação deve ser a mesma em todas as linhas; mesmo que possa parecer a mesma se usar
#       tabs misturados com espaços, é importante fazer todas as indentações exatamente iguais - o Python 3 não permite
#       a mistura de espaços e tabs para indentação.

# ========= Como funciona essa declaração?
#
# Se a expressão true_or_not representa a verdade (ou seja, o seu valor não é igual a zero), a(s) declaração(ões)
# indentada(s) será(ão) executada(s);
# se a expressão true_or_not não representa a verdade (ou seja, o seu valor é igual a zero), a(s) declaração(ões)
# indentada(s) será(ão) omitida(s) (ignoradas), e a próxima instrução executada será a que se segue ao nível da
# indentação original.

# Na vida real, expressamos frequentemente um desejo:
# se o tempo estiver bom, vamos dar um passeio
# depois, vamos almoçar

# Como se pode ver, almoçar não é uma atividade condicional e não depende do tempo.

# Sabendo que condições influenciam o nosso comportamento, e assumindo que temos as funções sem parâmetros
# go_for_a_walk() e have_lunch(), podemos escrever o seguinte snippet:

if the_weather_is_good:
    go_for_a_walk()
have_lunch()

# ========================================== Execução condicional: a declaração if .

# Se um certo programador de Python insonioso acabar por adormecer enquanto conta 120 ovelhas, e se este procedimento
# de indução do sono pudesse ser implementado como uma função especial chamada sleep_and_dream(),
# todo o código assumiria a seguinte forma:

if sheep_counter >= 120: # Evaluate a test expression
    sleep_and_dream() # Execute if test expression is True

# Pode lê-lo como: se sheep_counter é maior que ou igual a 120, então, adormecer e sonhar
# (ou seja, executar a função sleep_and_dream .)

# Dissemos que as declarações executadas condicionalmente têm de ser indentadas. Isto cria uma estrutura muito legível,
# demonstrando claramente todos os caminhos de execução possíveis no código.

# Dê uma vista de olhos no seguinte código:

if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
feed_the_sheepdogs()

# Como pode ver, fazer a cama, tomar um banho, e adormecer e sonhar, são todos === (executados condicionalmente) === -
# quando se sheep_counter atinge o limite desejado.

# Alimentar os cães de ovelha, no entanto, é  ===(sempre feito)=== (ou seja, a função feed_the_sheepdogs() não é indentada
# e não pertence ao bloco if , o que significa que é sempre executada.)

# Agora, vamos discutir outra variante da declaração condicional, que também lhe permite executar uma ação adicional
# quando a condição não for cumprida.

# ============================================= Execução condicional: a declaração if-else .

# Começámos com uma frase simples, que diz: Se o tempo estiver bom, vamos dar um passeio.

# Nota - não há uma palavra sobre o que irá acontecer se o tempo estiver mau. Nós apenas sabemos que não vamos para
# o exterior, mas o que poderíamos fazer em vez disso não é conhecido. Podemos querer planear algo em caso de mau
# tempo, também.

# Podemos dizer, por exemplo: Se o tempo estiver bom, vamos dar uma caminhada, caso contrário, vamos a um teatro.

# Agora sabemos o que iremos fazer se as condições forem cumpridas, e sabemos o que iremos fazer se nem tudo correr
# à nossa maneira. Por outras palavras, temos um “Plano B”.

# O Python permite-nos expressar estes planos alternativos. Isto é feito com uma segunda forma, ligeiramente mais
# complexa, da declaração condicional, a declaração if-else:

if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false

# Assim, há uma nova palavra: else - Esta é uma keyword.

# A parte do código que começa com else diz o que fazer se a condição especificada para o if não for cumprida
# (observe os dois pontos após a palavra).

# A execução if-else é feita da seguinte forma:

# ===> se a condição for avaliada comoTrue (o seu valor não é igual a zero), a declaração perform_if_condition_true é
# executada, e a declaração condicional chega ao fim;
# ===> se a condição for avaliada como False (o seu valor é igual a zero), a declaração perform_if_condition_false é
# executada, e a declaração condicional chega ao fim.

# ===================================== A declaração if-else : execução mais condicional ===============================

# Ao utilizar esta forma de declaração condicional, podemos descrever os nossos planos da seguinte forma:

if the_weather_is_good:
    go_for_a_walk()
else:
    go_to_a_theater()
have_lunch()

# Se o tempo estiver bom, vamos dar uma volta. Caso contrário, iremos a uma peça de teatro. Não importa se o
# tempo estiver bom ou mau, almoçaremos depois (depois do passeio ou depois de irmos ao teatro).

# Tudo o que dissemos sobre a indentação funciona da mesma forma dentro do ramo else:

if the_weather_is_good:
    go_for_a_walk()
    have_fun()
else:
    go_to_a_theater()
    enjoy_the_movie()
have_lunch()

# ========================================== Declarações if-else nested

# Agora vamos discutir dois casos especiais da declaração condicional.
# Primeiro, considere o caso em que a instrução colocada após a if é outra if.

# Leia o que temos planeado para este domingo. Se o tempo estiver bom, vamos dar uma volta. Se encontrarmos um bom
# restaurante, almoçaremos lá. Caso contrário, comemos uma sandes. Se o tempo estiver mau, vamos ao teatro. Se não
# houver bilhetes, iremos às compras no centro comercial mais próximo.

# Vamos escrever o mesmo em Python. Considere cuidadosamente o código aqui:

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

# =========================================== Aqui estão dois pontos importantes:

# ===> este uso da declaração if é conhecido como nesting; lembre-se que cada else refere-se ao if que se situa ao mesmo
#        nível de indentação; é preciso saber isto para determinar como os ifs e elses se emparelham;
# ===> considere como a indentação melhora a legibilidade, e torna o código mais fácil de compreender e rastrear.


# ============================================== A declaração elif .


# O segundo caso especial introduz outra nova keyword de Python: elif. Como provavelmente suspeitará, é uma
# forma mais curta de else if.

elif # é usado para verificar mais do que uma condição, e para parar quando a primeira afirmação que é verdadeira
# é encontrada.

# O nosso próximo exemplo assemelha-se a nesting, mas as semelhanças são muito ligeiras. Mais uma vez, vamos mudar
# os nossos planos e expressá-los como se segue: Se o tempo estiver bom, iremos dar um passeio, caso contrário, se
# conseguirmos bilhetes, iremos ao teatro, caso contrário, se houver mesas livres no restaurante, iremos almoçar; se
# tudo o resto falhar, regressaremos a casa e jogaremos xadrez.

# Já reparou quantas vezes utilizámos as palavras caso contrário? Esta é a fase em que a keyword elif desempenha o
# seu papel.

# Vamos escrever o mesmo cenário usando Python:

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

# A forma de reunir as declarações subsequentes if-elif-else é por vezes chamada de cascade (cascata).
# Repare novamente como a indentação melhora a legibilidade do código.

# Neste caso, deve ser dada alguma atenção adicional:

# ===> não deve usar else sem um precedente if;
# ===> else é sempre o último ramo da cascade, independentemente de ter utilizado elif ou não;
# ===> else é uma parte opcional da cascade, e pode ser omitida;
# ===> se houver um else ramo na cascade, apenas um de todos os ramos é executado;
# ===> se não houver nenhum else ramo, é possível que nenhuma das ramificações disponíveis seja executada.

# Isto pode parecer um pouco confuso, mas esperemos que alguns exemplos simples ajudem a lançar mais luz.

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# =========================================== Exemplo 01

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)
# Enter the first number: 10
# Enter the second number: 20
# The larger number is: 20

# =========================================== Exemplo 02

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)
# Enter the first number: 10
# Enter the second number: 0
# The larger number is: 10

# =========================================== Exemplo 03

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)
# Enter the first number: 10
# Enter the second number: 20
# Enter the third number: 30
# The largest number is: 30

# =====================================================

# =========================================== Pseudo-código e introdução aos loops

# Deverá agora ser capaz de escrever um programa que encontre o maior de quatro, cinco, seis, ou mesmo dez números.
# Já conhece o esquema, pelo que alargar a dimensão do problema não será particularmente complexo.
# Mas o que acontece se lhe pedirmos para escrever um programa que encontre o maior de duzentos números?
# Consegue imaginar o código?

# Vai precisar de duzentas variáveis. Se duzentas variáveis não for suficientemente mau, tente imaginar a procura
# do maior de um milhão de números.

# Imagine um código que contém 199 declarações condicionais e duzentas invocações da função input() . Felizmente,
# não precisa de lidar com isso. Há uma abordagem mais simples.

# Vamos ignorar os requisitos da sintaxe Python por agora, e tentar analisar o problema sem pensar na programação
# real. Por outras palavras, vamos tentar escrever o algoritmo, e quando estivermos satisfeitos com ele, vamos
# implementá-lo.

# Neste caso, utilizaremos uma espécie de notação que não é uma linguagem de programação real (não pode ser
# compilada nem executada), mas que é formalizada, concisa e legível. Chama-se pseudo-código.

# Vejamos o nosso pseudo-código abaixo:

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02

# O que está a acontecer nele?

# Em primeiro lugar, podemos simplificar o programa se, logo no início do código, atribuirmos a variável
# largest_number com um valor que será menor do que qualquer um dos números introduzidos. Vamos usar
# -999999999 para esse fim.

# Em segundo lugar, assumimos que o nosso algoritmo não saberá antecipadamente quantos números serão entregues
# ao programa. Esperamos que o utilizador introduza quantos números quiser - o algoritmo funcionará bem com cem
# e com mil números. Como é que fazemos isso?

# Fazemos um acordo com o utilizador: quando o valor -1 é introduzido, será um sinal de que não há mais dados e
# que o programa deve terminar o seu trabalho.

# Caso contrário, se o valor introduzido não for igual a -1, o programa irá ler outro número, e assim por diante.

# O truque baseia-se no pressuposto de que qualquer parte do código pode ser executada mais do que uma vez -
# precisamente, tantas vezes quantas forem necessárias.

# A execução de uma determinada parte do código mais do que uma vez é chamada um loop. O significado deste
# termo é provavelmente óbvio para si.

# Linhas 02 através 08 fazem um loop. Passaremos por eles tantas vezes quantas forem necessárias para rever todos
# os valores introduzidos.

# Pode usar uma estrutura semelhante num programa escrito em Python? Sim, pode.

# Informação Extra

# O Python vem muitas vezes com muitas funções incorporadas que farão o trabalho por si. Por exemplo,
# para encontrar o maior número de todos, pode usar uma função integrada Python chamada max(). Pode utilizá-la com
# múltiplos argumentos. Analise o código abaixo:

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)

# Da mesma forma, pode usar a função min() para devolver o menor número. Pode reconstruir o código acima e fazer
# experiências com ele na Sandbox.

# Vamos falar sobre estas (e muitas outras) funções em breve. Por enquanto, o nosso foco será colocado na execução
# condicional e nos loops para lhe permitir ganhar mais confiança na programação e ensinar-lhe as competências que
# lhe permitirão compreender e aplicar plenamente os dois conceitos no seu código. Portanto, por agora, não vamos
# por atalhos.

# Da mesma forma, pode usar a função min() para devolver o menor número.

# =====================================================

# Escreve um programa que utilize o conceito de execução condicional, toma uma string como entrada, e:

#       imprime a frase "Yes - Spathiphyllum is the best plant ever!" para o ecrã, se a cadeia de caracteres inseridos
#           é "Spathiphyllum" (upper-case)
#       Impressões "No, I want a big Spathiphyllum!" se a cadeia de caracteres inseridos é "spathiphyllum" (lower-case)
#       Impressões "Spathiphyllum! Not [input]!" caso contrário. Nota: [input] é a string tomada como input.

name = input("Enter flower name: ")

if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")
# Enter flower name: Sidney
# Spathiphyllum! Not Sidney!

# =====================================================

# A sua tarefa é escrever uma calculadora de impostos.

# ===> Deve aceitar um valor de floating-point: o rendimento.
# ===> A seguir, deve imprimir o imposto calculado, arredondado a thalers completos. Há uma função chamada round()
# que lhe fará o arredondamento por si - encontrá-la-á no código esqueleto no editor.
# Nota: este país feliz nunca devolve dinheiro aos seus cidadãos. Se o imposto calculado for inferior a zero,
# significa apenas que não há qualquer imposto (o imposto é igual a zero). Tenha isto em consideração durante
# os seus cálculos.

# Veja o código no editor - lê apenas um valor de input e faz output de um resultado, pelo que necessita de o
# completar com alguns cálculos inteligentes.

income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
# Enter the annual income: 10000
# The tax is: 1244.0 thalers

# =====================================================

# Como certamente sabe, devido a algumas razões astronómicas, os anos podem ser bissextos ou comuns.
# Os primeiros têm 366 dias de duração, enquanto os segundos têm 365 dias de duração.

# Desde a introdução do calendário gregoriano (em 1582), a seguinte regra é utilizada para determinar o tipo de ano:

# ==> se o número do ano não for divisível por quatro, é um ano comum;
# ==> caso contrário, se o número do ano não for divisível por 100, é um ano bissexto;
# ==> caso contrário, se o número do ano não for divisível por 400, é um ano comum;
# ==> caso contrário, é um ano bissexto.

# Veja o código no editor - lê apenas um número de ano, e precisa de ser completado com as instruções de implementação
# do teste que acabámos de descrever.

# O código deve fazer output de uma de duas mensagens possíveis, que são Leap year ou Common year, dependendo do
# valor inserido.

# Seria bom verificar se o ano introduzido cai na era Gregoriana, e faz output de um aviso caso contrário: Not
# within the Gregorian calendar period. Dica: use os operadores != e % .

year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")
# Enter a year: 2000
# Leap year

# ===================================================== Resumo =========================================================

# 1. Os operadores de comparação (ou os chamados relacionais) são usados para comparar valores. A tabela abaixo
# ilustra como os operadores de comparação funcionam, assumindo que x = 0, y = 1, e z = 0:

Operador	                                    Descrição	                                          Exemplo
   ==	         retorna se os valores dos operandos forem iguais, eFalse caso contrário
                                                                                                       x == y  # False
                                                                                                       x == z  # True

   !=	       retorna Truese os valores dos operandos não forem iguais, eFalse caso contrário
                                                                                                       x != y  # True
                                                                                                       x != z  # False

   >	                 Truese o valor do operando esquerdo for maior que o
                    valor do operando direito, eFalse caso contrário
                                                                                                       x > y  # False
                                                                                                       y > z  # True

   <	                 Truese o valor do operando esquerdo for inferior ao
                    valor do operando direito, eFalse caso contrário
                                                                                                       x < y  # True
                                                                                                       y < z  # False

   ≥	                 Truese o valor do operando esquerdo for maior ou
                    igual ao valor do operando direito, eFalse caso contrário
                                                                                                       x >= y  # False
                                                                                                       x >= z  # True
                                                                                                       y >= z  # True

   ≤	                 Truese o valor do operando esquerdo for inferior
                    ou igual ao valor do operando direito, eFalse caso contrário
                                                                                                       x <= y  # True
                                                                                                       x <= z  # True
                                                                                                       y <= z  # False

# 2. Quando quiser executar algum código apenas se uma determinada condição for cumprida, pode usar uma declaração
# condicional:

# ===> uma únicaif declaração, por exemplo:

x = 10
if x == 10: # condition
    print("x is equal to 10")  # Executed if the condition is True.

# ===> uma série de if declarações, por exemplo:

x = 10
if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.
if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.
if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.

#  Cada if declaração é testada separadamente.

# ===> uma if-elsedeclaração, por exemplo:

x = 10
if x < 10:  # Condition
    print("x is less than 10")  # Executed if the condition is True.
else:
    print("x is greater than or equal to 10")  # Executed if the condition is False.

# ===> uma série de if declarações seguidas por um else, por exemplo:

x = 10

if x > 5:  # True
    print("x > 5")
if x > 8:  # True
     print("x > 8")

if x > 10:  # False
    print("x > 10")
else:
    print("else will be executed")

# Cada if é testado separadamente. O corpo de else é executado se o último if for False.

# ===> A if-elif-elsedeclaração, por exemplo:

x = 10
if x == 10:  # True
    print("x == 10")
if x > 15:  # False
    print("x > 15")
elif x > 10:  # False
    print("x > 10")
elif x > 5:  # True
    print("x > 5")
else:
    print("else will not be executed")

# Se a condição if for False, o programa verifica as condições dos elif blocos subsequentes - o
# primeiro elif bloco que True é executado. Se todas as condições forem False, o else bloco será executado.

# ===> Declarações condicionais nested, por exemplo:

x = 10
if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")

# =====================================================

x = 5
y = 10
z = 8

print(x > y)
print(y > z)
# False
# True

# =====================================================

x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)
# False
# True

# =====================================================

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)
# True
# False

# =====================================================

x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")
# True
# True
# else

# =====================================================

x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")
# four
# five

# =====================================================

x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")
# one
# two

# =====================================================
