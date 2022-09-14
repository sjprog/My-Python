# ================================================ A função print() ===================================================

# A palavra print que se pode ver aqui é um nome de função. Isso não significa que, onde quer que a palavra apareça,
# é sempre um nome de função. O significado da palavra vem do contexto em que a palavra foi usada.
# print("Hello, World!") Apesar do número de argumentos necessários/fornecidos, as funções Python exigem fortemente a
# presença de um par de parêntesis - de abertura e de fecho, respetivamente. Se quiser entregar um ou mais argumentos a
# uma função, coloque-os dentro dos parêntesis. Se for utilizar uma função que não aceita qualquer argumento, ainda
# assim tem de ter os parêntesis.

# O que acontece quando o Python encontra uma invocação como esta abaixo?

# function_name(argument)

# ==>Primeiro, o Python verifica se o nome especificado é legal (navega nos seus dados internos a fim de encontrar
#       uma função existente com o mesmo nome; se esta pesquisa falhar, o Python aborta o código);
# ==>segundo, o Python verifica se os requisitos da função para o número de argumentos lhe permitem invocar a função
#       desta forma (por exemplo, se uma função específica exigir exatamente dois argumentos, qualquer invocação que
#       apresente apenas um argumento será considerada errada, e abortará a execução do código);
# ==>terceiro, o Python deixa o seu código por um momento e salta para a função que pretende invocar; claro, também leva
#       o(s) seu(s) argumento(s) e passa-o(s) para a função;
# ==>quarto, a função executa o seu código, causa o efeito desejado (se houver um), avalia o(s) resultado(s) desejado(s)
#       (se existir(em)) e termina a sua tarefa;
# ==>finalmente, o Python regressa ao seu código (ao local imediatamente após a invocação) e retoma a sua execução.

# Como pode ver, a invocação vazia print() não é tão vazia como se poderia esperar - produz uma linha vazia, ou
# (esta interpretação também é correta) o seu output é apenas uma newline.

# Esta não é a única forma de produzir uma newline na consola de output. Vamos agora mostrar-lhe outra forma.

# Há duas mudanças muito subtis - inserimos um estranho par de carateres dentro da rima. Têm este aspeto: \n.

# Curiosamente, enquanto se pode ver dois carateres, o Python vê um.
# A barra invertida (\) tem um significado muito especial quando usado dentro de strings - a isto chama-se o caratere de escape.

# A palavra escape deve ser entendida especificamente - significa que a série de carateres na string escapa por
# um momento (um momento muito curto) para introduzir uma inclusão especial.

# Por outras palavras, a barra invertida não significa nada em si, mas é apenas uma espécie de anúncio de que o
# próximo caratere após a barra invertida também tem um significado diferente.

# A letra n colocada após a barra invertida vem da palavra newline (nova linha).

# Tanto a barra invertida como o n formam um símbolo especial chamado um caratere de newline, que incita a consola a
# iniciar uma nova linha de output.

#  ============================  end='' =======================

#   O Python oferece outro mecanismo para a passagem de argumentos, que pode ser útil quando se quer convencer a
#   print() função a alterar um pouco o seu comportamento.
#
#   Não o vamos explicar em profundidade neste momento. Planeamos fazê-lo quando falarmos de funções. Por agora,
#   queremos simplesmente mostrar-lhe como funciona. Sinta-se à vontade para o utilizar nos seus próprios programas.
#
#   O mecanismo é chamado argumentos de keyword. O nome deriva do facto de o significado destes argumentos ser
#   retirado não da sua localização (posição) mas da palavra especial (keyword) utilizada para os identificar.
#
#   A função print() tem dois argumentos de keyword que pode usar para os seus propósitos. O primeiro deles é nomeado end.

#   Na janela do editor pode ver um exemplo muito simples da utilização de um argumento de keyword.

#   Para a sua utilização, é necessário conhecer algumas regras:

# ==>  um argumento de keyword consiste em três elementos: uma keyword identificando o argumento (end aqui); um sinal
#      de igual (=); e um valor atribuído a esse argumento;
# ==>  qualquer argumento de keyword tem de ser colocado após o último argumento posicional (isto é muito importante)

