



import pandas as pd
alunos = {'Nome': ['Sidney', 'Pedro', 'Carla', 'Paula'], # vamos criar uma tebela, criando um dicionario e uma lista
          'Nota':[4, 5, 9, 5.8],
          'Aprovado':['Não', 'Sim', 'Sim', 'Não']}

dataframe = pd.DataFrame(alunos) # função do panda que transforma a entrada em dataframe
print(dataframe) # quando se cria dataframe automaticamente se cria indices



objeto1 = pd.Series([2, 6, 9, 10, 5]) # criar uma lista series, e vetores unidimensionais
print(objeto1) # tambem adiciona indices


import numpy as np  # cria um array com o numpy
array1 = np.array([2, 6, 9, 10, 5]) # array dimensional
array2 = np.array([(2, 6, 9, 10, 5), (6, 5, 4, 8, 6)])  # cria o array bidimensional com dois
print(array1)
print(array2)


objeto2 = pd.Series(array1)  # criando um array no python so funcional pra uma dimensão
print(objeto2)

objeto2 = pd.Series(array2)  # duas dimensòes nao funciona
print(objeto2)