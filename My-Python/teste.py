


# import pandas as pd
# alunosDic = {'Nome': ['Sidney', 'Pedro', 'Carla', 'Paula'], # vamos criar uma tebela, criando um dicionario e uma lista
#           'Nota':[4, 5, 9, 5.8],
#           'Aprovado':['Não', 'Sim', 'Sim', 'Não']}
#
# alunosDF = pd.DataFrame(alunosDic)
# # alunosDF.groupby(['Nome'])   # fazer com um grupo
# # alunosDF.groupby(['Nome', 'Nota'])    #fazer com varios grupos
#
# # print(alunosDF.groupby(['Nome', 'Nota'])) # ao fazer essa aplicação criamos um DataFrame
# # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000289E37A6FD0>
#
# alunosDF.groupby(['Nome']).count() # faz uma contagem nao é mais DtaFrame grupy e passa a ser um panda.
# print(alunosDF.groupby(['Nome']).count()) # imprimindo pra ver ele funcionando, qualquer coisa pode colocar isso em
# # uma função e imprimir a função.
# #         Nota  Aprovado
# # Nome
# # Carla      1         1
# # Paula      1         1
# # Pedro      1         1
# # Sidney     1         1
#
# alunosDF.groupby(['Nome']).count()['Sidney'].sort_values() # ordernar por ordem crescente
# alunosDF.groupby(['Idade']).sum() # vai somar as linhas da coluna
#
# #  retorna apenas uma ocorrencia de cada atleta, não conta duas vezes o atleta.
# alunosDF.groupby('Atletas').nunique()['Name']

import matplotlib.pyplot as plt # biblioteca criada para criar graficos.
import pandas as pd # pd = apelida para facilitar
#dados = pd.read_excel('D:/tech/tech.xlsx')

#dados.hist(column='Coluna2', bins=8) # informa o nome da coluna que contenha numeros, bins é o numero de
# linhas para a amostra
#print(plt.show()) # imprime o grafico

#plt.hist(nome_array, bins=20) # fazendo a mesma amostra em barras, porem com array nao com o panda, onde esta
# nome_array deve colocar o nome que achar melhor


soma = 0
for i in range(1, 4):
    nota = (int(input(f'Digite um numero no posição {i}: ')))
    soma += nota
print(soma / 3)