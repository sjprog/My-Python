# ============================================================= Condicionais ===========================================
# Comparação: operador de igualdade

# Pergunta: são dois valores iguais?
#
# Para fazer esta pergunta, utiliza o operador == (igual igual).

# Não se esqueça desta importante distinção:

 = é um operador de atribuição, por exemplo, a = b atribui a com o valor de b;
 == é a questão são estes valores iguais?; a == b compara a e b.


# É um operador binário com ligação do lado esquerdo. Precisa de dois argumentos e verifica se são iguais.

# Igualdade: o operador igual a (==)


# A função == (igual a) compara os valores de dois operandos. Se forem iguais, o resultado da comparação é True. Se eles não forem iguais, o resultado da comparação é False.

# Veja a comparação de igualdade abaixo - qual é o resultado desta operação?

var == 0

# Note que não podemos encontrar a resposta se não soubermos qual o valor atualmente armazenado na variável var.

# Se a variável tiver sido alterada muitas vezes durante a execução do seu programa, ou o seu valor inicial
# for inserido a partir da consola, a resposta a esta pergunta pode ser dada apenas pelo Python, e apenas em runtime.

# Agora imagine um programador que sofre de insónias, e que tem de contar ovelhas pretas e brancas separadamente
# enquanto houver exatamente o dobro das ovelhas pretas do que das brancas.

# A questão será a seguinte:

black_sheep == 2 * white_sheep

# Devido à baixa prioridade do operador == , a questão deve ser tratada como equivalente a esta:

black_sheep == (2 * white_sheep)

# Então, vamos praticar a sua compreensão do operador == - consegue adivinhar o output do código abaixo?

var = 0  # Assigning 0 to var
print(var == 0)
# True

var = 1  # Assigning 1 to var
print(var == 0)
#  False

# Execute o código e verifique se estava certo.

# Desigualdade: o operador não igual a (!=)

# A função != (não igual) também compara os valores de dois operandos. Aqui está a diferença: se eles forem iguais, o resultado da comparação é False. Se eles não forem iguais, o resultado da comparação é True.

# Agora dê uma vista de olhos na comparação de desigualdade em baixo - consegue adivinhar o resultado desta operação?

var = 0  # Assigning 0 to var
print(var != 0)
#  False

var = 1  # Assigning 1 to var
print(var != 0)
# True

# ============================= Operadores de comparação: maior que

# Pode também fazer uma pergunta de comparação usando o operador > (maior que).
# Se quiser saber se há mais ovelhas pretas do que brancas, pode escrevê-lo da seguinte forma:

black_sheep > white_sheep  # Greater than

True confirma-o; False nega-o.

# ===================================== Operadores de comparação: maior que ou igual a

# O operador maior que tem outra variante especial, não estrita, mas é denotada de forma diferente da notação aritmética

clássica: >= (maior que ou igual a)

# Existem dois sinais subsequentes, não um.
# Ambos os operadores (estritos e não-estritos), bem como os outros dois discutidos na próxima secção, são operadores
# binários com ligação à esquerda, e a sua prioridade é maior do que a mostrada por == e !=.

# Se quisermos descobrir se temos ou não de usar um chapéu quente, fazemos a seguinte pergunta:

centigrade_outside ≥ 0.0  # Greater than or equal to

# =========================================== Operadores de comparação: menor que ou igual a

# Como já deve ter adivinhado, os operadores utilizados neste caso são: o < (less than) operator and its non-strict
# sibling: <= (menor que ou igual a).

# Veja este exemplo simples:

current_velocity_mph < 85  # Less than
current_velocity_mph ≤ 85  # Less than or equal to

# Vamos verificar se existe o risco de ser multado pela polícia rodoviária
# (a primeira pergunta é rigorosa, a segunda não).

# ======================================== Fazer uso das respostas

# O que pode fazer com a resposta (ou seja, o resultado de uma operação de comparação) que obtém do computador?
# Há pelo menos duas possibilidades: primeiro, pode memorizá-la (armazená-la numa variável) e utilizá-la mais tarde.
# Como se faz isso? Bem, utilizaria uma variável arbitrária como esta:

answer = number_of_lions >= number_of_lionesses

# O conteúdo da variável dar-lhe-á a resposta à pergunta feita.
# A segunda possibilidade é mais conveniente e muito mais comum: pode usar a resposta que obtém para tomar uma decisão
# sobre o futuro do programa.

# Precisa de uma instrução especial para este fim, e discutiremos isso muito em breve.

# ======================================= tabela de prioridades

Prioridade	        Operador
1	                 +, -	              unário
2	                 **
3	                 *, /, //, %
4	                 +, -	              binário
5	                 <, <=, >, >=
6	                 ==, !=

# ========================================== Exemplo

# Usando um dos operadores de comparação em Python, escreva um programa simples de duas linhas que toma o parâmetro
# n como input, que é um inteiro, e imprime False Se n for menor que 100, e True Se n for maior ou igual que 100.
#
# Não crie blocos if nenhuns (vamos falar deles muito em breve). Teste o seu código utilizando os dados que
# lhe fornecemos.

n = int(input("Enter a number: "))
print(n >= 100)
# Enter a number: 55
# False