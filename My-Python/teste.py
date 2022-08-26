
import pandas as pd
alunosDic = {'Nome': ['Sidney', 'Pedro', 'Carla', 'Paula'], # vamos criar uma tebela, criando um dicionario e uma lista
          'Nota':[4, 5, 9, 5.8],
          'Aprovado':['Não', 'Sim', 'Sim', 'Não']}

alunosDF = pd.DataFrame(alunosDic)

print(alunosDF.loc[alunosDF['Aprovado']=='Sim']) # apenas os aprovados