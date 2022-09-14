

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

# ======================================== O que é um boxplot e como calcular ==========================================


# ========================================== Criando boxplot usando Python ============================================

import matplotlib.pyplot as plt # biblioteca criada para criar graficos.
import pandas as pd # pd = apelida para facilitar
dados = pd.read_excel('D:/tech/tech.xlsx')
print(dados.head())


import matplotlib.pyplot as plt
dados.boxplot(column='contato') # comando para criar um boxplot
print(plt.show())


import matplotlib.pyplot as plt
dados.boxplot(column=['idade','numero','contato']) # dessa forma ele mostra varios boxplot
print(plt.show())

# =============================== Criando e visualizando gráficos com Matplotlib =======================================
# anaconda ja tem instalado

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # criari essas duas listas para mostrar como funciona.
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.scatter(x,y) # chamando a função e dizer quais variaveis iremos chamar, nessse caso x e y
print(plt.show()) # chamar o grafico

import numpy as np
x1 = np.arange(0,1000,1) # arange cria um array nesse caso começa em 0 vai ate 1000 e pula de 1 em 1
plt.plot(x1, x1 **2) # modifica o comportamento de uma função.
print(plt.show())

# ==========================================================

import pandas as pd # pd = apelida para facilitar
dados = pd.read_excel('D:/tech/tech.xlsx')

masculinos = dados.loc[dados['nome']=='paulo'] # dessa forma ele filme apenas os paulos, nesse exemplo.
print(masculinos.head())
#   nome  idade cidade  contato   casa  numero
# 5  paulo     32  paulo       32  paulo      32
# 6  paulo     33  paulo       33  paulo      33
# 7  paulo     34  paulo       34  paulo      34
# 8  paulo     35  paulo       35  paulo      35
# 9  paulo     36  paulo       36  paulo      36

# ==========================================================

import pandas as pd # pd = apelida para facilitar
dados = pd.read_excel('D:/tech/tech.xlsx')

import matplotlib.pyplot as plt
masculinos = dados.loc[dados['nome']=='paulo'] # dessa forma ele filme apenas os paulos, nesse exemplo.
a = masculinos['nome']
p = masculinos['idade']

plt.scatter(a,p)  # mostra outro grafico
print(plt.show())

# ====================================== Como trabalhar com dados faltantes ============================================
# NaN = significa que o dado esta faltando.

import pandas as pd # pd = apelida para facilitar
dados = pd.read_excel('D:/tech/tech.xlsx')

dados2 = dados.dropna() # esse comando dropna() vai excluir a linha que contenha qualquer dado faltante
print(dados2.shape) # mostra quantas linhas e quantas colunas tem no total

enulo = dados.isnull() # criamos uma nova variavel, nela colocamos o isnull() que mostra True ou False para
# dados faltantes.
print(enulo.head()) #vai mostrar na tela o resultado

faltantes = dados.isnull().sum() # a funçao sum() vai somar quantos colunas estao faltando, quantos True tem.
print(faltantes) # ou faltantes.head() para imprimir na tela.

faltantes_percentual = (dados.isnull().sum() / len(dados['idade'])) *100 # criei uma funçao que mostra a media dos dados
# faltantes em porcentagem, nesse caso pedi pra ver idade.
print(faltantes_percentual) # imprimir o resultado


# ====================== subistituir os dados faltantes

dados['idade'].fillna('Nenhuma',inplace = True) # nessa coluna idades iremos subistituir os dados faltantes
# pela palavra Nenhuma, o inplace=True mostra o resultado na mesma linha.
print(dados.head())

# podemos subistituir os faltantes pela media da propria coluna
dados['idade'].fillna(dados['idade'].mean(), inplace=True)
print(dados.head(100)) # esse valor  100 significa que quero verificar as primeiras 100 linhas


# ========================================= código de Machine Learning ================================================
# itulizei esse site pra pegar o exemplo csv     https://www.kaggle.com/datasets/dell4010/wine-dataset
import pandas as pd

vinho = pd.read_csv('C:/Users/EXCALIBUR-04/OneDrive/Documentos/GitHub/My-Python/My-Python/exemploscsv/wineQualityReds.csv')  # náo
# esqueca de no final o nome do vinho

print(vinho.head())  # imprimir o cabeçalho
print(vinho)  # imprimir tudo, veja que o Type esta Red ou White
#    Unnamed: 0  fixed.acidity  volatile.acidity  ...  alcohol  quality  Type
# 0           1            7.4              0.70  ...      9.4        5   Red
# 1           2            7.8              0.88  ...      9.8        5   Red


