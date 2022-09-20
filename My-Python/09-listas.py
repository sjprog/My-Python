# ================================================== LISTAS ===========================================================

# Pode acontecer que tenha de ler, armazenar, processar e, finalmente, imprimir dezenas, talvez centenas,
# talvez até milhares de números. E então, o quê? É necessário criar uma variável em separado para cada valor?
# É necessário passar várias horas a escrever declarações como as abaixo?

var1 = int(input())
var2 = int(input())
var3 = int(input())
var4 = int(input())
var5 = int(input())
var6 = int(input())
:
:

# Se pensa que esta não é uma tarefa complicada, então pegue num pedaço de papel e escreva um programa que:

===> leia cinco números,
===> que os imprima por ordem do mais pequeno ao maior (este tipo de processamento chama-se triagem).

# Deve chegar à conclusão de que não tem sequer papel suficiente para completar a tarefa.

# Até agora, aprendeu a declarar variáveis que são capazes de armazenar exatamente um determinado valor de cada vez.
# Tais variáveis são por vezes chamadas escalares, por analogia com a matemática. Todas as variáveis que utilizou até
# agora são, na verdade, escalares.

# Pense no quão conveniente seria declarar uma variável que pudesse armazenar mais do que um valor. Por exemplo, cem,
# ou mil, ou até dez mil. Seria ainda uma e a mesma variável, mas muito ampla e espaçosa. Parece apelativa? Talvez, mas
# como lidaria com um recipiente cheio de valores diferentes? Como escolheria apenas aquele de que necessita?

# E se pudesse simplesmente numerá-los? E depois dizer: dá-me o valor número 2; atribui o valor número 15; aumenta
# o valor número 10000.

# Vamos mostrar-lhe como declarar tais variáveis multi-valores. Vamos fazer isto com o exemplo que acabámos de sugerir.
# Vamos escrever um programa que ordena uma sequência de números. Não seremos particularmente ambiciosos - vamos
# assumir que existem exatamente cinco números.

# Vamos criar uma variável chamada numbers; é atribuída não apenas com um número, mas é preenchida com uma lista
# constituída por cinco valores (nota: a lista começa com um parêntesis reto aberto e termina com um parêntesis reto
# fechado; o espaço entre os parêntesis é preenchido com cinco números separados por vírgulas).

numbers = [10, 5, 7, 2, 1]

# Digamos a mesma coisa usando terminologia adequada: numbers é uma lista constituída por cinco valores, todos
# eles números. Podemos também dizer que esta declaração cria uma lista de comprimento igual a cinco (visto existir
# cinco elementos no seu interior).

# Os elementos dentro de uma lista podem ter tipos diferentes. Alguns deles podem ser inteiros, outros floats,
# e outros ainda podem ser listas.

# O Python adotou uma convenção, afirmando que os elementos numa lista são sempre numerados a partir do zero.
# Isto significa que o artigo armazenado no início da lista terá o número zero. Uma vez que existem cinco elementos na
# nossa lista, ao último deles é atribuído o número quatro. Não esqueça isto.

# Rapidamente se acostumará a isto, e tornar-se-á uma segunda natureza.

# Antes de avançarmos na nossa discussão, temos de referir o seguinte: a nossa lista é uma coleção de elementos,
# mas cada elemento é um escalar.

# ============================================================== Indexar listas

# Como se altera o valor de um elemento escolhido na lista?

# Vamos atribuir um novo valor de 111 ao primeiro elemento na lista. Fazemo-lo assim:

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content: ", numbers)  # Current list content.

# E agora queremos que o valor do quinto elemento seja copiado para o segundo elemento - consegue adivinhar como o fazer?

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content:", numbers)  # Printing current list content.


# O valor dentro dos parêntesis que seleciona um elemento da lista é chamado um index, enquanto a operação de
# selecionar um elemento da lista é conhecida como indexing (indexação).

# Vamos utilizar a função print() para imprimir o conteúdo da lista cada vez que fazemos as alterações. Isto
# ajudar-nos-á a seguir cada passo com mais cuidado e a ver o que se passa após uma determinada modificação da lista.

# Nota: todos os índices usados até agora são literais. Os seus valores são fixados em runtime, mas qualquer
# expressão também pode ser o index. Isto oferece muitas possibilidades.

#  =======================================================================

numbers = [10, 5, 7, 2, 1]
print("List content:", numbers)  # Printing original list content.
# List content: [10, 5, 7, 2, 1]

#  =======================================================================

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content:", numbers)  # Printing current list content.
# Original list content: [10, 5, 7, 2, 1]
#
# Previous list content: [111, 5, 7, 2, 1]
# New list content: [111, 1, 7, 2, 1]

#  =======================================================================

# Aceder ao conteúdo da lista
# Cada um dos elementos da lista pode ser acedido separadamente. Por exemplo, pode ser impresso:

print(numbers[0]) # Accessing the list's first element.

# Assumindo que todas as operações anteriores tenham sido concluídas com sucesso, o snippet enviará 111 para a consola.

# Como pode ver no editor, a lista também pode ser impressa como um todo - tal como aqui:

print(numbers)  # Printing the whole list.

# Como provavelmente já notou antes, o Python decora o output de uma forma que sugere que todos os valores
# apresentados formam uma lista. O output do exemplo acima é o seguinte:

[111, 1, 7, 2, 1]


# ==================================================================== O método len() .

# O comprimento de uma lista pode variar durante a execução. Novos elementos podem ser acrescentados à lista, enquanto
# outros podem ser retirados da mesma. Isto significa que a lista é uma entidade muito dinâmica.

