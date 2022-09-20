# ================================================= Lógica de computador ===============================================

# Utilizámos a conjunção and, o que significa que ir dar um passeio depende do cumprimento simultâneo destas duas
# condições. Na linguagem da lógica, tal ligação de condições é chamada uma conjunção. E agora outro exemplo:

# Se estiveres no centro comercial ou eu estiver no centro comercial, um de nós vai comprar um presente para a mãe.

# A aparência da palavra or significa que a compra depende de pelo menos uma destas condições. Em lógica, tal
# composto é chamado uma disjunção.

# É evidente que o Python deve ter operadores para construir conjunções e disjunções. Sem eles, o poder expressivo
# da linguagem ficaria substancialmente enfraquecido. Eles são chamados operadores lógicos.

# ======================================================= and

# Um operador de conjunção lógica em Python é a palavra and. É um operador binário com uma prioridade que é inferior
# à expressa pelos operadores de comparação. Permite-nos codificar condições complexas sem o uso de parêntesis
# como esta:

counter > 0 and value == 100

# O resultado fornecido pelo operador and pode ser determinado com base na tabela da verdade.

# Se considerarmos a conjunção de A e B, o conjunto de valores possíveis de argumentos e valores correspondentes
# da conjunção parece ser o seguinte:

Argumento A	                    Argumento B	                                A e B
False	                              False                                 	False
False	                              True	                                    False
True                                False	                                    False
True	                              True	                                    True

# ====================================================== or

# Um operador de disjunção é a palavra or. É um operador binário com uma prioridade inferior a and
# ( assim como + comparado com *). A sua tabela de verdade é a seguinte:

Argumento A	                             Argumento B	                         A ou B
False	                                     False	                                 False
False	                                     True	                                 True
True	                                     False	                                 True
True	                                     True	                                 True

# ====================================================== not

# Além disso, há outro operador que pode ser aplicado para construir condições. É um operador unário que executa
# uma negação lógica. O seu funcionamento é simples: transforma a verdade em falsidade e a falsidade em verdade.

# Este operador é escrito como a palavra not, e a sua prioridade é muito alta: a mesma que o unário + e -. A sua
# tabela de verdade é simples:

Argumento	                                     not Argumento
False	                                         True
True	                                         False

# ===================================================================== Expressões lógicas

# Vamos criar uma variável chamada var e atribuir 1 a ela. As seguintes condições são equivalentes em pares:

# # Example 1:
print(var > 0)
print(not (var <= 0))

# # Example 2:
print(var != 0)
print(not (var == 0))

# Pode estar familiarizado com as leis de De Morgan. Dizem que:

# A negação de uma conjunção é a disjunção das negações.

# A negação de uma disjunção é a conjunção das negações.

# Vamos escrever a mesma coisa usando Python:

not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)

# ======================================================================Valores lógicos vs. bits únicos

# Os operadores lógicos tomam os seus argumentos como um todo, independentemente da quantidade de bits que contenham.
#  Os operadores só estão conscientes do valor: zero (quando todos os bits são redefinidos) significa False; não zero
#  (quando pelo menos um bit está definido) significa True.

# O resultado das suas operações é um destes valores: False ou True. Isto significa que este snippet irá atribuir
# o valor True à variável j se i não for zero; caso contrário, será False.

i = 1
j = not not i

# ================================================================ Operadores bitwise

# No entanto, existem quatro operadores que lhe permitem manipular bits únicos de dados. São chamados operadores
# bitwise.

# Abrangem todas as operações que mencionámos anteriormente no contexto lógico, e um operador adicional. Este
# é o operador xor (como em exclusivo ou), e é denotado como ^ (acento circunflexo).

# Aqui estão todos eles:

& (e comercial) - conjunção bitwise;
| (barra) - disjunção bitwise;
~ (til) - negação bitwise;
^ (acento circunflexo) - bitwise exclusive ou (xor).

# ============================================================== Operações bitwise (&, |, e ^)

Argumento A	               Argumento B	           A & B	            A | B	           A ^ B
0	                            0	                 0	                  0	                 0
0	                            1	                 0	                  1	                 1
1	                            0	                 0	                  1	                 1
1	                            1	                 1	                  1	                 0

# =================================================================== Operações bitwise (~)

Argumento	       ~ Argumento
0	                     1
1	                     0

# Vamos facilitar as coisas:

# & requer exatamente dois 1para fornecer 1 como resultado;
# | requer pelo menos um 1 para fornecer 1 como resultado;
# ^ requer exatamente um 1 para fornecer 1 como resultado.

# ========================================================Operações lógicas versus bit: continuação

# Vamos agora mostrar-lhe um exemplo da diferença de funcionamento entre as operações lógicas e as operações de
# bit. Vamos assumir que as seguintes atribuições foram realizadas:

