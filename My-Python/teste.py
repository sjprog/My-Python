

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




import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # criari essas duas listas para mostrar como funciona.
# y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# plt.scatter(x,y) # chamando a função e dizer quais variaveis iremos chamar, nessse caso x e y
# print(plt.show()) # chamar o grafico
#
# import numpy as np
# x1 = np.arange(0,1000,1) # arange cria um array nesse caso começa em 0 vai ate 1000 e pula de 1 em 1
# plt.plot(x1, x1 **2) # modifica o comportamento de uma função.
# print(plt.show())
# import pandas as pd # pd = apelida para facilitar
# dados = pd.read_excel('D:/tech/tech.xlsx')
#
# import matplotlib.pyplot as plt
# masculinos = dados.loc[dados['nome']=='paulo'] # dessa forma ele filme apenas os paulos, nesse exemplo.
# a = masculinos['nome']
# p = masculinos['idade']
#
# plt.scatter(a,p)  # mostra outro grafico
# print(plt.show())