# Se quiser verificar o comprimento atual da lista, pode usar uma função chamada len() (o seu nome vem de length
# (comprimento)).

# A função toma o nome da lista como argumento, e devolve o número de elementos atualmente armazenados
# dentro da lista (por outras palavras - o comprimento da lista).

# Veja a última linha de código no editor, execute o programa e verifique que valor irá imprimir para a consola.
# Consegue adivinhar?

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList length:", len(numbers))  # Printing the list's length.
# Original list content: [10, 5, 7, 2, 1]
#
# Previous list content: [111, 5, 7, 2, 1]
# Previous list content: [111, 1, 7, 2, 1]
#
# List length: 5

# ==========================================================Remover elementos de uma lista

# Qualquer elemento da lista pode ser removido a qualquer momento - isto é feito com uma instrução chamada del
# (delete). Nota: é uma instrução, não uma função.

# É preciso apontar o elemento a ser removido - desaparecerá da lista, e o comprimento da lista será reduzido em um.

# Olhe para o snippet abaixo. Consegue adivinhar que output irá produzir? Execute o programa no editor e verifique.

del numbers[1]
print(len(numbers))
print(numbers)

# Não se pode aceder a um elemento que não existe - não se pode obter o seu valor nem atribuir-lhe um valor.
# Ambas estas instruções irão agora causar erros de runtime:

print(numbers[4])
numbers[4] = 1

# Adicione o snippet acima após a última linha de código no editor, execute o programa e verifique o que acontece.

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###
# Original list content: [10, 5, 7, 2, 1]
#
# Previous list content: [111, 5, 7, 2, 1]
# Previous list content: [111, 1, 7, 2, 1]
#
# List's length: 5
# New list's length: 4
#
# New list content: [111, 7, 2, 1]

# =========================================================== Índices negativos são legais

# Pode parecer estranho, mas os índices negativos são legais, e podem ser muito úteis.
# Um elemento com um index igual a -1 é o último na lista.

print(numbers[-1])

# O snippet de exemplo terá como output 1. Execute o programa e verifique.

# Da mesma forma, o elemento com um index igual a -2 é o penúltimo na lista.

print(numbers[-2])

# O snippet de exemplo terá como output 2.

# O último elemento acessível da nossa lista é numbers[-4] (o primeiro) - não tente ir mais longe!

numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])
# 1
# 2

# =====================================================================

# A tarefa é:

# escrever uma linha de código que peça ao utilizador para substituir o número médio na lista por um número
#   inteiro introduzido pelo utilizador (Passo 1)
# escrever uma linha de código que remova o último elemento da lista (Passo 2)
# escrever uma linha de código que imprima o comprimento da lista existente (Passo 3).

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)
# [1, 2, 3, 4, 5]

# =================================================================== Funções vs. métodos

# Um método é um tipo específico de função - comporta-se como uma função e parece uma função, mas difere na forma
# como atua, e no seu estilo de invocação.

# Uma função não pertence a nenhum dado - recebe dados, pode criar novos dados e (geralmente) produz um resultado.

# Um método faz todas estas coisas, mas também é capaz de alterar o estado de uma entidade selecionada.

# Um método é propriedade dos dados para os quais trabalha, enquanto uma função é propriedade de todo o código.

# Isto também significa que a invocação de um método requer alguma especificação dos dados a partir dos quais o
# método é invocado.

# Pode parecer intrigante aqui, mas lidaremos com isso em profundidade quando nos aprofundarmos na programação
# orientada ao objeto.

# Em geral, uma invocação de função típica pode parecer-se com isto:

result = function(arg)

# A função toma um argumento, faz algo, e devolve um resultado.

# Um método típico de invocação é geralmente semelhante a este:

result = data.method(arg)

# Nota: o nome do método é precedido do nome dos dados que possuem o método. Em seguida, adiciona-se um ponto, seguido
# do nome do método, e um par de parêntesis que encerra os argumentos.

# O método comportar-se-á como uma função, mas pode fazer algo mais - pode alterar o estado interno dos dados a
# partir dos quais foi invocado.

# Pode perguntar: porque estamos a falar de métodos e não de listas?

# Esta é uma questão essencial neste momento, pois vamos mostrar-lhe como adicionar novos elementos a uma lista
# existente. Isto pode ser feito com métodos pertencentes a todas as listas, e não por funções.


# =============================================================== Adicionar elementos a uma lista: append() e insert()

# Um novo elemento pode ser colado no fim da lista existente:

list.append(value)

# Tal operação é realizada por um método chamado append(). Toma o valor do seu argumento e coloca-o no final da
# lista que possui o método.

# O comprimento da lista aumenta então em um.

# O método insert() é um pouco mais inteligente - pode acrescentar um novo elemento em qualquer lugar da
# lista, e não apenas no final.

list.insert(location, value)


# São necessários dois argumentos:

# ===> o primeiro mostra a localização necessária do elemento a ser inserido; nota: todos os elementos
#   existentes que ocupam locais à direita do novo elemento (incluindo o que se encontra na posição indicada)
#   são deslocados para a direita, a fim de criar espaço para o novo elemento;
# ===> o segundo é o elemento a ser inserido.

# Veja o código no editor. Veja como utilizamos os append() e insert() métodos. Preste atenção ao que acontece após
# a utilização insert(): o primeiro elemento é agora o segundo, o segundo o terceiro, e assim por diante.
# Adicione o seguinte snippet após a última linha de código no editor:

numbers.insert(1, 333)

