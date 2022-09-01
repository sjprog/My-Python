

# ==================================================== Numpy =======================================================

 https://didatica.tech/o-pacote-numpy-python-para-machine-learning/

# O Numpy é um dos principais pacotes da linguagem Python para machine learning e inteligência artificial.
# Essencialmente, ele é um pacote para operações matemáticas, possuindo assim muitas funções
# prontas para estas operações.

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
a = np.eyes(4) # cria uma matriz quadrada 4 linhas e 4 colunas, diagonal com 1, pode ser 10 por 10, basta
# trocar o 4 pelo numero desejado
print(a.max()) # fala qual o maior elemento da matriz
print(a.min()) # menor elemento da matriz
print(a.sum()) #  soma da matriz
print(a.mean()) # media dos elementos da matriz
print(a.std()) # desvio padrão da matriz

# ======================================== Arquivos com o Pandas - XLSX e CSV ==========================================

# crie um arquivo no exel com linhas e colunas.

import pandas as pd # pd = apelida para facilitar
dados = pd.read_excel('D:/tech/tech.xlsx') # tem que inverter a direção da barra, depois digita o nome do
# arquivo manualmente
print(dados.head()) # função do panda de cabeçalho ela so mostra as primeiras 5 linhas, caso queira
# mais linhas digite um o
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


# ======================================== Introdução ao Pandas ========================================================

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
# ============================================ Comandos úteis do Pandas ================================================
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

print(alunosDF.describe()) # mostra informaçoes sobre os dados numericos, mostra a media
# o minimo entre outras informações.
#      Nota
# count  4.00000
# mean   5.95000
# std    2.16256
# min    4.00000
# 25%    4.75000
# 50%    5.40000
# 75%    6.60000
# max    9.00000

# ===================================== Filtrando linhas e colunas no Pandas ==========================================

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

print(alunosDF.loc[[0]]) # chama a linha 0, pode informar outros valores, pode criar uma lista
# e colocar uma outra lista dentro
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

# ===================================== Cheat Sheet (Folha de dicas) - Pandas ==========================================

 #  Dicas sobre o pandas
 https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf


# =========================================== Manipulando linhas com o Pandas ==========================================

import pandas as pd
alunosDic = {'Nome': ['Sidney', 'Pedro', 'Carla', 'Paula'], # vamos criar uma tebela, criando um dicionario e uma lista
          'Nota':[4, 5, 9, 5.8],
          'Aprovado':['Não', 'Sim', 'Sim', 'Não']}

alunosDF = pd.DataFrame(alunosDic)

primeiraslinhas = alunosDF.loc[0:2] # linhas de 0 até 2, criando variaveis novas nao perdemos os dados anteriores.
# primeiraslinhas é uma copia do alunosDF
print(primeiraslinhas)
#      Nome  Nota Aprovado
# 0  Sidney   4.0      Não
# 1   Pedro   5.0      Sim
# 2   Carla   9.0      Sim


novoDF = alunosDF.loc[alunosDF['Nota']!=9] # excluiu a nota 9
print(novoDF)
#      Nome  Nota Aprovado
# 0  Sidney   4.0      Não
# 1   Pedro   5.0      Sim
# 3   Paula   5.8      Não

# =================================== Manipulando colunas com o Pandas =================================================

import pandas as pd

dados = pd.read_csv('D:/tech/athlete_events.csv')  # da mesma forma porem com arquivo csv

dados.rename(columns={'Name': 'Nome', 'Sex': 'Sexo', 'Age': 'Idade'}, inplace = True) # atribui os valores
print(dados.columns)
# Index(['ID', 'Nome', 'Sexo', 'Idade', 'Height', 'Weight', 'Team', 'NOC',
#        'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'],
#       dtype='object')


print(dados['Height']) # mostra apenas os dados de uma coluna especifica, nesse caso da aultura
# 271111    179.0
# 271112    176.0
# 271113    176.0
# 271114    185.0
# 271115    185.0

altura = dados['Height']
print(altura) # dados recebe altura
# 271111    179.0
# 271112    176.0
# 271113    176.0
# 271114    185.0
# 271115    185.0
# Name: Height, Length: 271116, dtype: float64

altura = dados['Height']
print(type(altura))
# <class 'pandas.core.series.Series'>

print(dados['Medal'].value_counts()) # mostra quantas vezes os valores aparece
# Gold      13372
# Bronze    13295
# Silver    13116
# Name: Medal, dtype: int64

dados2 = dados['Medal'].value_counts() # mostra quantas vezes os valores aparece
print(dados2)
# Gold      13372
# Bronze    13295
# Silver    13116
# Name: Medal, dtype: int64