# Como pode ver, o argumento de keyword end determina os carateres que a função print() envia para o output,
# uma vez que atinge o final dos seus argumentos posicionais.

# O comportamento padrão reflete a situação em que o argumento de keyword end é implicitamente usado
# da seguinte maneira: end="\n".

print("My name is", "Python.", end=" ")
print("Monty Python.")
# My name is Python. Monty Python.

# Se olhar cuidadosamente, verá que utilizámos o argumento end , mas a string atribuída a ele está vazia
# (não contém nenhum caratere).
# O que vai acontecer agora? Execute o programa no editor para descobrir.
# Como o argumento end foi definido para nada, a função print() também não produz nenhum output, uma vez que os
# seus argumentos posicionais foram esgotados.
# Nota: não foram enviadas newlines para o output.
# A string atribuída ao argumento de keyword end pode ter qualquer comprimento. Experimente-a se quiser.

#  ============================  sep=' ' =======================
# Já dissemos anteriormente que a função print() separa os seus argumentos de output com espaços.
# Este comportamento também pode ser alterado.
# O argumento de keyword que pode fazer isto é chamado sep (como separador).

# Veja o código no editor, e execute-o.

# O argumento sep fornece os seguintes resultados: My-name-is-Monty-Python.

# A função print() agora utiliza um traço, em vez de um espaço, para separar os argumentos de output.

# Nota: o valor do argumento sep também pode ser uma string vazia. Experimente você mesmo.

print("My", "name", "is", "Monty", "Python.", sep="-")
# My-name-is-Monty-Python.

# Ambos os argumentos de keyword podem ser misturados numa só invocação, tal como aqui na janela do editor.
# O exemplo não faz muito sentido, mas apresenta visivelmente as interações entre end e sep.
# Consegue prever o output?
# Execute o código e veja se corresponde às suas previsões.
# Agora que compreende a função print() , está pronto a considerar como armazenar e processar dados em Python.
# Sem print(), não seria capaz de ver nenhum resultado.

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
# My_name_is*Monty*Python.*

print("Programming","Essentials","in", sep="", end="")
print("Python")
# ProgrammingEssentialsinPython

# ===== Exemplo ====

# Encorajamo-lo vivamente a brincar com o código que escrevemos para si, e a fazer algumas (talvez mesmo destrutivas)
# alterações. Sinta-se livre para modificar qualquer parte do código, mas há uma condição - aprenda com os seus erros e tire as suas próprias conclusões.

# Tente:

# ==> minimizar o número de invocações da função print() inserindo a sequência \n nas strings
# ==> fazer a seta duas vezes maior (mas mantendo as proporções)
# ==> duplicar a seta, colocando ambas as setas lado a lado; nota: uma string pode ser multiplicada usando o seguinte
#       truque: "string" * 2 produzirá "stringstring" (brevemente, falaremos mais sobre o assunto)
# ==> retire qualquer uma das aspas, e veja cuidadosamente a resposta do Python; preste atenção ao local onde o
#       Python vê um erro - é este o local onde o erro realmente existe?
# ==> faça o mesmo com alguns dos parêntesis;
# ==> altere qualquer uma das print palavras por outra coisa, diferindo apenas no caso (por exemplo, Print) - o que acontece agora?
# ==> substitua algumas das aspas por apóstrofes; observe cuidadosamente o que acontece.

###################
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)
# original version:
#     *
#    * *
#   *   *
#  *     *
# ***   ***
#   *   *
#   *   *
#   *****
# with fewer 'print()' invocations:
#     *
#    * *
#   *   *
#  *     *
# ***   ***
#   *   *
#   *   *
#   *****
# higher:
#         *
#        * *
#       *   *
#      *     *
#     *       *
#    *         *
#   *           *
#  *             *
# ******     ******
#      *     *
#      *     *
#      *     *
#      *     *
#      *     *
#      *     *
#      *******
# doubled:
#         *                *
#        * *              * *
#       *   *            *   *
#      *     *          *     *
#     *       *        *       *
#    *         *      *         *
#   *           *    *           *
#  *             *  *             *
# ******     ************     ******
#      *     *          *     *
#      *     *          *     *
#      *     *          *     *
#      *     *          *     *
#      *     *          *     *
#      *     *          *     *
#      *******          *******