# =================================================================
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
# 4
# [111, 7, 2, 1]
# 5
# [111, 7, 2, 1, 4]
# 6
# [222, 111, 7, 2, 1, 4]

# ==========================================================================

# =====================================================================Adicionar elementos a uma lista: continuação

# Pode iniciar a vida de uma lista tornando-a vazia (isto é feito com um par de parêntesis retos vazio) e depois
# adicionando-lhe novos elementos conforme necessário.

# Veja o snippet no editor. Tente adivinhar o seu output após a execução do loop for . Execute o programa para
# verificar se estava certo.

# Será uma sequência de números inteiros consecutivos a partir de 1 (depois adiciona-se um a todos os valores
# anexados) até 5.

# Modificámos um pouco o snippet:

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

# O que acontecerá agora? Execute o programa e verifique se desta vez também estava certo.

# Deve obter a mesma sequência, mas em ordem inversa (este é o mérito de usar o método insert() ).

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)
# [1, 2, 3, 4, 5]

#  =========================================================================

# ============================================================================Utilização de listas

# O loop for tem uma variante muito especial que pode processar listas muito eficazmente - vejamos isso.

# Vamos supor que deseja calcular a soma de todos os valores armazenados na lista my_list .

# É necessária uma variável cuja soma será armazenada e à qual será inicialmente atribuído um valor de 0 - o seu
# nome será total. (Nota: não vamos nomeá-la sum visto o Python usar o mesmo nome para uma das suas funções internas
# - sum(). Utilizar o mesmo nome seria geralmente considerado uma má prática). Em seguida, acrescenta-lhe todos
# os elementos da lista utilizando o loop for . Veja o snippet no editor.

# Vamos comentar este exemplo:

# à lista é atribuída uma sequência de cinco valores inteiros;
# a variável i toma os valores 0, 1, 2, 3, e 4, e depois indexa a lista, selecionando os elementos seguintes: o
# primeiro, o segundo, o terceiro, o quarto e o quinto;
# cada um destes elementos é adicionado em conjunto pelo operador += à variável total , dando o resultado final
# no fim do loop;
# observe a forma como a função len() foi utilizada - torna o código independente de quaisquer possíveis alterações
# no conteúdo da lista.

# A segunda face do loop for .
# Mas o loop for pode fazer muito mais. Pode ocultar todas as ações ligadas à indexação da lista, e entregar
# todos os elementos da lista de uma forma prática.

# Este snippet modificado mostra como isto funciona:

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

# O que acontece aqui?

# ===> a instrução for especifica a variável usada para navegar na lista (i aqui) seguida pela keyword in e pelo nome
# da lista que está a ser processada (my_list aqui)
# ===> à variável i são atribuídos os valores de todos os elementos da lista subsequente, e o processo ocorre tantas
# vezes quantos os elementos da lista;
# ===> isto significa que se utiliza a variável i como uma cópia dos valores dos elementos, e não se precisa de utilizar
# índices;
# ===> a função len() também não é necessária aqui.

#  ==================================================================================

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
# 27

#  ==================================================================================

# ========================================================================= Listas em ação

# Deixemos as listas de lado por um breve momento e vejamos uma questão intrigante.

# Imagine que precisa de reorganizar os elementos de uma lista, ou seja, inverter a ordem dos elementos: o
# primeiro e o quinto, bem como o segundo e o quarto elementos serão trocados. O terceiro permanecerá intocado.

# Pergunta: como se pode trocar os valores de duas variáveis?

# Veja o snippet:

variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2

# Se fizer algo como isto, perderá o valor previamente armazenado em variable_2. Alterar a ordem das atribuições
# não ajudará. É necessária uma terceira variável que sirva como armazenamento auxiliar.

# É assim que se pode fazer:

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary


# O Python oferece uma forma mais conveniente de fazer a troca - veja:

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

# ==================================================================================Listas em ação

# Agora pode facilmente trocar os elementos da lista para inverter a sua ordem:

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Execute o snippet. O seu output deve ter este aspeto:

[5, 3, 8, 1, 10]

# Fica bem com cinco elementos.

# Será ainda aceitável com uma lista contendo 100 elementos? Não, não será.

# Pode utilizar o loop for para fazer a mesma coisa automaticamente, independentemente do comprimento da lista?
# Sim, pode.

# Foi assim que o fizemos:
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
# [5, 3, 8, 1, 10]

# Nota:

# ===> nós atribuímos a variável length com o comprimento da lista atual (isto torna o nosso código um pouco mais
#   claro e mais curto)
# ===> lançámos o loop for para correr através do seu corpo length // 2 vezes (isto funciona bem para listas com
#   comprimentos pares e ímpares, porque quando a lista contém um número ímpar de elementos, o do meio permanece intocado)
# ===> trocamos o i-ésimo elemento (desde o início da lista) com o que tem um index igual a (length - i - 1)
#   (do final da lista); no nosso exemplo, para i igual a 0 o ramo (lenght - i - 1) dá 4; para i igual a 1, dá
#   3 - Isto é exatamente o que precisávamos.

# ============================================================================================

# Escreva um programa que reflita estas mudanças e lhe permita praticar com o conceito de listas. A sua tarefa é:

# passo 1: criar uma lista vazia com o nome beatles;
# passo 2: utilizar o método append() para adicionar os seguintes membros da banda à lista: John Lennon,
#   Paul McCartney, e George Harrison;
# passo 3: utilizar o loop for e o método append() para solicitar ao utilizador que adicione os seguintes
#   membros da banda à lista: Stu Sutcliffe, e Pete Best;
# passo 4: utilizar a instrução del para remover Stu Sutcliffe e Pete Best da lista;
# passo 5: utilizar o método insert() para adicionar Ringo Starr ao início da lista.