dados2 = dados['Name'].value_counts() # mostra quantas vezes os valores aparece
print(dados2)
# Robert Tait McKenzie            58
# Heikki Ilmari Savolainen        39
# Joseph "Josy" Stoffel           38
# Ioannis Theofilakis             36
# Takashi Ono                     33
#                                 ..
# Tatyana Vasilyevna Kalmykova     1
# Mariya Lvovna Kalmykova          1
# Christine Kalmer                 1
# Joannis "Jannis" Kalmazidis      1
# Pierre-Georges LeClercq          1
# Name: Name, Length: 134732, dtype: int64

dados2 = dados['City'].value_counts() # mostra quantas vezes os valores aparece
print(dados2)
# London                    22426
# Athina                    15556
# Sydney                    13821
# Atlanta                   13780
# Rio de Janeiro            13688
# Beijing                   13602
# Barcelona                 12977
# ..................

dados2 = dados['Sex'].value_counts() # mostra quantas vezes os valores aparece, é uma contagem.
print(dados2)
# M    196594
# F     74522
# Name: Sex, dtype: int64

dados2 = dados['Sex'].value_counts().index.values # exemplo para filtrar melhor os dados de amostra, os valores do index.
print(dados2)

dados2 = dados.describe() # mostra todos os dados
print(dados2)
#                   ID            Age  ...         Weight           Year
# count  271116.000000  261642.000000  ...  208241.000000  271116.000000
# mean    68248.954396      25.556898  ...      70.702393    1978.378480
# std     39022.286345       6.393561  ...      14.348020      29.877632
# min         1.000000      10.000000  ...      25.000000    1896.000000
# 25%     34643.000000      21.000000  ...      60.000000    1960.000000
# 50%     68205.000000      24.000000  ...      70.000000    1988.000000
# 75%    102097.250000      28.000000  ...      79.000000    2002.000000
# max    135571.000000      97.000000  ...     214.000000    2016.000000

# ======================================== Como excluir colunas no Pandas ==============================================
import pandas as pd

dados = pd.read_csv('D:/tech/athlete_events.csv')  # da mesma forma porem com arquivo csv

# axis = 0    é uma linha    axis = 1    é uma coluna
dados.drop('ID', axis = 1, inplace = True) # exclui essas colunas, id, city, season
dados.drop('City', axis = 1, inplace = True)
dados.drop('Season', axis = 1, inplace = True)
print(dados.columns)
# Index(['Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games',
#        'Year', 'Sport', 'Event', 'Medal'],
#       dtype='object')

# ================================================ Função groupby - Pandas =============================================
# criar grupos a partir de um determinado criterio.

import pandas as pd
alunosDic = {'Nome': ['Sidney', 'Pedro', 'Carla', 'Paula'], # vamos criar uma tebela, criando um dicionario e uma lista
          'Nota':[4, 5, 9, 5.8],
          'Aprovado':['Não', 'Sim', 'Sim', 'Não']}

alunosDF = pd.DataFrame(alunosDic)
# alunosDF.groupby(['Nome'])   # fazer com um grupo
# alunosDF.groupby(['Nome', 'Nota'])    #fazer com varios grupos

# print(alunosDF.groupby(['Nome', 'Nota'])) # ao fazer essa aplicação criamos um DataFrame
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000289E37A6FD0>

alunosDF.groupby(['Nome']).count() # faz uma contagem nao é mais DtaFrame grupy e passa a ser um panda.
print(alunosDF.groupby(['Nome']).count()) # imprimindo pra ver ele funcionando, qualquer coisa pode colocar isso em
# uma função e imprimir a função.
#         Nota  Aprovado
# Nome
# Carla      1         1
# Paula      1         1
# Pedro      1         1
# Sidney     1         1

alunosDF.groupby(['Nome']).count()['Sidney'].sort_values() # ordernar por ordem crescente
alunosDF.groupby(['Idade']).sum() # vai somar as linhas da coluna

#  retorna apenas uma ocorrencia de cada atleta, não conta duas vezes o atleta.
alunosDF.groupby('Atletas').nunique()['Name']

#  retornar varios valores juntos.
alunosDF.groupby('Atletas').agg({'Name': 'nunique',
                                 'Medal': 'count',
                                 'Games': 'nunique'})  # chamamos uma função, nesse exemplo temos 3 tabelas name, medal,
# games e cada tabela  retorna um parametro selecionado

# ============================================= Como criar histogramas ================================================

# histograma é um grafico de barras

import matplotlib.pyplot as plt # biblioteca criada para criar graficos.
import pandas as pd # pd = apelida para facilitar
dados = pd.read_excel('D:/tech/tech.xlsx')

dados.hist(column='Coluna2', bins=8) # informa o nome da coluna que contenha numeros, bins é o numero de
# linhas para a amostra
print(plt.show()) # imprime o grafico

plt.hist(nome_array, bins=20) # fazendo a mesma amostra em barras, porem com array nao com o panda, onde esta
# nome_array deve colocar o nome que achar melhor