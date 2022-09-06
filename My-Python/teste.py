

import pandas as pd # pd = apelida para facilitar
dados = pd.read_excel('D:/tech/tech.xlsx')


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
import pandas as pd # pd = apelida para facilitar
dados = pd.read_excel('D:/tech/tech.xlsx')

import matplotlib.pyplot as plt
masculinos = dados.loc[dados['nome']=='paulo'] # dessa forma ele filme apenas os paulos, nesse exemplo.
a = masculinos['nome']
p = masculinos['idade']

plt.scatter(a,p)  # mostra outro grafico
print(plt.show())