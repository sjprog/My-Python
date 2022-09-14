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