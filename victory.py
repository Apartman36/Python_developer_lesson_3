import random as rand
import numpy as np
import re

while True:
  actor = ['Том Круз', 'Дуэйн Джонсон', 'Том Хэнкс', 'Брэд Питт', 'Дензел Вашингтон', 'Джулия Робертс', 'Уилл Смит', 'Ди Каприо', 'Джонни Депп', 'Кевин Харт']
  dates = ['03.07.1961', '02.05.1972', '09.07.1956', '18.12.1963', '28.12.1954', '28.10.1967', '25.09.1968', '11.11.1974', '09.06.1963', '06.07.1979']
  days = ([i[0:2] for i in dates])
  months = ([i[3:5] for i in dates])
  years = [i[(len(i) - 4) : len(i)] for i in dates]
  chase = rand.sample([i for i in range(10)], 5)
  otvets = []

  print('Добро пожаловать на викторину!\nВводить даты роджения нужно в формате dd.mm.yyyy\n')
  for i in range(len(chase)):
    rezult = str(input('Введите дату рождения {} - '.format(actor[chase[i]])))
    if rezult == dates[chase[i]]:
      otvets.append(True)
    else:
      otvets.append(False)
  index_lose = [i for i in range(len(otvets)) if otvets[i] == False]

  days_letter = {
      '02' : 'Второе',
      '03' : 'Третье',
      '06' : 'Шестое',
      '09' : 'Девятое',
      '11' : 'Одиннадатое',
      '18' : 'Восемнадцатое',
      '25' : 'Двадцать пятое',
      '28' : 'Двадцать восьмое'
  }

  months_letter = {
      '05' : 'мая',
      '06' : 'июня',
      '07' : 'июля',
      '08' : 'августа',
      '09' : 'сентября',
      '10' : 'октября',
      '11' : 'ноября',
      '12' : 'декабря'
  }

  if otvets.count(False) > 0:
    print('\nУ вас есть ошиибки - {}'.format(otvets.count(False)))
    for i in index_lose:
      print(actor[chase[i]] + ' --> ' + days_letter[days[chase[i]]] + ' ' + months_letter[months[chase[i]]] + ' ' + years[chase[i]] + ' года')

  print('\nКоличество правильных ответов:', otvets.count(True))
  print('Количество неправильных ответов:', otvets.count(False))

  ends = str(input('\nХотите перепройти тест?(Да/Нет): '))
  ends = ends.lower()

  if ends == 'нет':
    print('Викторина окончена')
    break
  else:
    print()
