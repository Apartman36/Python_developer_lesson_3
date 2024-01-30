kol_1 = int(input('Введите количество элементов списка: '))
list_1 = [int(input()) for i in range(kol_1)]

kol_2 = int(input('Введите количества элементов второго списка: '))
list_2 = [int(input()) for i in range(kol_2)]

list_3 =[i for i in list_1 if not i in list_2 or list_2.remove(i)]
print('Результат:', list_3)
