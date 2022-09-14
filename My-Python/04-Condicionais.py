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
