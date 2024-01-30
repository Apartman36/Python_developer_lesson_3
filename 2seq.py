import numpy as np

listik = str(input('Введите числа через запятую: '))

if ',' in listik: listik = list(listik.split(','))
elif ';' in listik: listik = list(listik.split(';'))
elif '/' in listik: listik = list(listik.split('/'))

listik_un = list(np.unique(listik))
print('\nИзначальный список:', listik)
print('Уникальные значения:', listik_un)

list_raz = [i for i in listik if not i in listik_un or listik_un.remove(i)]
print('Разница:', list_raz)

rez_1 = list(np.unique(listik))
rez_2 = list(np.unique(list_raz))
rez = [i for i in rez_1 if not i in rez_2 or rez_2.remove(i)]

print('\nРезультат:', rez)