# step 1:
Beatles = []
print("Step 1:", Beatles)

# step 2:

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Step 2:", Beatles)

# step 3:
for members in range(2):
    Beatles.append(input("New band member: "))
print("Step 3:", Beatles)

# step 4:
del Beatles[-1]
del Beatles[-1]
print("Step 4:", Beatles)

# step 5:
Beatles.insert(0, "RingoStarr")
print("Step 5:", Beatles)
print("The Fab:",len(Beatles))
# Step 1: []
# Step 2: ['John Lennon', 'Paul McCartney', 'George Harrison']
# New band member: sidney
# New band member: siqueira
# Step 3: ['John Lennon', 'Paul McCartney', 'George Harrison', 'sidney', 'siqueira']
# Step 4: ['John Lennon', 'Paul McCartney', 'George Harrison']
# Step 5: ['RingoStarr', 'John Lennon', 'Paul McCartney', 'George Harrison']

# ============================================================ RESUMO =================================================

# 1. A lista é um tipo de dados em Python usada para armazenar vários objetos. É uma coleção ordenada e mutável
# de ítens separados por vírgulas, entre parêntesis retos, por exemplo:

my_list = [1, None, True, "I am a string", 256, 0]

# 2. As listas podem ser indexadas e atualizadas, por exemplo:

my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0

my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

# 3. As listas podem ser nested, por exemplo:

my_list = [1, 'a', ["list", 64, [0, 1], False]]

# Aprenderá mais sobre o nesting no módulo 3.1.7 - por enquanto, só queremos que esteja ciente de que algo como
# isto também é possível.

# 4. Os elementos da lista e as listas podem ser excluídos, por exemplo:

my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list  # deletes the whole list

# Novamente, aprenderá mais sobre isto no módulo 3.1.6 - não se preocupe. Por enquanto, basta tentar experimentar o
# código acima e verificar como a sua alteração afeta o output.

# 5. As listas podem ser iteradas através da utilização do loop for , por exemplo:

my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color)

# 6. A função len() pode ser usada para verificar o comprimento da lista, por exemplo:

my_list = ["white", "purple", "blue", "yellow", "green"]
print(len(my_list))  # outputs 5

del my_list[2]
print(len(my_list))  # outputs 4

# 7. Uma invocação de função típica parece-se com a seguinte: result = function(arg), enquanto uma invocação de
# método típica parece-se com isto:result = data.method(arg).

#  ============================================================================

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)
# [6, 2, 3, 4, 5, 1]

#  ============================================================================

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)
# [1, 3, 6, 10, 15]

#  ============================================================================

lst = []
del lst
print(lst)
# NameError: name 'lst' is not defined

#  ============================================================================

lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
# [2, 3]
# 3

#  ============================================================================

# ================================================================================O bubble sort

# Agora que pode efetivamente fazer malabarismos com os elementos das listas, é tempo de aprender a ordená-los.
# Muitos algoritmos de ordenação foram inventados até agora, que diferem muito na velocidade, bem como na complexidade.
# Vamos mostrar-lhe um algoritmo muito simples, fácil de compreender, mas infelizmente também não muito eficiente.
# É utilizado muito raramente, e certamente não para listas grandes e extensas.

# Digamos que uma lista pode ser ordenada de duas maneiras:

# ===> crescente (ou mais precisamente - não decrescente) - se em cada par de elementos adjacentes, o primeiro elemento
# não for maior do que o segundo;
# ===> decrescente (ou mais precisamente - não crescente) - se em cada par de elementos adjacentes, o primeiro elemento
# não for inferior ao segundo.

# Nas secções seguintes, ordenaremos a lista por ordem crescente, de modo a que os números sejam ordenados do
# mais pequeno para o maior.

# Aqui está a lista:

 8 10 6 2 4
# Tentaremos usar a seguinte abordagem: tomaremos o primeiro e o segundo elementos e compará-los-emos; se determinarmos
# que estão na ordem errada (ou seja, o primeiro é maior que o segundo), trocá-los-emos; se a sua ordem for válida, não
# faremos nada. Um olhar sobre a nossa lista confirma esta última - os elementos 01 e 02 estão na ordem correta, como
# em 8 < 10.

# Agora olhe para o segundo e o terceiro elementos. Estão nas posições erradas. Temos de os trocar:

 8 6 10 2 4 # 6 E 10

# Vamos mais longe, e olhemos para o terceiro e quarto elementos. Novamente, não é assim que deveria ser. Temos
# de os trocar:

 8 6 2 10 4  # 2 E 10

# Agora verificamos o quarto e o quinto elementos. Sim, eles também estão nas posições erradas. Outra troca ocorre:

 8 6 2 4 10 # 4 E 10

# A primeira passagem pela lista já está terminada. Ainda estamos longe de terminar o nosso trabalho, mas algo
# de curioso aconteceu entretanto. O maior elemento, 10, já foi para o final da lista. Note-se que este é o lugar
# desejado para ele. Todos os elementos restantes formam uma confusão pitoresca, mas este já está no lugar

# Agora, por um momento, tente imaginar a lista de uma forma ligeiramente diferente - nomeadamente, assim:

# 10
# 4
# 2
# 6
# 8

# Olhe - 10 está no topo. Poderíamos dizer que flutuou do fundo para a superfície, tal como a bolha numa taça de
# champanhe. O método de classificação deriva o seu nome da mesma observação - chama-se um bubble sort
# (uma espécie de bolha).

