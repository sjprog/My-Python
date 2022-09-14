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

# Um sinal // (dupla barra) é um operador de divisão inteira. Difere do operador padrão / em dois detalhes:
#
# o seu resultado não tem a parte fracionada - está ausente (para inteiros), ou é sempre igual a zero (para floats);
# isto significa que os resultados são sempre arredondados;
# está em conformidade com a regra inteiro vs. float.
# Execute o exemplo abaixo e veja os resultados:
#
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
# 2
# 2.0
# 2.0
# 2.0
#
# Como se pode ver, a divisão inteiro por inteiro dá um resultado inteiro. Todos os outros casos produzem floats.
#
#
# Vamos fazer alguns testes mais avançados.
#
# Veja o seguinte snippet:
#
print(6 // 4)
print(6. // 4)
# 1
# 1.0
#
# Imagine que usámos / em vez de // - consegue prever os resultados?
#
# Sim, seria 1.5 em ambos os casos. Isso é claro.
#
# Mas que resultados devemos esperar com // divisão?
#
# Execute o código e veja por si mesmo.

# O que obtemos são dois uns - um inteiro e um float.
#
# O resultado da divisão inteira é sempre arredondado para o valor inteiro mais próximo, que é inferior ao
# resultado real (não arredondado).
#
# Isto é muito importante: o arredondamento vai sempre para o número inteiro menor.
#
#
# Veja o código abaixo e tente prever os resultados mais uma vez:
#
print(-6 // 4)
print(6. // -4)
# -2
# -2.0
#
# Nota: alguns dos valores são negativos. Isto irá obviamente afetar o resultado. Mas como?
#
# O resultado são dois dois negativos. O resultado real (não arredondado) é -1.5 em ambos os casos.
# No entanto, os resultados são sujeitos a arredondamento. O arredondamento vai para o menor valor inteiro, e o
# menor valor inteiro é -2, logo: -2 e -2.0.
#
# NOTA
#
# A divisão inteira também pode ser chamada floor division. Definitivamente, no futuro, deparar-se-á com este termo.


# O próximo operador é bastante peculiar, visto não ter equivalente entre os operadores aritméticos tradicionais.
#
# A sua representação gráfica em Python é o sinal % (percentagem), o que pode parecer um pouco confuso.
#
# Tente pensar nisto como uma barra (operador de divisão) acompanhada por dois pequenos círculos engraçados.
#
# O resultado do operador é um remainder (resto) deixado após a divisão inteira.
#
# Por outras palavras, é o valor que sobrou depois de dividir um valor por outro para produzir um quociente inteiro.
#
# Nota: o operador às vezes é chamado modulo noutras linguagens de programação.
#
# Dê uma vista de olhos no snippet - tente prever o seu resultado e, em seguida, execute-o:
#
print(14 % 4)
# 2
#
# Como pode ver, o resultado é dois. Esta é a razão:
#
# ==> 14 // 4 dá 3 → este é o quociente inteiro;
# ==> 3 * 4 dá 12 → como resultado da multiplicação de quocientes e divisores;
# ==> 14 - 12 dá 2 → este é o resto.
#
# Este exemplo é um pouco mais complicado:
#
print(12 % 4.5)
# 3,0 - não 3 mas 3.0 (a regra ainda funciona: 12 // 4.5 dá 2.0; 2.0 * 4.5 dá 9.0; 12 - 9.0 dá 3.0)

# Operadores: como não dividir
# Como provavelmente sabe, === (a divisão por zero não funciona.) ===
#
# Não tente:
#
# ==> executar uma divisão por zero;
# ==> executar uma divisão inteira por zero;
# ==> encontrar um remainder de uma divisão por zero.


# O operador de adição é o sinal + (mais), que está totalmente de acordo com os padrões matemáticos.
#
# Novamente, dê uma vista de olhos no snippet do programa em baixo:
#
print(-4 + 4)
print(-4. + 8)
# 0
# 4.0
#
# O resultado não deve ser nada surpreendente. Execute o código para o verificar.
#
#
# O operador de subtração, operadores unários e binários
# O operador de subtração é obviamente o sinal - (menos), embora deva notar que este operador também tem outro
# significado - ele pode alterar o sinal de um número.
#
# Esta é uma grande oportunidade para apresentar uma distinção muito importante entre operadores unários e binários.
#
# Em aplicações de subtração, o operador menos espera dois argumentos: o da esquerda (um minuendo em termos aritméticos)
# e o da direita (um subtraendo).
#
# Por esta razão, o operador de subtração é considerado um dos operadores binários, assim como os operadores de
# adição, multiplicação e divisão.
#
# Mas o operador menos pode ser usado de uma forma diferente (unária) - veja a última linha do snippet em baixo:
#
print(-4 - 4)
print(4. - 8)
print(-1.1)
# -8
# -4.0
# -1.1
#
# A propósito: há também um operador + unário. Pode utilizá-lo assim:
#
print(+2)
# 2
#
# O operador preserva o sinal de seu único argumento - o correto.
#
# Embora tal construção seja sintaticamente correta, a sua utilização não faz muito sentido, e seria difícil
# encontrar uma boa razão para o fazer.


# Os operadores e as suas prioridades

# Até agora, temos tratado cada operador como se não tivesse qualquer ligação com os outros. Obviamente, uma
# situação tão ideal e simples é uma raridade na programação real.
#
# Além disso, encontrará muito frequentemente mais do que um operador numa só expressão, e então esta presunção
# já não é tão óbvia.
#
# Considere a seguinte expressão:
#
# 2 + 3 * 5
#
# Provavelmente lembra-se da escola que as multiplicações precedem as adições.
#
# Deve certamente lembrar-se que primeiro deve multiplicar 3 por 5 e, mantendo o 15 na sua memória, depois
# adicioná-los a 2, obtendo assim o resultado de 17.
#
# O fenómeno que leva alguns operadores a agir antes de outros é conhecido como a hierarquia de prioridades.
#
# O Python define com precisão as prioridades de todos os operadores, e assume que os operadores de maior
# (mais alta) prioridade realizam as suas operações antes dos operadores de menor prioridade.
#
# Portanto, se sabe que * tem uma prioridade maior do que +, o cálculo do resultado final deve ser óbvio.
#
#
# Os operadores e as suas ligações
# A ligação do operador determina a ordem dos cálculos efetuados por alguns operadores com igual prioridade,
# colocados lado a lado numa só expressão.
#
# A maioria dos operadores de Python têm ligação do lado esquerdo, o que significa que o cálculo da expressão
# é realizado da esquerda para a direita.
#
# Este exemplo simples mostrar-lhe-á como funciona. Veja:
#
print(9 % 6 % 2)
#
#
# Há duas formas possíveis de avaliar esta expressão:
#
# ==> da esquerda para a direita: primeiro 9 % 6 dá 3e, em seguida, 3 % 2 dá 1;
# ==> da direita para a esquerda: primeiro 6 % 2 dá 0e, em seguida, 9 % 0 causa um erro fatal.
#
# Execute o exemplo e veja o que obtém.
#
# O resultado deve ser 1. Este operador tem ligação do lado esquerdo. Mas há uma exceção interessante.

# Repita a experiência, mas agora com exponenciação.
#
# Use este snippet de código:
#
print(2 ** 2 ** 3)
# 256
#
# Os dois resultados possíveis são:
#
# ==> 2 ** 2 → 4; 4 ** 3 → 64
# ==> 2 ** 3 → 8; 2 ** 8 → 256
#
# Execute o código. O que vê?
#
# O resultado mostra claramente que === (o operador de exponenciação utiliza a ligação do lado direito.) ===

# Lista de prioridades
# Uma vez que é novo nos operadores Python, não queremos apresentar neste momento a lista completa de prioridades
# dos operadores.
#
# Em vez disso, vamos mostrar-lhe a sua forma truncada, e vamos expandi-la de forma consistente à medida que
# introduzimos novos operadores.
#
# Veja a tabela abaixo:
#

Prioridade	       Operador
1	               +, -	                       unário
2	               **
3	               *, /, //, %
4	               +, -	                       binário


# Operadores e parêntesis

# Claro, é sempre permitido utilizar parêntesis, o que pode alterar a ordem natural de um cálculo.
#
# De acordo com as regras aritméticas, as subexpressões entre parêntesis são sempre calculadas em primeiro lugar.
#
# Pode-se usar tantos parêntesis quantos forem necessários, e são frequentemente usados para melhorar a
# egibilidade de uma expressão, mesmo que não alterem a ordem das operações.
#
# Um exemplo de uma expressão com vários parêntesis é este:
#
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# 10.0
#
# Tente calcular o valor que é impresso para a consola. Qual é o resultado da função print() ?

#  ================================================== RESUMO ===========================================================

# 1. Uma expressão é uma combinação de valores (ou variáveis, operadores, chamadas a funções - em breve aprenderá sobre
#   elas) que avalia a um valor, por exemplo, 1 + 2.
#
# 2. Os operadores são símbolos especiais ou keywords capazes de operar sobre os valores e realizar operações
#   (matemáticas), por exemplo, o * operador multiplica dois valores: x * y.
#
# 3. Operadores aritméticos em Python: + (adição), - (subtração), * (multiplicação), /
#   (divisão clássica - devolve sempre um float), % (módulo - divide o operando esquerdo pelo operando direito e
#   devolve o resto da operação, por exemplo, 5 % 2 = 1), ** (exponenciação - operando esquerdo elevado à potência do
#   operando direito, por exemplo, 2 ** 3 = 2 * 2 * 2 = 8), // (divisão por piso/inteiro - devolve um número resultante
#   da divisão, mas arredondado para baixo para o número inteiro mais próximo, por exemplo 3 // 2.0 = 1.0)
#
# 4. Um operador unário é um operador com apenas um operando, por exemplo, -1, ou +3.
#
# 5. Um operador binário é um operador com dois operandos, por exemplo, 4 + 5, ou 12 % 5.
#
# 6. Alguns operadores atuam antes de outros - a hierarquia de prioridades:
# ==> unário + e - têm a prioridade mais alta
# ==> depois: **, depois: *, /, e %e, depois, a prioridade mais baixa: binário + e -.

# 7. Subexpressões entre parêntesis são sempre calculadas em primeiro lugar, por exemplo, 15 - 1 * (5 * (1 + 2)) = 0.
#
# 8. O operador de exponenciação utiliza ligação do lado direito, por exemplo 2 ** 2 ** 3 = 256.

print((2 ** 4), (2 * 4.), (2 * 4))
# 16 8.0 8

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
# -0.5 0.5 0 -1

print((2 % -4), (2 % 4), (2 ** 3 ** 2))
# -2 2 512


#  ========================================================= INPUT =====================================================

# Vamos agora apresentar-lhe uma função completamente nova, que parece ser um reflexo da boa e velha função print() .

# Porquê? Bem, print() envia dados para a consola.

# A nova função obtém dados dela.

# print() não tem resultado utilizável. O significado da nova função é devolver um resultado muito utilizável.

# A função é chamada input(). The name of the function says everything.

# A tecla programável input() function is able to read data entered by the user and to return the same data to the
# running program.

# O programa pode manipular os dados, tornando o código genuinamente interativo.

# Virtualmente todos os programas lêem e processam dados. Um programa que não recebe um input do utilizador é um
# programa surdo.

# Dê uma vista de olhos no nosso exemplo:

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")


# Isto mostra um caso muito simples de utilização da função input() .

# Nota:

# ===> O programa pede ao utilizador que introduza alguns dados da consola (muito provavelmente utilizando um teclado,
#       embora também seja possível introduzir dados utilizando voz ou imagem);
# ===> a função input() é invocada sem argumentos (esta é a forma mais simples de usar a função); a função irá mudar
#       a consola para o modo de input; verá um cursor a piscar, e poderá introduzir algumas keystrokes, terminando com a
#       tecla Enter; todos os dados introduzidos serão enviados para o seu programa através do resultado da função;
# ===> nota: é necessário atribuir o resultado a uma variável; isto é crucial - a falta desta etapa fará com que os
#       dados introduzidos se percam;
# ===> então, utilizamos a função print() para fazer output dos dados que obtemos, com algumas observações adicionais.

# A função input() pode fazer algo mais: pode incitar o utilizador sem qualquer ajuda de print().

# Modificámos um pouco o nosso exemplo, olha para o código:

# anything = input("Tell me anything...")
# print("Hmm...", anything, "...Really?")

# Nota:

# a keyword input() é invocada com um argumento - é uma string contendo uma mensagem;
# a mensagem será exibida na consola antes de ser dada ao utilizador a oportunidade de introduzir qualquer coisa;
# input() fará então o seu trabalho.
# Esta variante da invocação input() simplifica o código e torna-o mais claro.

# Já o dissemos, mas deve ser afirmado uma vez mais sem ambiguidade: o resultado da função input() é uma string.

# Uma string contendo todos os carateres que o utilizador introduz a partir do teclado. Não é um inteiro ou um float.

# Isto significa que não deve usá-la como um argumento de qualquer operação aritmética, por exemplo, não pode usar
# estes dados para os elevar ao quadrado, dividi-los por qualquer coisa, ou dividir qualquer coisa por eles.

anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

#  ====================================================

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# Concatenação


# O sinal + (mais), quando aplicado a duas strings, torna-se um operador de concatenação:

string + string

# Simplesmente concatena (cola) duas strings numa. Claro que, tal como o seu irmão aritmético, pode ser usado
# mais de uma vez numa expressão, e em tal contexto comporta-se de acordo com a ligação do lado esquerdo.

# Em contraste com o seu irmão aritmético, o operador da concatenação não é comutativo, ou seja "ab" + "ba" não
# é o mesmo que "ba" + "ab".

# Não se esqueça - se quiser que o sinal + seja um concatenador, não um adicionador, deve assegurar-se de que
# ambos os seus argumentos são strings.

# Não se podem misturar tipos aqui.

# Este programa simples mostra o sinal + na sua segunda utilização:

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
# May I have your first name, please? SIDNEY
# May I have your last name, please? JUNIO
# Thank you.

# Your name is SIDNEY JUNIO.


# Replicação


# O sinal * (asterisco), quando aplicado a uma string e número (ou um número e string, visto permanecer comutativo
# nesta posição) torna-se um operador de replicação:

string * number
number * string

# Replica a string o mesmo número de vezes especificado pelo número.

# Por exemplo:

"James" * 3 dá "JamesJamesJames"
3 * "an" dá "ananan"
5 * "2" (ou "2" * 5) dá "22222" (não 10!)

# LEMBRE-SE

# Um número menor ou igual a zero produz uma string vazia.

# Este programa simples "desenha" um retângulo, fazendo uso de um antigo operador (+) num novo papel:

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
# +----------+
# |          |
# |          |
# |          |
# |          |
# |          |
# +----------+

# Note a forma como utilizámos os parêntesis na segunda linha do código.

# Tente praticar para criar outras formas ou a sua própria obra de arte!

# Nota: usando + para concatenar strings permite construir o output de uma forma mais precisa do que com uma função
# pura print() , mesmo que enriquecida com os end= e sep= argumentos de keyword.

# Execute o código e veja se o output corresponde às suas previsões.


# Conversão de tipo: str()


# Já sabe como utilizar as funções int() e float() para converter uma string num número.

# Este tipo de conversão não é uma rua de sentido único. Também se pode converter um número numa string,
# o que é muito mais fácil e seguro - esta operação é sempre possível.

# Uma função capaz de o fazer chama-se str():

str(number)

# Para ser honesto, pode fazer muito mais do que apenas transformar números em strings, mas isso pode ficar para mais tarde.

# O “triângulo de ângulo retângulo” novamente
# Aqui está o nosso programa “triângulo de ângulo retângulo” novamente:

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
# Input first leg length: 1.80
# Input second leg length: 1.54
# Hypotenuse length is 2.3688815926508444

# Modificámo-lo um pouco para lhe mostrar como a função str() funciona. Graças a isso, podemos passar
# todo o resultado para a função print() como uma string, esquecendo as vírgulas.

# Deu alguns passos sérios no seu caminho para a programação em Python.

# Já conhece os tipos de dados básicos, e um conjunto de operadores fundamentais. Sabe como organizar o
# output e como obter dados do utilizador. Estas são bases muito fortes para o Módulo 3. Mas antes de passarmos ao
# módulo seguinte, vamos fazer alguns laboratórios, e recapitular tudo o que aprendeu nesta secção.

a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("\nThat's all, folks!")
# Enter first value: 50
# Enter second value: 30
# Addition: 80.0
# Subtraction: 20.0
# Multiplication: 1500.0
# Division: 1.6666666666666667
#
# That's all, folks!

# =======================================================

x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)
# Enter value for x: 2
# y = 0.4137931034482759

# =======================================================

# A sua tarefa é preparar um código simples capaz de avaliar o tempo final de um período de tempo,
# dado como um número de minutos (pode ser arbitrariamente grande). O tempo inicial é dado como um par de horas (0.. 23) e minutos (0.. 59). O resultado tem de ser impresso para a consola.

# Por exemplo, se um evento começar às 12:17 e durar 59 minutos, ele terminará às 13:16.

# Não se preocupe com quaisquer imperfeições no seu código - não faz mal se aceitar um tempo inválido - o
# mais importante é que o código produza resultados válidos para dados de input válidos.

# Teste o seu código com cuidado. Dica: utilizar o operador % pode ser a chave para o sucesso.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')
# Starting time (hours): 2
# Starting time (minutes): 30
# Event duration (minutes): 40
# 3:10

# ======================================================= RESUMO ======================================================

# 1. A função print() envia dados para a consola, enquanto a função input() obtém dados da consola.

# 2. O método input() vem com um parâmetro opcional: a string prompt. Permite-lhe escrever uma mensagem antes do
# input do utilizador, por exemplo

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

# 3. Quando a função input() é chamada, o fluxo do programa é interrompido, o símbolo de prompt continua a
# piscar (pede ao utilizador para tomar medidas quando a consola é mudada para o modo de input) até o utilizador
# ter introduzido um input e/ou premido a tecla Enter.

# NOTA

# Pode testar a funcionalidade da função input() em todo o seu scope localmente na sua máquina. Por razões de
#  otimização de recursos, limitámos o tempo máximo de execução do programa no Edube a alguns segundos. Vá à Sandbox,
#  copie-cole o snippet acima, execute o programa, e não faça nada - espere apenas alguns segundos para ver o
#  que acontece. O seu programa deve ser interrompido automaticamente após um breve momento. Agora abra o IDLE,
#  e execute lá o mesmo programa - consegue ver a diferença?

# Dica: a característica acima mencionada da função input() pode ser utilizada para solicitar o utilizador a
# terminar um programa. Veja o código em baixo:

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

# 3. O resultado da função input() é uma string. Podem adicionar-se strings umas às outras usando a concatenação
# (+) operador. Verifique este código:

num_1 = input("Enter the first number: ") # Enter 12
num_2 = input("Enter the second number: ") # Enter 21
print(num_1 + num_2) # the program returns 1221

# 4. Também pode multiplicar (* - replicação) strings, por exemplo:

my_input = input("Enter something: ") # Example input: hello
print(my_input * 3) # Expected output: hellohellohello

# =======================================================

x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")
# 55

# =======================================================

x = input("Enter a number: ") # The user enters 2
print(type(x))
# <class 'str'>