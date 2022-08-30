import pandas as pd

dados = pd.read_csv('D:/tech/athlete_events.csv')  # da mesma forma porem com arquivo csv


dados.drop('ID', axis = 1, inplace = True) # exclui essas colunas
dados.drop('City', axis = 1, inplace = True)
dados.drop('Season', axis = 1, inplace = True)
print(dados.columns)