# Agora começamos com a segunda passagem através da lista. Olhamos para o primeiro e segundo elementos - é
# necessária uma troca:

 6 8 2 4 10 # 6 E 8

# Tempo para o segundo e terceiro elementos: temos de os trocar também:

 6 2 8 4 10 # 2 e 8

# Agora o terceiro e quarto elementos, e a segunda passagem está terminada, visto 8 já estar no lugar:

 6 2 4 8 10 # 4 e 8

# Começamos a próxima passagem imediatamente. Observe cuidadosamente o primeiro e o segundo elementos - é necessária
# outra troca:

 2 6 4 8 10 # 2 e 6

# Agora 6 precisa de ser posto no lugar. Trocamos o segundo e o terceiro elementos:

 2 4 6 8 10 # 4 e 6

# A lista já está ordenada. Não temos mais nada a fazer. Isto é exatamente o que queremos.

# Como pode ver, a essência deste algoritmo é simples: comparamos os elementos adjacentes e, trocando alguns
# deles, atingimos o nosso objetivo

# =============================================================================Classificar uma lista

# Quantas passagens precisamos para ordenar a lista completa?

# Resolvemos esta questão da seguinte forma: introduzimos outra variável; a sua tarefa é observar se foi feita
# alguma troca durante a passagem ou não; se não houver troca, então a lista já está ordenada, e nada mais tem
# de ser feito. Criamos uma variável chamada swapped, e atribuímos-lhe um valor de False , para indicar que não há
# trocas. Caso contrário, será atribuído True.
#
my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.


# Deverá ser capaz de ler e compreender este programa sem quaisquer problemas:

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
# [2, 4, 6, 8, 10]

# =====================================================================O bubble sort - versão interativa

# No editor pode ver um programa completo, enriquecido por uma conversa com o utilizador, e que permite ao utilizador
# introduzir e imprimir elementos da lista: O bubble sort - versão interativa final.

# O Python, contudo, tem os seus próprios mecanismos de ordenação. Ninguém precisa de escrever a sua própria
# ordenação, uma vez que existe um número suficiente de ferramentas prontas a usar.

# Explicámos-lhe este sistema de ordenação porque é importante aprender a processar o conteúdo de uma
# lista, e mostrar-lhe como a ordenação real pode funcionar.

# Se quiser que o Python ordene a sua lista, pode fazê-lo desta forma:

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# É tão simples quanto isso.

# O output do snippet é o seguinte:

[2, 4, 6, 8, 10]

# Como pode ver, todas as listas têm um método chamado sort(), que as classifica o mais rapidamente possível.
# Já aprendeu alguns dos métodos de lista antes, e vai aprender mais sobre outros muito em breve.

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
# How many elements do you want to sort:
# KeyboardInterrupt

# =========================================================== RESUMO ===================================================

# 1. Pode utilizar a keyword sort() para ordenar elementos de uma lista, por exemplo:

lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]

# 2. Há também um método de lista chamado reverse(), que pode utilizar para inverter a lista, por exemplo

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]

# ===================================================================

lst = ["D", "F", "A", "Z"]
lst.sort()

print(lst)
# ['A', 'D', 'F', 'Z']

# ===================================================================

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)
# [1, 2, 3]

# ===================================================================

a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)
# [' ', 'C', 'B', 'A']

# ===================================================================

# ========================================================================A vida interna das listas

# Agora queremos mostrar-lhe uma característica importante, e muito surpreendente, das listas, que as distingue
# fortemente das variáveis comuns.

# Queremos que o memorize - pode afetar os seus programas futuros, e causar graves problemas se esquecido ou
# negligenciado.

# Veja o snippet no editor.

# O programa:

# ===> cria uma lista de um elemento chamada list_1;
# ===> atribui-o a uma nova lista chamada list_2;
# ===> altera o único elemento de list_1;
# ===> imprime list_2.

# A parte surpreendente é o facto de que o programa fará o output: [2], não [1], que parece ser a solução óbvia.

# As listas (e muitas outras entidades complexas de Python) são armazenadas de formas diferentes das variáveis
# ordinárias (escalares).

# Pode-se dizer que:

# ===> o nome de uma variável ordinária é o nome do seu conteúdo;
# ===> o nome de uma lista é o nome de um local de memória onde a lista é armazenada.

# Leia estas duas linhas mais uma vez - a diferença é essencial para compreender aquilo de que vamos falar a seguir.

# A atribuição: list_2 = list_1 copia o nome do array, não o seu conteúdo. Com efeito, os dois nomes
# (list_1 e list_2) identificam o mesmo local na memória do computador. Modificar um deles afeta o outro, e vice-versa.

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
# [2]

# =============================================================================== Slices poderosas

# Felizmente, a solução está ao seu alcance - o seu nome é slice.
# Uma slice é um elemento da sintaxe Python que lhe permite fazer uma cópia completamente nova de uma lista ou
# partes de uma lista.

# Na verdade, a slice copia o conteúdo da lista, não o seu nome.

# Isto é exatamente o que necessita. Dê uma vista de olhos no snippet em baixo:

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# O seu output é [1].

# Esta parte inconspícua do código descrito como [:] é capaz de produzir uma lista completamente nova.

# Uma das formas mais gerais da slice tem o seguinte aspeto:

my_list[start:end]

# Como pode ver, assemelha-se à indexação, mas os dois pontos no interior fazem uma grande diferença.
#
# Uma slice desta forma faz uma nova lista (alvo), retirando elementos da source list - os elementos dos índices
# desde o início até end - 1.