vinho['Type'] = vinho['Type'].replace('Red', 0)  # irei trasnformar o red em numero para que o python possa
# contar ou seja transformando string em numero. subistitui red por numero 0
vinho['Type'] = vinho['Type'].replace('White', 1)  # onde esta white subistitui pelo numero 1

print(vinho['Type'])  # mostrando que foi mesmo modificado
# 0       0    antes era Red
# 1       0
# 2       0


print(vinho)  # imprimir tudo, veja que agora o Type esta 0 ou 1
#       Unnamed: 0  fixed.acidity  volatile.acidity  ...  alcohol  quality  Type
# 0              1            7.4             0.700  ...      9.4        5     0
# 1              2            7.8             0.880  ...      9.8        5     0


y = vinho['Type']  # colocando a coluna Type na variavel y
x = vinho.drop('Type', axis=1)  # esta excluindo a coluna Type e salvando o resto na variavel x

print(y)  # testando... apenas a coluna Type
# 0       0    antes era Red
# 1       0
# 2       0

print(x)  # o resto da lista sem a coluna Type
#       Unnamed: 0  fixed.acidity  volatile.acidity  ...  sulphates  alcohol  quality
# 0              1            7.4             0.700  ...       0.56      9.4        5
# 1              2            7.8             0.880  ...       0.68      9.8        5
# 2              3            7.8             0.760  ...       0.65      9.8        5


# ====================== separando colunas de treino e de testes ====

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)  # dados de, o teste size, mostra a
# porcentagem que eu quero para treino nesse caso quero 30% das amostras

print(y.shape)  # mostra qual o espaço amostral da coluna Type, usaremos 30% dela.
# (1599,)

# ====================== imortar o algoritmo machine learning ExtraTreesClassifier ====

from sklearn.ensemble import ExtraTreesClassifier # trabalha com classificação
modelo = ExtraTreesClassifier()  # chamar a funçao e salva na variavel modelo
modelo.fit(x_treino, y_treino)  # vai aplicar nos dados com o fit, vai treinar os dados

resultado = modelo.score(x_teste, y_teste) # score vai comprar tudo e passar para o algoritimo
print('Acurácia:', resultado)
# Acurácia: 1.0  =  100% dos dados ele acertou  / 0.99 = 99%

print(y_teste[400:403]) # pegando tres amostras, nao treinadas
# 1534    0
# 310     0
# 1558    0
# Name: Type, dtype: int64

print(x_teste[400:403]) # pegando tres amostras, nao treinadas
#       Unnamed: 0  fixed.acidity  volatile.acidity  ...  sulphates  alcohol  quality
# 1055        1056            8.2              0.64  ...       0.62      9.1        6
# 235          236            7.2              0.63  ...       0.58      9.0        6
# 294          295           13.3              0.34  ...       0.81      9.5        6

previsaoes = modelo.predict(x_teste[400:403]) # mostra a previsao
print(previsaoes)
# [0 0 0]  mostrando a previsao das amostrar que escolhi.


# ============================================== Prevendo dados diariamente com Machine Learning =======================

# utilizei esse site para fazer      https://www.kaggle.com/datasets/benjibb/sp500-since-1950

import pandas as pd # importou o pandas
df = pd.read_csv('C:/Users/EXCALIBUR-04/OneDrive/Documentos/GitHub/My-Python/My-Python/exemploscsv/GSPC.csv')
print(df.head()) # imprimir o csv
#          Date   Open   High    Low  Close  Adj Close   Volume
# 0  1950-01-03  16.66  16.66  16.66  16.66      16.66  1260000
# 1  1950-01-04  16.85  16.85  16.85  16.85      16.85  1890000
# 2  1950-01-05  16.93  16.93  16.93  16.93      16.93  2550000
# 3  1950-01-06  16.98  16.98  16.98  16.98      16.98  2010000
# 4  1950-01-09  17.08  17.08  17.08  17.08      17.08  2520000

df = df.drop('Date', axis = 1) # deletar a primeira coluna de Data. que náo será utulizada
print(df.head())
#     Open   High    Low  Close  Adj Close   Volume
# 0  16.66  16.66  16.66  16.66      16.66  1260000
# 1  16.85  16.85  16.85  16.85      16.85  1890000
# 2  16.93  16.93  16.93  16.93      16.93  2550000
# 3  16.98  16.98  16.98  16.98      16.98  2010000
# 4  17.08  17.08  17.08  17.08      17.08  2520000

print(df[-2::]) # vai para o final dos dados
#               Open         High  ...    Adj Close      Volume
# 17216  2748.459961  2752.610107  ...  2748.800049  3517790000
# 17217  2753.250000  2772.389893  ...  2772.350098  3651640000

