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