# Nota: não para end mas para end - 1. Um elemento com um índice igual a end é o primeiro elemento que não
# participa no slicing.

# É possível utilizar valores negativos tanto para o início como para o fim (tal como na indexação).

# Veja o snippet:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# A new_list lista terá end - start (3 - 1 = 2) elementos - aqueles com índices iguais a 1 e 2 (mas não 3).

# O output do snippet é: [8, 6]

# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
# [1]
# [8, 6]

# =================================================================== Slices - índices negativos

# Veja o snippet em baixo:

my_list[start:end]

# Para repetir:

# ===> start é o index do primeiro elemento incluído no slice;
# ===> end é o index do primeiro elemento não incluído no slice.

# É assim que os índices negativos funcionam com o slice:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
# [8, 6, 4]


# Se o start especifica um elemento que se encontra mais longe do que o descrito pelo end
# (do ponto de vista inicial da lista), o slice estará vazio:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
# []

# ======================================================================== Slices: continuação

# Se omitir o start no seu slice, assume-se que pretende obter um slice começando pelo elemento com index 0.

# Por outras palavras, o slice desta forma:

my_list[:end]

# é um equivalente mais compacto de:

my_list[0:end]

# Veja o snippet em baixo:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# É por isso que o seu output é: [10, 8, 6].

# Da mesma forma, se omitir o end no seu slice, presume-se que deseja que o slice termine no elemento com o
# index len(my_list).

# Por outras palavras, o slice desta forma:

my_list[start:]

# é um equivalente mais compacto de:

my_list[start:len(my_list)]

# Veja o snippet seguinte:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
# [4, 2]

# ========================================================================= Slices: continuação

# Como já dissemos anteriormente, omitindo ambos start e end faz uma cópia de toda a lista:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)
#[10, 8, 6, 4, 2].

# A instrução anteriormente descrita del é capaz de apagar mais do que apenas um elemento de uma lista
# ao mesmo tempo - também pode apagar slices:

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# Nota: neste caso, o slice não produz nenhuma lista nova!

# O output do snippet é: [10, 4, 2].

# A eliminação de todos os elementos de uma só vez também é possível:

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
#  [].

# A remoção do slice do código muda dramaticamente o seu significado.

# Veja:

my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)

# A instrução del eliminará a lista em si, não o seu conteúdo.

# A print() invocação da função a partir da última linha do código causará então um erro de runtime.

# ============================================================================Os loops in e not in operadores

# O Python oferece dois operadores muito poderosos, capazes de olhar através da lista a fim de verificar se um
# valor específico está ou não armazenado dentro da lista

# Estes operadores são:

elem in my_list
elem not in my_list

# O primeiro deles (in) verifica se um dado elemento (o seu argumento da esquerda) está atualmente armazenado
# algures dentro da lista (o argumento da direita) - o operador devolve True neste caso.

# O segundo (not in) verifica se um dado elemento (o seu argumento da esquerda) está ausente numa lista - o operador
# devolve True neste caso.

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
# False
# True
# True

# ======================================================================= Listas - alguns programas simples

# Agora queremos mostrar-lhe alguns programas simples que utilizam listas.

# O primeiro deles tenta encontrar o maior valor na lista. Veja o código no editor.
#
# O conceito é bastante simples - assumimos temporariamente que o primeiro elemento é o maior, e verificamos a
# hipótese contra todos os restantes elementos da lista.

# O código fará o output 17 (como esperado).

# O código pode ser reescrito para fazer uso da forma recentemente introduzida do for :

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
     largest = i

print(largest)

# O programa acima realiza uma comparação desnecessária, quando o primeiro elemento é comparado consigo
# mesmo, mas isto não é de todo um problema.

# O código fará o output 17, também (nada invulgar).

# Se precisar de poupar energia do computador, pode utilizar um slice:

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)

#  =============================================================================

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)
# 17

# ========================================================================Listas - alguns programas simples

# Agora vamos encontrar a localização de um dado elemento dentro de uma lista:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")
# Element found at index 4


# Nota:

# ===> o valor alvo é armazenado na variável to_find ;
# ===> o estado atual da pesquisa é armazenado na variável found (True/False)
# ===> quando found se torna True, o loop for é saído.

# Vamos supor que escolheu os seguintes números na lotaria: 3, 7, 11, 42, 34, 49.

# Os números que foram sorteados são: 5, 11, 9, 42, 3, 49.

# A questão é: em quantos números é que acertou?

# O programa dar-lhe-á a resposta:

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

# Nota:

# ===> a keyword drawn armazena todos os números sorteados;
# ===> a lista bets armazena as suas apostas;
# ===> a variável hits conta os seus êxitos.

# O output do programa é: 4.

#  ===================================================================

# escrever um programa que remova todas as repetições de números da lista. O objetivo é ter uma lista na
# qual todos os números não aparecem mais de uma vez.
# Nota: suponha que a source list está codificada dentro do código - não tem de a introduzir a partir
# do teclado. É claro que pode melhorar o código e adicionar uma parte que pode realizar uma conversa com o utilizador
# e obter todos os dados a partir dele.
# Dica: encorajamo-lo a criar uma nova lista como área de trabalho temporária - não precisa de atualizar
# a lista in situ.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for number in my_list:  # Browse all numbers from the source list.
	if number not in new_list:  # If the number doesn't appear within the new list...
		new_list.append(number)  # ...append it here.
my_list = new_list[:]  # Make a copy of new_list.
print("The list with unique elements only:")
print(my_list)
# The list with unique elements only:
# [1, 2, 4, 6, 9]