# vamos salvar essa 17217 em outra base de dados
amanha = df[-1::] # vai cumprir apenas a ultima linha da base df, e colocou na variavel amanha
print(amanha)
#          Open         High          Low        Close    Adj Close      Volume
# 17217  2753.25  2772.389893  2748.459961  2772.350098  2772.350098  3651640000

base = df.drop(df[-1::].index, axis = 0) # exclui a 17217 da lista geral, temos essa lista apenas na variavel amanha.
print(base.tail())
#              Open         High  ...    Adj Close      Volume
# 17212  2702.429932  2729.340088  ...  2724.010010  3561050000
# 17213  2720.979980  2722.500000  ...  2705.270020  4235370000
# 17214  2718.699951  2736.929932  ...  2734.620117  3684130000
# 17215  2741.669922  2749.159912  ...  2746.870117  3376510000
# 17216  2748.459961  2752.610107  ...  2748.800049  3517790000

# fechamento de hj foi 2748.800049 queremos saber se amanha será abaixo ou acima desse valor
base['target'] = base['Close'][1:len(base)].reset_index(drop=True) # nova variavel base, nova coluna target, vamos
# salvar nesse coluna o conteudo da coluna close, indicamos que nao iremos comecar no indice 0, queremos comecar
# com o indixe 1, depois resetamos o indice.
print(base.tail)
# <bound method NDFrame.tail of               Open         High  ...      Volume       target
# 0        16.660000    16.660000  ...     1260000    16.850000
# 1        16.850000    16.850000  ...     1890000    16.930000
# 2        16.930000    16.930000  ...     2550000    16.980000
# 3        16.980000    16.980000  ...     2010000    17.080000
# 4        17.080000    17.080000  ...     2520000    17.030001
# ...            ...          ...  ...         ...          ...
# 17212  2702.429932  2729.340088  ...  3561050000  2705.270020
# 17213  2720.979980  2722.500000  ...  4235370000  2734.620117
# 17214  2718.699951  2736.929932  ...  3684130000  2746.870117
# 17215  2741.669922  2749.159912  ...  3376510000  2748.800049
# 17216  2748.459961  2752.610107  ...  3517790000          NaN          (NaN = nao sabemos o fechamento de amanha)

prev = base[-1::].drop('target', axis = 1) # coloca a 17216 na variavel prev
print(prev)
#               Open         High  ...    Adj Close      Volume
# 17216  2748.459961  2752.610107  ...  2748.800049  3517790000

treino = base.drop(base[-1::].index, axis = 0) # nao tem mais a linha 17216, pois ela esta na prev
print(treino.tail())
#               Open         High  ...      Volume       target
# 17211  2705.110107  2710.669922  ...  3736890000  2724.010010
# 17212  2702.429932  2729.340088  ...  3561050000  2705.270020
# 17213  2720.979980  2722.500000  ...  4235370000  2734.620117
# 17214  2718.699951  2736.929932  ...  3684130000  2746.870117
# 17215  2741.669922  2749.159912  ...  3376510000  2748.800049

# temos que mostrar na coluna target a classificacao de  0 ou 1
treino.loc[treino['target'] > treino['Close'],'target']= 1  # todas as linhas onde o valor da variavel target for maior
# que o valor da variavel close, quero que essa linha na variavel target receba o valor de 1
print(treino.tail())
#               Open         High  ...      Volume      target
# 17211  2705.110107  2710.669922  ...  3736890000     1.00000
# 17212  2702.429932  2729.340088  ...  3561050000  2705.27002
# 17213  2720.979980  2722.500000  ...  4235370000     1.00000
# 17214  2718.699951  2736.929932  ...  3684130000     1.00000
# 17215  2741.669922  2749.159912  ...  3376510000     1.00000

treino.loc[treino['target'] != 1, 'target'] = 0 # caso o valor da variavel target for diferente de 1 adicione o numero 0
print(treino.tail())
#               Open         High          Low  ...    Adj Close      Volume  target
# 17211  2705.110107  2710.669922  2676.810059  ...  2689.860107  3736890000     1.0
# 17212  2702.429932  2729.340088  2702.429932  ...  2724.010010  3561050000     0.0
# 17213  2720.979980  2722.500000  2700.679932  ...  2705.270020  4235370000     1.0
# 17214  2718.699951  2736.929932  2718.699951  ...  2734.620117  3684130000     1.0
# 17215  2741.669922  2749.159912  2740.540039  ...  2746.870117  3376510000     1.0

y = treino['target']
x = treino.drop('target', axis=1)

from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3) # 30% para teste e 70% para treino

from sklearn.ensemble import ExtraTreesClassifier
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

resultado = modelo.score(x_teste, y_teste)
print('Acurácia: ', resultado)
# Acurácia:  0.5237173281703775 (52% resultado nao é bom, Acurácia ruim)

