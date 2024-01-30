kol = int(input('Введите количество элементов списка: '))
spisok = []
for i in range(kol):
  spisok.append(int(input('Введите элемент списка: ')))
print('Вывод:',sorted(spisok))