# ================================================ RESUMO ============================================================

# 1. Se tiver uma lista l1, então a seguinte tarefa: l2 = l1 não faz uma cópia da lista l1 , mas faz com que as
# variáveis l1 e l2 apontem para uma e a mesma lista na memória. Por exemplo:

vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']

# 2. Se quiser copiar uma lista ou parte da lista, pode fazê-lo executando slicing:

colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list

# 3. Também se podem utilizar índices negativos para executar slices. Por exemplo:

sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

# 4. O objeto da exceção start e end parâmetros são opcionais ao executar uma slice: list[start:end], por exemplo.:

my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]

# 5. Pode eliminar slices usando a instrução del :

my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # deletes the list content, outputs: []

# 6. Pode testar se alguns itens existem numa lista ou não usando as keywords in e not in, por exemplo.:

my_list = ["A", "B", 1, 2]

print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False

#  ================================================================

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)
# ['C']

#  ================================================================

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)
# ['B', 'C']

#  ================================================================

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)
# []

#  ================================================================

list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)
# ['A', 'B', 'C']

#  ================================================================

my_list = [1, 2, "in", True, "ABC"]

print(1 ??? my_list)  # outputs True
print("A" ??? my_list)  # outputs True
print(3 ??? my_list)  # outputs True
print(False ??? my_list)  # outputs False
# my_list = [1, 2, "in", True, "ABC"]
#
# print(1 in my_list)  # outputs True
# print("A" not in my_list)  # outputs True
# print(3 not in my_list)  # outputs True
# print(False in my_list)  # outputs False

# =======================================================================================Listas em listas

# As listas podem consistir em escalares (nomeadamente números) e elementos de uma estrutura muito mais complexa
# (já viu exemplos como strings, booleanos, ou mesmo outras listas nas lições do Resumo da Secção anterior).
# Vamos analisar mais de perto o caso em que os elementos de uma lista são apenas listas.

# Encontramos frequentemente tais arrays (matrizes) nas nossas vidas. Provavelmente o melhor exemplo disto
# é um tabuleiro de xadrez.

# Um tabuleiro de xadrez é composto por linhas e colunas. Existem oito linhas (em inglês, rows) e oito colunas.
# Cada coluna é marcada com as letras de A a H. Cada linha é marcada com um número de um a oito.

# A localização de cada campo é identificada por pares de letras-dígitos. Assim, sabemos que o canto inferior
# esquerdo do tabuleiro (o que tem a torre branca) é A1, enquanto que o canto oposto é H8.

# Vamos assumir que somos capazes de utilizar os números selecionados para representar qualquer peça de xadrez.
# Podemos também assumir que cada linha do tabuleiro de xadrez é uma lista.
#
# Veja o código abaixo:

row = []

for i in range(8):
    row.append(WHITE_PAWN)


# Constrói uma lista contendo oito elementos que representam a segunda linha do tabuleiro de xadrez - a que está cheia
# de peões (suponha que WHITE_PAWN é um símbolo pré-definido que representa um peão branco).

# O mesmo efeito pode ser alcançado através de uma compreensão de lista, a sintaxe especial utilizada por Python
# para preencher listas massivas.

# Uma compreensão de lista é na realidade uma lista, mas criada durante a execução do programa, e não é descrita
# estaticamente.

# Veja o snippet:

row = [WHITE_PAWN for i in range(8)]


# A parte do código colocada dentro dos parêntesis retos especifica:

# ===> os dados a utilizar para preencher a lista (WHITE_PAWN)
# ===>a cláusula que especifica quantas vezes os dados ocorrem dentro da lista (for i in range(8))

# Deixe-nos mostrar-lhe alguns outros exemplos de compreensão de lista:

# Exemplo #1:

squares = [x ** 2 for x in range(10)]

# O snippet produz uma lista de dez elementos preenchida com quadrados de dez números inteiros começando do
# zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

# Exemplo #2:

twos = [2 ** i for i in range(8)]

# O snippet cria um array de oito elementos contendo as primeiras oito potências de dois (1, 2, 4, 8, 16, 32, 64, 128)

# Exemplo #3:

odds = [x for x in squares if x % 2 != 0 ]

# O snippet faz uma lista apenas com os elementos ímpares da lista squares .

# =============================================================================Listas em listas: arrays bidimensionais

# Vamos também assumir que um símbolo pré-definido chamado EMPTY designa um campo vazio no tabuleiro de xadrez.

# Assim, se quisermos criar uma lista de listas representando todo o tabuleiro de xadrez, isso pode ser feito da
#  seguinte forma:

board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

# Nota:

# ===> a parte interior do loop cria uma linha composta por oito elementos (cada um deles igual a EMPTY) e
#   anexa-o à lista board ;
# ===> a parte externa repete-o oito vezes;
# ===> no total, a lista board consiste em 64 elementos (todos iguais a EMPTY)

# Este modelo imita perfeitamente o verdadeiro tabuleiro de xadrez, que é de facto uma lista de oito
# elementos, sendo todos eles filas únicas. Vamos resumir as nossas observações:

# ===> os elementos das filas são campos, oito deles por fila;
# ===> os elementos do tabuleiro de xadrez são linhas, oito delas por tabuleiro de xadrez.

# A variável board é agora um array bidimensional. Também é chamada, por analogia aos termos algébricos, uma matriz.

# Como as compreensões de lista podem ser nested, podemos encurtar a criação do tabuleiro da seguinte forma:

board = [[EMPTY for i in range(8)] for j in range(8)]