# =================================================  Resumo =====================================================

# 1. A função print() é uma função incorporada. Imprime/faz output de uma mensagem especificada para a janela do ecrã/consola.
# 2. As funções incorporadas, ao contrário das funções definidas pelo utilizador, estão sempre disponíveis
#   e não têm de ser importadas. O Python 3.8 vem com 69 funções incorporadas. Pode encontrar a sua lista completa
#   fornecida em ordem alfabética na Biblioteca Padrão Python.
# 3. Para chamar uma função (este processo é conhecido como invocação de função ou chamada de função), é necessário
#   usar o nome da função seguido de parêntesis. Pode passar argumentos para uma função, colocando-os dentro dos
#   parêntesis. Deve separar os argumentos com uma vírgula, por exemplo, print("Hello,", "world!"). Uma função “vazia”
#   print() faz output de uma linha vazia para o ecrã.
# 4. As strings de Python são delimitadas com aspas, por exemplo, "I am a string" (aspas duplas), ou 'I am a string,
#   too' (aspas simples).
# 5. Os programas de computador são coleções de instruções. Uma instrução é um comando para executar uma tarefa
#   específica quando executada, por exemplo, para imprimir uma determinada mensagem no ecrã.
# 6. Em strings de Python a barra invertida (\) é um caratere especial que anuncia que o próximo caratere tem um
#   significado diferente, por exemplo \n (the newline character) starts a new output line.
# 7. Os argumentos posicionais são aqueles cujo significado é ditado pela sua posição, por exemplo, o segundo
#   argumento é apresentado após o primeiro, o terceiro é apresentado após o segundo, etc.
# 8. Os argumentos de keyword são aqueles cujo significado não é ditado pela sua localização, mas por uma palavra
#   especial (keyword) utilizada para os identificar.
# 9. Os loops end e sep podem ser usados para formatar o output da função print() . O parâmetro sep especifica o
#   separador entre os argumentos de output (por exemplo, o parâmetro print("H", "E", "L", "L", "O", sep="-"),
#   enquanto o parâmetro end especifica o que imprimir no final da declaração print.


#  ========================================== Inteiros: números octais e hexadecimais =================================

# Há duas convenções adicionais em Python que são desconhecidas no mundo da matemática. A primeira permite-nos utilizar
# números numa representação octal.
# Se um número inteiro for precedido por um 0O ou 0o prefixo (zero-o), ele será tratado como um valor octal.
# Isto significa que o número deve conter apenas dígitos retirados do intervalo [0..7].
# 0o123 é um número octal com um valor (decimal) igual a 83.
# A classe print() faz a conversão automaticamente. Experimente isto:
print(0o123)

# A segunda convenção permite-nos utilizar números hexadecimais. Estes números devem ser precedidos pelo prefixo 0x ou 0X (zero-x).
# 0x123 é um número hexadecimal com um valor (decimal) igual a 291. A função print() também pode gerir estes valores. Experimente isto:
print(0x123)

# =================================================== Floats ===========================================================

# Agora é altura de falar de outro tipo, que foi concebido para representar e armazenar os números que
# (como diria um matemático) têm uma fração decimal não vazia.

# São os números que têm (ou podem ter) uma parte fracionada após o ponto decimal, e embora tal definição seja muito
# pobre, é certamente suficiente para o que desejamos discutir.

# Sempre que utilizamos um termo como dois e meio ou menos zero ponto quatro, pensamos em números que o computador
# considera números de floating-point:
2.5
-0.4
# Nota: dois e meio parece normal quando se escreve num programa, embora se a sua língua materna preferir usar
# uma vírgula em vez de um ponto no número, deve assegurar-se de que o seu número não contém quaisquer vírgulas.

