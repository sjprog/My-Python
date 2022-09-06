
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