# A parte interior cria uma fila, e a parte exterior constrói uma lista de filas.

EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)
# [['ROOK', '-', '-', '-', '-', '-', '-', 'ROOK'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-',
# '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-',
# '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['ROOK', '-', '-', '-', '-', '-', '-',
# 'ROOK']]

# ==========================================================Natureza multidimensional das listas: aplicações avançadas

# Vamos aprofundar a natureza multidimensional das listas. Para encontrar qualquer elemento de uma lista
# bidimensional, é preciso utilizar duas coordenadas:

# ===> uma vertical (número da fila)
# ===>e uma horizontal (número da coluna).

# Imagine que desenvolve uma peça de software para uma estação meteorológica automática. O dispositivo
# regista a temperatura do ar numa base horária e fá-lo ao longo de todo o mês. Isto dá-lhe um total de 24 & vezes;
#  31 = 744 valores. Vamos tentar criar uma lista capaz de armazenar todos estes resultados.

# Primeiro, tem de decidir que tipo de dados serão adequados para esta aplicação. Neste caso, um float seria
# melhor, uma vez que este termómetro é capaz de medir a temperatura com uma precisão de 0,1 ℃.

# De seguida, toma uma decisão arbitrária de que as filas registarão as leituras de hora em hora (por isso
# a fila terá 24 elementos) e que cada uma das filas será atribuída a um dia do mês (vamos supor que cada mês
# tem 31 dias, por isso precisa de 31 filas). Aqui está o par apropriado de compreensões (h é para hora, d para dia):

temps = [[0.0 for h in range(24)] for d in range(31)]

# Toda a matriz está agora preenchida com zeros. Pode assumir que é atualizada automaticamente utilizando agentes
# especiais de hardware. O que tem de fazer é esperar que a matriz seja preenchida com medições.

# Agora é altura de determinar a temperatura média mensal ao meio-dia. Some todas as 31 leituras registadas ao
# meio-dia e divida a soma por 31. Pode assumir que a temperatura à meia-noite é armazenada em primeiro lugar.
# Aqui está o código relevante:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]
# average = total / 31

print("Average temperature at noon:", average)
# Average temperature at noon: 0.0

# Nota: a variável day usada pelo loop for não é um escalar - cada passagem através da matriz temps atribui-a com
# as linhas subsequentes da matriz; portanto, é uma lista. Tem que ser indexado com 11 para aceder ao valor da
# temperatura medida ao meio-dia.

# Agora encontre a temperatura mais alta durante todo o mês - veja o código:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)
# The highest temperature was: 0.0

# Nota:

# ===> a keyword day itera através de todas as linhas na matriz temps ;
# ===> a variável temp itera através de todas as medições efetuadas num dia.

# Agora conte os dias em que a temperatura ao meio-dia era de pelo menos 20 ℃:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

hot_days = 0
for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")
# 0 days were hot.

# ===========================================================================Arrays tridimensionais

# O Python não limita a profundidade da inclusão list-in-list. Aqui pode ver um exemplo de um array tridimensional:

# Imagine um hotel. É um enorme hotel constituído por três edifícios, com 15 andares cada um. Há 20 quartos em cada
# andar. Para tal, é necessário um array que possa recolher e processar informações sobre os quartos ocupados/livres.

# Primeiro passo - o tipo de elementos do array. Neste caso, um valor booleano (True/False) caberia.

# Segundo passo - análise calma da situação. Resumir a informação disponível: três edifícios, 15 andares, 20 quartos.

# Agora pode criar o array:

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# O primeiro index (0 através 2) seleciona um dos edifícios; o segundo (0 através 14) seleciona o andar,
# o terceiro (0 através 19) seleciona o número do quarto. Todos os quartos estão inicialmente livres.

# Agora pode reservar um quarto para dois recém-casados: no segundo edifício, no décimo andar, quarto 14:

rooms[1][9][13] = True

# e libertar o segundo quarto no quinto andar, localizado no primeiro edifício:

rooms[0][4][1] = False

# Verifique se há vagas no 15º andar do terceiro edifício:

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

# A variável vacancy contém 0 se todos os quartos estiverem ocupados, ou o número de quartos disponíveis, caso contrário.

# ================================================= RESUMO =============================================================

# 1. A compreensão de lista permite-lhe criar novas listas a partir de listas existentes de uma forma concisa e
# elegante. A sintaxe de uma compreensão de lista é a seguinte:

[expression for element in list if conditional]

# que é na verdade um equivalente ao seguinte código:

for element in list:
    if conditional:
        expression

# Eis um exemplo de compreensão de uma lista - o código cria uma lista de cinco elementos preenchida com os primeiros
# cinco números naturais elevados à potência de 3:

cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]

# 2. Pode usar listas nested em Python para criar matrizes (ou seja, listas bidimensionais). Por exemplo:

# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

# 3. Pode fazer nest de quantas lists-in-lists quiser, e portanto criar listas n-dimensionais, por exemplo, três,
# quatro ou mesmo sessenta e quatro arrays dimensionais. Por exemplo:

# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'

#  ================================================================================================================

# breve resumo dos objetivos que abordou e com os quais se familiarizou no Módulo 3:

# Valores booleanos para comparar diferentes valores e controlar os caminhos de execução usando as instruções if e if-else ;
# a utilização de loops (while e for) e como controlar o seu comportamento usando as instruções break e continue ;
# a diferença entre as operações lógicas e as operações bitwise;
# o conceito de listas e processamento de listas, incluindo a iteração fornecida pelo loop for , e slicing;
# a ideia de arrays multidimensionais.