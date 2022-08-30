

# ==================================================== Numpy =======================================================

 https://didatica.tech/o-pacote-numpy-python-para-machine-learning/

# O Numpy é um dos principais pacotes da linguagem Python para machine learning e inteligência artificial.
# Essencialmente, ele é um pacote para operações matemáticas, possuindo assim muitas funções prontas para estas operações.

import numpy  # importar o numpy
a = numpy.array([1, 2, 3])  # array com uma lista, elementos do mesmo tipo
print(a)
# [1 2 3]

import numpy as np  # np = apelida para numpy, outra forma de chamar
a = np.array([1, 2, 3])
print(a)
# [1 2 3]

a = np.array([(2, 5, 7), (5, 3, 9), (4, 6, 5)]) # pode usar agora o np
print(a)
# [[2 5 7]
#  [5 3 9]
#  [4 6 5]]

# uma funçào do np para criar matriz
a = np.zeros((4, 3)) # 4 colunas 3 elementos tudo com numeros 0
a = np.ones((4, 3))  # 4 colunas 3 elementos tudo com numeros 1
a = np.eyes(4) # cria uma matriz quadrada 4 linhas e 4 colunas, diagonal com 1, pode ser 10 por 10, basta trocar o 4 pelo numero desejado
print(a.max()) # fala qual o maior elemento da matriz
print(a.min()) # menor elemento da matriz
print(a.sum()) #  soma da matriz
print(a.mean()) # media dos elementos da matriz
print(a.std()) # desvio padrão da matriz

# ========================================== Arquivos com o Pandas - XLSX e CSV ===========================================

# crie um arquivo no exel com linhas e colunas.

import pandas as pd # pd = apelida para facilitar
dados = pd.read_excel('D:/tech/tech.xlsx') # tem que inverter a direção da barra, depois digita o nome do arquivo manualmente
print(dados.head()) # função do panda de cabeçalho ela so mostra as primeiras 5 linhas, caso queira mais linhas digite um o
# numero nas aspas do head

#  site com link de dados para baixar:
 https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results

# outro exemplo com arquivo csv, o arquivo baixado do link aberto nesse exemplo de csv
import pandas as pd
dados2 = pd.read_csv('D:/tech/athlete_events.csv') # da mesma forma porem com arquivo csv
print(dados2.head())

#========================== CASO DE ERRO, DIGITE ESSE CODIGO E IMPRIMA =================================
import pip
pip.main(["install", "openpyxl"])

# =================================ou esse========
pip install defusedxml


# ======================================= Introdução ao Pandas ===========================================================

import pandas as pd
alunos = {'Nome': ['Sidney', 'Pedro', 'Carla', 'Paula'], # vamos criar uma tebela, criando um dicionario e uma lista
          'Nota':[4, 5, 9, 5.8],
          'Aprovado':['Não', 'Sim', 'Sim', 'Não']}

dataframe = pd.DataFrame(alunos) # função do panda que transforma a entrada em dataframe
print(dataframe) # quando se cria dataframe automaticamente se cria indices
#      Nome  Nota Aprovado
# 0  Sidney   4.0      Não
# 1   Pedro   5.0      Sim
# 2   Carla   9.0      Sim
# 3   Paula   5.8      Não

objeto1 = pd.Series([2, 6, 9, 10, 5]) # criar uma lista series, e vetores unidimensionais
print(objeto1) # tambem adiciona indices
# 0     2
# 1     6
# 2     9
# 3    10
# 4     5
# dtype: int64

import numpy as np  # cria um array com o numpy
array1 = np.array([2, 6, 9, 10, 5]) # array dimensional
array2 = np.array([(2, 6, 9, 10, 5), (6, 5, 4, 8, 6)])  # cria o array bidimensional com dois
print(array1)
print(array2)
# [ 2  6  9 10  5]
# [[ 2  6  9 10  5]
#  [ 6  5  4  8  6]]

objeto2 = pd.Series(array1)  # criando um array no python so funcional pra uma dimensão
print(objeto2)
# 0     2
# 1     6
# 2     9
# 3    10
# 4     5

objeto2 = pd.Series(array2)  # duas dimensòes nao funciona
print(objeto2)
# dtype: int32
# ==================================================== Comandos úteis do Pandas =======================================================
import pandas as pd
alunosDic = {'Nome': ['Sidney', 'Pedro', 'Carla', 'Paula'], # vamos criar uma tebela, criando um dicionario e uma lista
          'Nota':[4, 5, 9, 5.8],
          'Aprovado':['Não', 'Sim', 'Sim', 'Não']}

alunosDF = pd.DataFrame(alunosDic)

print(alunosDF.head()) # mostra o cabeçlho

#     Nome  Nota Aprovado
# 0  Sidney   4.0      Não
# 1   Pedro   5.0      Sim
# 2   Carla   9.0      Sim
# 3   Paula   5.8      Não

print(alunosDF.shape) # mostra quantas linhas e quantas colunas temos
# (4, 3)

print(alunosDF.describe()) # mostra informaçoes sobre os dados numericos, mostra a media o minimo entre outras informações.
#      Nota
# count  4.00000
# mean   5.95000
# std    2.16256
# min    4.00000
# 25%    4.75000
# 50%    5.40000
# 75%    6.60000
# max    9.00000

# ================================================ Filtrando linhas e colunas no Pandas ==========================================

print(alunosDF['Nome'])
# 0    Sidney
# 1     Pedro
# 2     Carla
# 3     Paula
# Name: Nome, dtype: object

print(alunosDF['Nota'])
# 0    4.0
# 1    5.0
# 2    9.0
# 3    5.8
# Name: Nota, dtype: float64

print(alunosDF['Aprovado'])
# 0    Não
# 1    Sim
# 2    Sim
# 3    Não
# Name: Aprovado, dtype: object

print(alunosDF.loc[[0]]) # chama a linha 0, pode informar outros valores,  pode criar uma lista e colocar uma outra lista dentro
#      Nome  Nota Aprovado
# 0  Sidney   4.0      Não

print(alunosDF.loc[[0, 2]]) # chama a linha do indice 0 e do indice 2
#      Nome  Nota Aprovado
# 0  Sidney   4.0      Não
# 2   Carla   9.0      Sim

print(alunosDF.loc[[0,2,3]]) # chama a linha do indice 0 e do indice 2 e 3
#      Nome  Nota Aprovado
# 0  Sidney   4.0      Não
# 2   Carla   9.0      Sim
# 3   Paula   5.8      Não

print(alunosDF.loc[0:3]) # com dois pontos mostra da linha até a outra linha
#      Nome  Nota Aprovado
# 0  Sidney   4.0      Não
# 1   Pedro   5.0      Sim
# 2   Carla   9.0      Sim
# 3   Paula   5.8      Não

print(alunosDF.loc[alunosDF['Nome']=='Pedro']) # chama apenas oque tem o nome Pedro
#    Nome  Nota Aprovado
# 1  Pedro   5.0      Sim

print(alunosDF.loc[alunosDF['Nome']!='Pedro']) # chama apenas diferentes do nome pedro
#      Nome  Nota Aprovado
# 0  Sidney   4.0      Não
# 2   Carla   9.0      Sim
# 3   Paula   5.8      Não

print(alunosDF.loc[alunosDF['Aprovado']=='Sim']) # apenas os aprovados
#    Nome  Nota Aprovado
# 1  Pedro   5.0      Sim
# 2  Carla   9.0      Sim

# ===================================================== Cheat Sheet (Folha de dicas) - Pandas ==============================================

 #  Dicas sobre o pandas
 https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf


# ===================================================Solução do exercício - Encontrando Percentuais =======================================

