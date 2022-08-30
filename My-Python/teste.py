import pandas as pd

dados = pd.read_csv('D:/tech/athlete_events.csv')  # da mesma forma porem com arquivo csv


dados2 = dados.describe() # mostra todos os dados
print(dados2)