# O Python não aceitará isso, ou (em casos muito raros mas possíveis) pode interpretar mal as suas intenções,
# uma vez que a própria vírgula tem o seu significado reservado em Python.
#
# Se quiser usar apenas um valor de dois e meio, deve escrevê-lo como mostrado acima. Nota mais uma vez -
# há um ponto entre 2 e 5 - não uma vírgula.
# Como provavelmente pode imaginar, o valor de zero ponto quatro pode ser escrito em Python como:
#
# 0.4
#
# Mas não se esqueça desta regra simples - pode omitir o zero quando é o único dígito em frente ou após o ponto decimal.
#
# Em essência, pode escrever o valor 0.4 como:
#
# .4
#
# Por exemplo: o valor de 4.0 pode ser escrito como:
#
# 4.
#
# Isto não mudará nem o seu tipo nem o seu valor.

#  ===================================================== Ints vs. floats ===============================================

# O ponto decimal é essencialmente importante no reconhecimento de números de floating-point em Python.
#
# Veja estes dois números:
#
# 4
# 4.0
#
# Pode pensar que eles são exatamente os mesmos, mas o Python vê-os de uma forma completamente diferente.
#
# 4 é um número inteiro, enquanto que 4.0 é um número floating-point.
#
# O ponto é o que faz um float.
#
#
# Por outro lado, não são apenas os pontos que fazem um float. Também pode utilizar a letra e.
#
# Quando quiser usar números muito grandes ou muito pequenos, pode usar notação científica.

# Tome, por exemplo, a velocidade da luz, expressa em metros por segundo. Escrito diretamente, ficaria assim: 300000000.
#
# Para evitar escrever tantos zeros, os livros de física utilizam uma forma abreviada, que provavelmente já viu: 3 x 108.
#
# Lê-se: três vezes dez à potência de oito.
#
# Em Python, o mesmo efeito é conseguido de uma forma ligeiramente diferente - veja:
#
# 3E8
#
# A letra E (também pode utilizar a letra minúscula e - vem da palavra expoente) é um registo conciso da frase
# vezes dez à potência de.
#
# Nota:
#
# o expoente (o valor após o E) deve ser um número inteiro;
# a base (o valor à frente do E) pode ser um inteiro.

# === Codificação de floats ===

# Vejamos como esta convenção é utilizada para registar números que são muito pequenos (no sentido do seu valor
# absoluto, que está próximo de zero).
#
# Uma constante física chamada constante de Planck (e denotada com um h), de acordo com os manuais escolares,
# tem o valor de: 6.62607 x 10-34.
#
# Se quiser utilizá-la num programa, deve escrevê-la desta forma:
#
# 6.62607E-34
#
# Nota: o facto de ter escolhido uma das formas possíveis de codificação de valores float não significa que o
# Python o apresente da mesma forma.
#
# O Python pode, por vezes, escolher uma notação diferente da sua.
# Por exemplo, digamos que decidiu usar o seguinte float literal:
#
# 0.0000000000000000000001
#
# Quando executa este literal através do Python:
#
# print(0.0000000000000000000001)
#
#
# este é o resultado:
#
# 1e-22

# O Python escolhe sempre a forma mais económica de apresentação do número, e deve ter isto em consideração
# ao criar literais.


# ==== Strings ====


# Strings são utilizadas quando é necessário processar texto (como nomes de todos os tipos, endereços, romances, etc.)
# , não números.
#
# Já sabe um pouco sobre elas. Por exemplo, que as strings precisam de aspas da mesma forma que floats precisam de pontos.
#
# Esta é uma string muito típica: "I am a string."
#
#
# No entanto, há um senão. O senão é como codificar uma aspa dentro de uma string que já está delimitada por aspas.
#
# Vamos supor que queremos imprimir uma mensagem muito simples dizendo:
#
# I like "Monty Python"
#
# Como fazemos isto sem gerar um erro? Existem duas soluções possíveis.