# vamos continuar a aula, mesmo com esse resultado ruim

print(prev)
#               Open         High  ...    Adj Close      Volume
# 17216  2748.459961  2752.610107  ...  2748.800049  3517790000

print(modelo.predict(prev)) # pegar o modelo para fazer uma previsao
# [1.]  siginifica que o valor de fechamento de amanha será maior que 2748

prev['target'] = modelo.predict(prev) # salvando dentro da variavel prev na nova coluna target
print(prev)
#               Open         High         Low  ...    Adj Close      Volume  target
# 17216  2748.459961  2752.610107  2739.51001  ...  2748.800049  3517790000     1.0

print(amanha) # fechou acima que  2748
#           Open         High          Low        Close    Adj Close      Volume
# 17217  2753.25  2772.389893  2748.459961  2772.350098  2772.350098  3651640000

print(base.tail()) # continuar fazendo o teste automatico com a entrada de novos dados, pode filtar a cada
# 10 novos dados  ou 100 ext...
#               Open         High  ...      Volume       target
# 17212  2702.429932  2729.340088  ...  3561050000  2705.270020
# 17213  2720.979980  2722.500000  ...  4235370000  2734.620117
# 17214  2718.699951  2736.929932  ...  3684130000  2746.870117
# 17215  2741.669922  2749.159912  ...  3376510000  2748.800049
# 17216  2748.459961  2752.610107  ...  3517790000          NaN

base = base.append(amanha, sort=True) # incluindo com a funcao append o dia de amanha na base de dados
# inseriu o dia 17217
print(base.tail())
#          Adj Close        Close  ...      Volume       target
# 17213  2705.270020  2705.270020  ...  4235370000  2734.620117
# 17214  2734.620117  2734.620117  ...  3684130000  2746.870117
# 17215  2746.870117  2746.870117  ...  3376510000  2748.800049
# 17216  2748.800049  2748.800049  ...  3517790000          NaN
# 17217  2772.350098  2772.350098  ...  3651640000          NaN

# ================================== ficar de forma automatica====

def warn(*args, **kwargs):  # avisos
    pass
import warnings
warnings.warn = warn


import pandas as pd
prev = pd.read_csv('C:/Users/EXCALIBUR-04/OneDrive/Documentos/GitHub/My-Python/My-Python/exemploscsv/Prev.csv') # carregamento
# da vase prev
print('Fechamento anterior:', prev['Close'][0])
print('Previsão anterior:', prev['target'][0])

base = pd.read_csv('C:/Users/EXCALIBUR-04/OneDrive/Documentos/GitHub/My-Python/My-Python/exemploscsv/Hoje.csv')

try:
    amanha = pd.read_csv('C:/Users/EXCALIBUR-04/OneDrive/Documentos/GitHub/My-Python/My-Python/exemploscsv/Futuro.csv')
    print('Fechamento atual:', amanha['Close'][0])
    base = base.append(amanha[:1], sort=True)
    amanha = amanha.drop(amanha[:1].index, axis=0)
    base.to_csv('C:/Users/EXCALIBUR-04/OneDrive/Documentos/GitHub/My-Python/My-Python/exemploscsv/Hoje.csv', index=False)
    amanha.to_csv('C:/Users/EXCALIBUR-04/OneDrive/Documentos/GitHub/My-Python/My-Python/exemploscsv/Futuro.csv', index=False)
except Exception:
    print('O fechamento ainda não ocorreu!')
    pass

base['target'] = base['Close'][1:len(base)].reset_index(drop=True)
prev = base[-1::].drop('target', axis=1)
treino = base.drop(base[-1::].index, axis=0)

treino.loc[treino['target'] > treino['Close'], 'target'] = 1
treino.loc[treino['target'] != 1, 'target'] = 0

y = treino['target']
x = treino.drop('target', axis=1)

from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3) # 30% para teste e 70% para treino

from sklearn.ensemble import ExtraTreesClassifier
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

print('Acurácia: ', modelo.score(x_teste, y_teste))

prev['target'] = modelo.predict(prev)
print('Fechamento de ontem: ', prev['Close'][0])

if prev['target'][0] == 1:
    print('VAI SUBIR!!!')
else:
    print('vai cais.')

prev.to_csv('C:/Users/EXCALIBUR-04/OneDrive/Documentos/GitHub/My-Python/My-Python/exemploscsv/Prev.csv', index=False)

# ========================= Inteligência Artificial para recomendar filmes com Power BI e Python =======================

# ======================================= Desenvolvimento de softwares com Kivy =======================================

# ================================================= Layouts ===========================================================

https://kivy.org/doc/stable/guide/widgets.html


# ==================================================== Documentação ====================================================

# ====================================================== Instalação e primeiros passos ================================