i = 15
j = 22

# Se assumirmos que os números inteiros são armazenados com 32 bits, a imagem bitwise das duas variáveis será a seguinte:

i: 00000000000000000000000000001111
j: 00000000000000000000000000010110

# A atribuição é dada:

log = i and j

# Estamos a lidar aqui com uma conjunção lógica. Vamos traçar o curso dos cálculos. Ambas as variáveis i e j não
# são zeros, por isso serão consideradas para representar True. Consultando a tabela da verdade para o operador
# and , podemos ver que o resultado será True. Nenhuma outra operação é realizada.

log: True

# Agora a operação bitwise - aqui está ela:

bit = i & j

# O operador & operará com cada par de bits correspondentes separadamente, produzindo os valores dos bits relevantes
# do resultado. Portanto, o resultado será o seguinte:

i	00000000000000000000000000001111
j	00000000000000000000000000010110
bit = i & j	00000000000000000000000000000110
# Estes bits correspondem ao valor inteiro de seis.

# Vejamos agora os operadores de negação. Primeiro, o lógico:

logneg = not i

# A variável logneg será definida como False - nada mais precisa de ser feito.

# A negação bitwise é assim:

bitneg = ~i

# Pode ser um pouco surpreendente: o valor da variável bitneg é -16. Isto pode parecer estranho, mas
# não é de todo. Se desejar saber mais, deve verificar o sistema de numeração binária e as regras que regem os números
#  complementares de dois.

i	00000000000000000000000000001111
bitneg = ~i	11111111111111111111111111110000

# Cada um destes operadores de dois argumentos pode ser utilizado de forma abreviada. Estes são os exemplos
# das suas notações equivalentes:

x = x & y	x &= y
x = x | y	x |= y
x = x ^ y	x ^= y

# ======================================== Como lidamos com bits individuais?

# Vamos agora mostrar-lhe aquilo para que pode utilizar os operadores bitwise. Imagine que é um programador
# obrigado a escrever uma parte importante de um sistema operativo. Foi informado de que tem permissão para usar
# uma variável atribuída da seguinte maneira:

flag_register = 0x1234

# A variável armazena as informações sobre vários aspectos da operação do sistema. Cada bit da variável armazena um
# valor yes/no. Também lhe foi dito que apenas um destes bits é seu - o terceiro (lembre-se que os bits são numerados
# a partir do zero, e o bit número zero é o mais baixo, enquanto o mais alto é o número 31). Os bits restantes não
# podem ser alterados, porque se destinam a armazenar outros dados. Aqui está o seu bit marcado pela letra x:

flag_register = 0000000000000000000000000000x000

# Pode ser confrontado com as seguintes tarefas:

# 1. Verifique o estado do seu bit - quer descobrir o valor do seu bit; comparar a variável inteira com zero
# não fará nada, porque os bits restantes podem ter valores completamente imprevisíveis, mas pode usar a
# seguinte propriedade de conjunção:

x & 1 = x
x & 0 = 0

# Se aplicar a & operação à flag_register variável juntamente com a seguinte imagem de bit:

00000000000000000000000000001000

# (observe o 1 na posição do seu bit) como resultado, obtém uma das seguintes strings de bit:

00000000000000000000000000001000 se o seu bit foi definido para 1
00000000000000000000000000000000 se o seu bit foi redefinido para 0

# Tal sequência de zeros e uns, cuja tarefa é agarrar o valor ou alterar os bits selecionados, é chamada de bit mask.
#
# Vamos criar uma bit mask para detetar o estado do seu bit. Deve apontar para o terceiro bit. Esse bit tem o peso
# de 23 = 8. Uma mask adequada poderia ser criada através da seguinte declaração:

the_mask = 8

# Também pode fazer uma sequência de instruções dependendo do estado do seu bit i aqui está:
#
if flag_register & the_mask:
    # My bit is set.
else:
    # My bit is reset.

# 2. Redefina o seu bit - atribua um zero ao bit enquanto todos os outros bits devem permanecer inalterados;
# utilizemos a mesma propriedade de conjunção como antes, mas utilizemos uma mask ligeiramente diferente - exatamente
# como em baixo:

11111111111111111111111111110111

# Observe que a mask foi criada como resultado da negação de todos os bits de the_mask variável. Redefinir o bit é simples, e parece-se com isto (escolha o que mais gostar):

flag_register = flag_register & ~the_mask
flag_register &= ~the_mask

# 3. Defina o seu bit - atribua um 1 ao seu bit, enquanto todos os bits restantes devem permanecer inalterados; use
# a seguinte propriedade de disjunção:

x | 1 = 1
x | 0 = x

# Agora está pronto para definir o seu bit com uma das seguintes instruções:

flag_register = flag_register | the_mask
flag_register |= the_mask

# 4. Negue o seu bit - substitua um 1 com um 0 e um 0 com um 1. Pode utilizar uma propriedade interessante do
# xor operador:

x ^ 1 = ~x
x ^ 0 = x

# e negue o seu bit com as seguintes instruções:

flag_register = flag_register ^ the_mask
flag_register ^= the_mask

# =============================================Shifting binário à esquerda e shifting binário à direita

# O Python oferece mais uma operação relacionada a bits individuais: shifting (deslocamento). Isto é aplicado apenas
# a valores inteiros, e não se deve utilizar floats como argumentos.

# Você já aplica esta operação com alguma frequência, e bastante inconscientemente. De que forma multiplica
# qualquer número por dez? Dê uma vista de olhos:

12345 × 10 = 123450

# Como se pode ver, multiplicar por dez é, de facto, um shifting de todos os dígitos para a esquerda, preenchendo
# a lacuna resultante com zero.

# Divisão por dez? Dê uma vista de olhos:

12340 ÷ 10 = 1234

# Dividir por dez não é mais do que um shifting dos dígitos para a direita

# O mesmo tipo de operação é realizado pelo computador, mas com uma diferença: como dois é a base para números
# binários (não 10), o shifting de um valor um bit para a esquerda corresponde assim a multiplicá-lo por dois;
# respetivamente, o shifting um bit para a direita é o mesmo que dividí-lo por dois (repare que o bit mais à
# direita é perdido).

# Os operadores shift em Python são um par de dígrafos: << e >>, sugerindo claramente em que direção a mudança
# irá ocorrer.

value << bits
value >> bits

# O argumento à esquerda destes operadores é um valor inteiro cujos bits são deslocados. O argumento à direita
# determina o tamanho do shifting.

# Isto demonstra que esta operação não é certamente comutativa.

# A prioridade destes operadores é muito alta. Vê-los-á na tabela de prioridades atualizada, que lhe mostraremos
# no final desta secção.

# Dê uma vista de olhos nas mudanças na janela do editor.

# A invocação print() final produz o seguinte output:

17 68 8


# Nota:

17 >> 1 → 17 // 2 (17 divido por baixo por 2 à potência de 1) → 8 (shifting para a direita por um bit é o mesmo que a divisão inteira por dois)
17 << 2 → 17 * 4 17 multiplicado por 2 à potência de 2) → 68 (shifting para a esquerda por dois bits é o mesmo que a multiplicação de inteiros por quatro)

# E aqui está a tabela de prioridades atualizada, contendo todos os operadores introduzidos até agora:

 Prioridade	             Operador
 1	                      ~, +, -	             unário
 2	                      **
 3	                      *, /, //, %
 4	                      +, -	                 binário
 5	                      <<, >>
 6	                      <, <=, >, >=
 7	                      ==, !=
 8	                      &
 9	                      |
 10	                      =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=

#  ===========================================================
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
# 17 68 8

#  =========================================================== RESUMO ==============================================

# 1. O Python suporta os seguintes operadores lógicos:

# ===> and → se ambos os operandos forem verdadeiros, a condição é verdadeira, por exemplo, (True and True) é True,
# ===> or → se algum dos operandos for verdadeiro, a condição é verdadeira, por exemplo, (True or False) é True,
# ===> not → retorna falso se o resultado for verdadeiro, e retorna verdadeiro se o resultado for falso, por exemplo,
# not True é False.

# 2. Pode utilizar operadores bitwise para manipular bits únicos de dados. Os seguintes dados de amostra:

# ===> x = 15, que é 0000 1111 em binário,
# ===> y = 16, que é 0001 0000 em binário.

# serão utilizados para ilustrar o significado de operadores bitwise em Python. Analise os exemplos em baixo:

# ===> & faz um bitwise and, por exemplo, x & y = 0, que é 0000 0000 em binário,
# ===> | faz um bitwise ou, por exemplo, x | y = 31, que é 0001 1111 em binário,
# ===> ˜  faz um bitwise não, por exemplo, ˜ x = 240*, que é 1111 0000 em binário,
# ===> ^ faz um bitwise xor, por exemplo, x ^ y = 31, que é 0001 1111 em binário,
# ===> >> faz um bitwise right shift, por exemplo, y >> 1 = 8, que é 0000 1000 em binário,
# ===> << faz um bitwise left shift, por exemplo, y << 3 = , que é 1000 0000 em binário,

# ===> * -16 (decimal do complemento assinado de 2) — leia mais sobre a Two's complement operation
# (operação de complemento de dois).

#  ===========================================================

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))
# False

#  ===========================================================

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
# 0 5 -5 1 1 16