# A primeira baseia-se no conceito que já conhecemos do caratere de escape, que como se deve lembrar é
# representado pela barra invertida. A barra invertida também pode escapar às aspas. Uma aspa precedida por uma barra
# invertida muda o seu significado - não é um delimitador, mas apenas uma aspa. Isto funcionará como pretendido:
#
# print("I like \"Monty Python\"")
#
#
# Nota: existem duas aspas escapadas dentro da string - consegue vê-las?
#
# A segunda solução pode ser um pouco surpreendente. O Python pode utilizar uma apóstrofe em vez de uma aspa.
# Qualquer um destes carateres pode delimitar strings, mas deve ser consistente.
#
# Se abrir uma string com uma aspa, tem de fechá-la com uma aspa.
#
# Se começar uma string com uma apóstrofe, tem de a acabar com uma apóstrofe.
#
# Este exemplo também funcionará:
#
# print('I like "Monty Python"')
#
#
# Nota: não precisa de fazer nenhum escape aqui.

#  =============== Valores Booleanos ==================

# Para concluir com os literais de Python, existem mais dois.
#
# Não são tão óbvios como os anteriores, uma vez que são usados para representar um valor muito abstrato -
# truthfulness (veracidade).
#
# Cada vez que pergunta ao Python se um número é maior que outro, a pergunta resulta na criação de alguns dados
# específicos - um valor Booleano.
#
# O nome vem de George Boole (1815-1864), autor da obra fundamental, As Leis do Pensamento, que contém a definição de
# álgebra Booleana - uma parte da álgebra que faz uso de apenas dois valores distintos: True e False, denotado como 1 e 0.
#
#
# Um programador escreve um programa, e o programa faz perguntas. O Python executa o programa, e fornece as respostas.
# O programa deve ser capaz de reagir de acordo com as respostas recebidas.
#
# Felizmente, os computadores conhecem apenas dois tipos de respostas:
#
#   Sim, isto é verdade;
#   Não, isto é falso.
# Nunca obterá uma resposta como: Não sei ou Provavelmente sim, mas não sei ao certo.

# O Python, então, é um réptil binário.
#
# Estes dois valores Booleanos têm denotações rigorosas em Python:
#
# True
# False
#
# Não se pode mudar nada - é preciso tomar estes símbolos tal como eles são, incluindo case-sensitivity.
#
#
# Desafio: Qual será o output do seguinte snippet de código?
#
# print(True > False)
# print(True < False)
#
#
# Execute o código na Sandbox para verificar. Consegue explicar o resultado?

print("I'm\nlearning Python")
# I'm
# learning Python

#  ================================================== RESUMO ===========================================================

# 1. Os literais são notações para representar alguns valores fixos em código. O Python tem vários tipos de literais -
#   por exemplo, um literal pode ser um número (literais numéricos, por exemplo, 123), ou uma string
#   (literais de string, por exemplo, “Eu sou um literal.“).
#
# 2. O sistema binário é um sistema de números que emprega 2 como base. Portanto, um número binário é composto apenas
#   por 0s e 1s, por exemplo, 1010 é 10 em decimal.
#
# Os sistemas de numeração octal e hexadecimal, do mesmo modo, empregam 8 e 16 como suas bases, respetivamente.
# O sistema hexadecimal utiliza os números decimais e seis letras extra.

# 3. Inteiros (ou simplesmente ints) são um dos tipos numéricos suportados pelo Python. São números escritos sem um
#   componente fracionário, por exemplo, 256, ou -1 (inteiros negativos).
#
# 4. Números de floating-point (ou simplesmente floats) são outro dos tipos numéricos suportados pelo Python.
#   São números que contêm (ou são capazes de conter) um componente fracionário, por exemplo 1.27.
#
# 5. Para codificar uma apóstrofe ou uma aspa dentro de uma string, pode usar o caratere de escape, por
#   exemplo, 'I\'m happy.', ou abrir e fechar a string utilizando um conjunto de símbolos opostos aos que deseja
#   codificar, por exemplo "I'm happy." codificar uma apóstrofe, e 'He said "Python", not "typhoon"' para codificar
#   umas aspas (duplas).
#
# 6. Valores booleanos são os dois objetos constantes True e False usado para representar valores de verdade
#   (em contextos numéricos 1 é True, enquanto 0 é False.
#
# EXTRA
#
# Há mais um literal especial que é usado em Python: o literal None . Este literal é um chamado NoneType objeto,
# e é utilizado para representar a ausência de um valor. Em breve, contar-lhe-emos mais sobre isso.

