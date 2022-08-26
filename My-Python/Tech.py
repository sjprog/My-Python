

# =================================================== Numpy =====================================================

# https://didatica.tech/o-pacote-numpy-python-para-machine-learning/

# O Numpy é um dos principais pacotes da linguagem Python para machine learning e inteligência artificial.
# Essencialmente, ele é um pacote para operações matemáticas, possuindo assim muitas funções prontas para estas operações.

import numpy  # importar o numpy
a = numpy.array([1, 2, 3])  # array com uma lista, elementos do mesmo tipo

import numpy as np  # np = apelida para numpy, outra forma de chamar
a = np.array([1, 2, 3])

a = np.array([2, 5, 7), (5, 3, 9), (4, 6, 5)] # pode usar agora o np

# uma funçào do np para criar matriz
a = np.zeros((4, 3)) # 4 colunas 3 elementos tudo com numeros 0
a = np.ones((4, 3))  # 4 colunas 3 elementos tudo com numeros 1
a = np.eyes(4) # cria uma matriz quadrada 4 linhas e 4 colunas, diagonal com 1, pode ser 10 por 10, basta trocar o 4 pelo numero desejado
print(a.max()) # fala qual o maior elemento da matriz
print(a.min()) # menor elemento da matriz
print(a.sum()) #  soma da matriz
print(a.mean()) # media dos elementos da matriz
print(a.std()) # desvio padrão da matriz

# ========================================= Arquivos com o Pandas - XLSX e CSV =========================================

# crie um arquivo no exel com linhas e colunas.

import pandas as pd # pd = apelida para facilitar
dados = pd.read_excel('D:/tech/tech.xlsx') # tem que inverter a direção da barra, depois digita o nome do arquivo manualmente
print(dados.head()) # função do panda de cabeçalho ela so mostra as primeiras 5 linhas, caso queira mais linhas digite um o
# numero nas aspas do head

#  site com link de dados para baixar:
# https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results

# outro exemplo com arquivo csv, o arquivo baixado do link aberto nesse exemplo de csv
import pandas as pd
dados2 = pd.read_csv('D:/tech/athlete_events.csv') # da mesma forma porem com arquivo csv
print(dados2.head())

#========================== CASO DE ERRO, DIGITE ESSE CODIGO E IMPRIMA =================================
import pip
pip.main(["install", "openpyxl"])

# =================================ou esse========
pip install defusedxml