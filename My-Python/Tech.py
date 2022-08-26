

# =================================================== Numpy =====================================================

import numpy  # importar o numpy
a = numpy.array([1, 2, 3])  # array com uma lista, elementos do mesmo tipo

import numpy as np  # np = apelida para numpy, outra forma de chamar
a = np.array([1, 2, 3])

a = np.array([2, 5, 7), (5, 3, 9), (4, 6, 5)] # pode usar agora o np

# uma funçào do np para criar matriz
a = np.zeros((4, 3)) # 4 colunas 3 elementos tudo com numeros 0
a = np.ones((4, 3))  # 4 colunas 3 elementos tudo com numeros 1
a = np.eyes(4) # cria uma matriz quadrada 4 linhas e 4 colunas, diagonal com 1, pode ser 10 por 10, basta trocar o 4 pelo numero desejado
a.max() # fala qual o maior elemento da matriz
a.min() # menor elemento da matriz
a.sum() #  soma da matriz
a.mean() # media dos elementos da matriz
a.std() # desvio padrão da matriz