# Exercício 1
#
# Que tipos de literais são os dois exemplos seguintes?
#
# "Hello ", "007"       Ambos são strings/literais de strings.

# Que tipos de literais são os quatro exemplos seguintes?
#
# "1.5", 2.0, 528, False      O primeiro é uma string, o segundo é um literal numérico (um float), o terceiro é um
#                               literal numérico (um inteiro), e o quarto é um literal booleano

# Qual é o valor decimal do seguinte número binário?
#
# 1011        É 11, porque (2**0) + (2**1) + (2**3) = 11


#  ===================================================== Operadores ====================================================

# Um operador é um símbolo da linguagem de programação, que é capaz de operar sobre os valores.
#
# Por exemplo, tal como na aritmética, o sinal + (mais) é o operador que é capaz de adicionar dois números,
# dando o resultado da adição.
#
# Mas nem todos os operadores Python são tão óbvios como o sinal de mais, por isso vamos analisar alguns dos
# operadores disponíveis em Python, e explicaremos que regras regem a sua utilização, e como interpretar as
# operações que realizam.
#
# Começaremos pelos operadores que estão associados às operações aritméticas mais amplamente reconhecidas:
#
 +, -, *, /, //, %, **
#
#
# A ordem do seu aparecimento não é acidental. Falaremos mais sobre o assunto depois de termos passado por todos eles.
#
# Lembre-se: Os dados e os operadores, quando ligados entre si, formam expressões. A expressão mais simples é
# um literal em si.

# Um sinal ** (duplo asterisco) é um operador de exponenciação (potência). O seu argumento esquerdo é a base, o
# seu direito, o expoente.
#
# A matemática clássica prefere a notação com sobrescrito, tal como esta: 23. Os editores de texto puro não aceitam
# isso, por isso o Python usa ** ao invés, por exemplo, 2 ** 3.
#
# Dê uma vista de olhos aos nossos exemplos na janela do editor.
#
#
# Nota: rodeámos os asteriscos duplos com espaços nos nossos exemplos. Não é obrigatório, mas melhora a legibilidade do código.
#
# Os exemplos mostram uma característica muito importante de praticamente todos os operadores numéricos de Python.
#
# Execute o código e veja cuidadosamente os resultados que produz. Consegue ver alguma regularidade aqui?
#
#
# Lembre-se: É possível formular as seguintes regras com base neste resultado:
#
# ==> quando ambos os argumentos ** são inteiros, o resultado é também um inteiro;
# ==> quando pelo menos um argumento ** é um float, o resultado é também um float.
# Esta é uma distinção importante a lembrar.

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
# 8
# 8.0
# 8.0
# 8.0


# Um sinal * (asterisco) é um operador de multiplicação.
#
# Execute o código abaixo e verifique se a nossa regra de inteiro vs. float ainda está a funcionar.
#
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
#6
# 6.0
# 6.0
# 6.0
#
# Operadores aritméticos: divisão
# O sinal / (barra) é um operador de divisão.
#
# O valor em frente da barra é um dividendo, o valor por detrás da barra, um divisor.
#
# Execute o código abaixo e analise os resultados.
#
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
# 2.0
# 2.0
# 2.0
# 2.0
#
# Deve ver que existe uma exceção à regra.
#
# O resultado produzido pelo operador da divisão é sempre um float, independentemente de o resultado parecer ou não
# ser um float à primeira vista: 1 / 2, ou se se parecer com um inteiro puro: 2 / 1.
#
# Isto é um problema? Sim, é. Acontece por vezes que é realmente necessária uma divisão que forneça um valor
# inteiro, não um float.