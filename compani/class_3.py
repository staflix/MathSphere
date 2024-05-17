from company import *

year_3 = Class(3)

topic_1 = Topic('Числа   от   1   до   100. Сложение и вычитание.')
lvl_1 = Level(1, info='Привет! Немного посчитай примеры.')
lvl_1.add(Task(text='реши пример в столбик на картинке', answer='55', image="pic/50.jpg"))
lvl_1.add(Task(text='и этот', answer='80', image="pic/51.jpg"))

lvl_2 = Level(1, info='Теперь немного примеров!')
lvl_2.add(Task(text='реши вот этот пример в несколько действий', answer='79', image='pic/52.jpg'))
lvl_2.add(Task(text="1 + 34 - 32 =", answer="3"))
lvl_2.add(Task(text="7 - 6 - 29 =", answer="-28"))
lvl_2.add(Task(text="1 + 34 - 32 =", answer="3"))

lvl_3 = Level(1, info='продалжием')
lvl_3.add(Task(text="11 - 19 + 8 =", answer="0"))
lvl_3.add(Task(text="36 + 41 - 1 =", answer="76"))
lvl_3.add(Task(text="17 - 8 - 12 =", answer="-3"))
lvl_3.add(Task(text="11 - 19 + 8 =", answer="0"))

topic_1.add_level(lvl_1)
topic_1.add_level(lvl_2)
topic_1.add_level(lvl_3)

year_3.add_level(topic_1)

topic_2 = Topic('Числа   от   1   до   100. Умнажение деление.')

lvl_1 = Level(1, info='Теперь просто без лишникх слов поделеи и поумнажаем')
lvl_1.add(Task(text="3 * 2 / 3 =", answer="2"))
lvl_1.add(Task(text="4 * 8 / 1 =", answer="32"))
lvl_1.add(Task(text="6 * 7 / 6 =", answer="7"))

lvl_2 = Level(1, info='Немного примеров!')
lvl_2.add(Task(text="3 * 3 * 6 =", answer="54"))
lvl_2.add(Task(text="10 * 10 * 4 =", answer="400"))
lvl_2.add(Task(text="5 * 3 * 1 =", answer="15"))
lvl_2.add(Task(text="2 * 10 * 5 =", answer="100"))

lvl_3 = Level(1, info='Ещё примеры!')
lvl_3.add(Task(text="7 / 1 * 10 =", answer="70"))
lvl_3.add(Task(text="9 * 6 / 6 =", answer="9"))
lvl_3.add(Task(text="1 / 2 * 6 =", answer="3"))

topic_2.add_level(lvl_1)
topic_2.add_level(lvl_2)
topic_2.add_level(lvl_3)
year_3.add_level(topic_2)

topic_3 = Topic("Умножение на 1")
lvl_1 = Level(1, info='Привет! Тебе нужно поумнажаить 1!')
lvl_1.add(Task(text="26 * 1 =", answer="26"))
lvl_1.add(Task(text="9 * 1 =", answer="9"))
lvl_1.add(Task(text="14 * 1 =", answer="14"))

lvl_2 = Level(1, info='Продолжаем!')
lvl_2.add(Task(text="24 * 1 =", answer="24"))
lvl_2.add(Task(text="30 * 1 =", answer="30"))
lvl_2.add(Task(text="22 * 1 =", answer="22"))
lvl_2.add(Task(text="51 * 1 =", answer="51"))

lvl_3 = Level(1, info='еще чучуть')
lvl_3.add(Task(text="55 * 1 =", answer="55"))
lvl_3.add(Task(text="42 * 1 =", answer="42"))
lvl_3.add(Task(text="40 * 1 =", answer="40"))
lvl_3.add(Task(text="31 * 1 =", answer="31"))

lvl_4 = Level(1, info='ну и последний раз')
lvl_4.add(Task(text="54 * 1 =", answer="54"))
lvl_4.add(Task(text="44 * 1 =", answer="44"))
lvl_4.add(Task(text="15 * 1 =", answer="15"))
lvl_4.add(Task(text="47 * 1 =", answer="47"))

lvl_10 = Level(1, info='Время теста!', style='test', time=60, topic='умнажение на 1')
lvl_10.add(Task(text="13 * 1 =", answer="13"))
lvl_10.add(Task(text="45 * 1 =", answer="45"))
lvl_10.add(Task(text="47 * 1 =", answer="47"))
lvl_10.add(Task(text="6 * 1 =", answer="6"))
lvl_10.add(Task(text="29 * 1 =", answer="29"))
lvl_10.add(Task(text="44 * 1 =", answer="44"))
lvl_10.add(Task(text="5 * 1 =", answer="5"))
lvl_10.add(Task(text="46 * 1 =", answer="46"))
lvl_10.add(Task(text="59 * 1 =", answer="59"))
lvl_10.add(Task(text="46 * 1 =", answer="46"))

topic_3.add_level(lvl_1)
topic_3.add_level(lvl_2)
topic_3.add_level(lvl_3)
topic_3.add_level(lvl_4)
topic_3.add_level(lvl_10)
year_3.add_level(topic_3)


topic_4 = Topic('умнажение на 0')
lvl_1 = Level(1, info='Привет! Тут тоже самое только нужно умножить на 0.')
lvl_1.add(Task(text="41 * 0 =", answer="0"))
lvl_1.add(Task(text="27 * 0 =", answer="0"))
lvl_1.add(Task(text="13 * 0 =", answer="0"))

lvl_2 = Level(1, info='')
lvl_2.add(Task(text="28 * 0 =", answer="0"))
lvl_2.add(Task(text="51 * 0 =", answer="0"))
lvl_2.add(Task(text="11 * 0 =", answer="0"))
lvl_2.add(Task(text="29 * 0 =", answer="0"))

lvl_3 = Level(1, info='тоже самое')
lvl_3.add(Task(text="29 * 0 =", answer="0"))
lvl_3.add(Task(text="35 * 0 =", answer="0"))
lvl_3.add(Task(text="26 * 0 =", answer="0"))
lvl_3.add(Task(text="16 * 0 =", answer="0"))
lvl_3.add(Task(text="16 * 0 =", answer="0"))


lvl_10 = Level(1, info='Время теста!', style='test', time=60, topic='умнажение на 0')
lvl_10.add(Task(text="21 * 0 =", answer="0"))
lvl_10.add(Task(text="37 * 0 =", answer="0"))
lvl_10.add(Task(text="7 * 0 =", answer="0"))
lvl_10.add(Task(text="33 * 0 =", answer="0"))
lvl_10.add(Task(text="32 * 0 =", answer="0"))
lvl_10.add(Task(text="5 * 0 =", answer="0"))
lvl_10.add(Task(text="57 * 0 =", answer="0"))
lvl_10.add(Task(text="35 * 0 =", answer="0"))
lvl_10.add(Task(text="17 * 0 =", answer="0"))
lvl_10.add(Task(text="26 * 0 =", answer="0"))
topic_4.add_level(lvl_1)
topic_4.add_level(lvl_2)
topic_4.add_level(lvl_3)
topic_4.add_level(lvl_4)
topic_4.add_level(lvl_10)
year_3.add_level(topic_4)


topic_5 = Topic('Доли.')

lvl_1 = Level(1, info='Привет! Определи сколько долей ')
lvl_1.add(Task(text='Сколько яблок на этой картинке?', answer='2', image='pic/53.jpg'))
lvl_1.add(Task(text='А на этой?', answer='4', image='pic/54.jpg'))


lvl_2 = Level(1, info='Привет! Сравни части.')
lvl_2.add(Task(text='ответь на вопрос на рисунку', answer='одна четвертая', image='pic/55.jpg', choice=['одна шестая', 'одна четвертая']))
lvl_2.add(Task(text='какая часть меньше одна вторая или одна третья?', answer='одна третья', image='pic/55.jpg', choice=['одна третья', 'одна вторая']))


lvl_3 = Level(1, info='Выбери как называется часть на рисунке')
lvl_3.add(Task(text='как можно назвать часть на рисунке', answer='одна третья', image='pic/56.jpg', choice=['одна третья', 'три первых']))
lvl_3.add(Task(text='А какя часть здесь выделина?', answer='одна двенадцатая', image='pic/57.jpg', choice=['одна третья', 'три первых', 'одна двенадцатая']))


lvl_4 = Level(1, info='Давай еще немного по чястям')
lvl_4.add(Task(text='сколько здесь частей выделено?', answer='1', image='pic/58.jpg', choice=['1', '2', '3']))
lvl_4.add(Task(text='а здесь?', answer='1', image='pic/58.jpg', choice=['1', '2', '3']))
lvl_4.add(Task(text='последний раз', answer='1', image='pic/59.jpg', choice=['1', '2', '3']))


lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Угол. Виды углов. Логика.')
lvl_10.add(Task(text='Сколько яблок на этой картинке?', answer='2', image='pic/53.jpg'))
lvl_10.add(Task(text='А на этой?', answer='4', image='pic/54.jpg'))
lvl_10.add(Task(text='сколько здесь частей выделено?', answer='1', image='pic/58.jpg', choice=['1', '2', '3']))
lvl_10.add(Task(text='а здесь?', answer='1', image='pic/58.jpg', choice=['1', '2', '3']))
lvl_10.add(Task(text='последний раз', answer='1', image='pic/59.jpg', choice=['1', '2', '3']))
lvl_10.add(Task(text='ответь на вопрос на рисунку', answer='одна четвертая', image='pic/55.jpg', choice=['одна шестая', 'одна четвертая']))
lvl_10.add(Task(text='какая часть меньше одна вторая или одна третья?', answer='одна третья', image='pic/55.jpg', choice=['одна третья', 'одна вторая']))

topic_5.add_level(lvl_1)
topic_5.add_level(lvl_2)
topic_5.add_level(lvl_3)
topic_5.add_level(lvl_4)

topic_5.add_level(lvl_10)
year_3.add_level(topic_5)


topic_6 = Topic('вычисления вида 80:20.')

lvl_1 = Level(1, info='Привет! Будет немного деления')
lvl_1.add(Task(text="70 / 10 =", answer="7"))
lvl_1.add(Task(text="90 / 10 =", answer="9"))
lvl_1.add(Task(text="80 / 10 =", answer="8"))

lvl_2 = Level(1, info='теперь на 20')
lvl_2.add(Task(text="40 / 20 =", answer="2"))
lvl_2.add(Task(text="80 / 20 =", answer="4"))
lvl_2.add(Task(text="60 / 20 =", answer="3"))


lvl_3 = Level(1, info='И нужно повторить умножение ')
lvl_3.add(Task(text="1 * 12 =", answer="12"))
lvl_3.add(Task(text="22 * 3 =", answer="66"))
lvl_3.add(Task(text="1 * 17 =", answer="17"))
lvl_3.add(Task(text="3 * 14 =", answer="42"))
lvl_3.add(Task(text="5 * 7 =", answer="35"))

lvl_4 = Level(1, info='Реши уравнения!')
lvl_4.add(Task(text='75 - х = 75', answer='0'))
lvl_4.add(Task(text='4 + х = 84', answer='80'))
lvl_4.add(Task(text='89 - х = 0', answer='89'))

lvl_5 = Level(1, info='Вычислительная машина!')
lvl_5.add(Task(text="(5 + 17) / 2 =", answer="11"))
lvl_5.add(Task(text="(7 + 8) / 6 =", answer="2"))
lvl_5.add(Task(text="(11 + 6) / 2 =", answer="8"))
lvl_5.add(Task(text="(21 + 1) / 7 =", answer="3"))
lvl_5.add(Task(text="(7 + 14) / 8 =", answer="2"))


lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='вычисления вида 80:20..')
lvl_10.add(Task(text="(11 + 6) / 2 =", answer="8"))
lvl_10.add(Task(text="(21 + 1) / 7 =", answer="3"))
lvl_10.add(Task(text="(7 + 14) / 8 =", answer="2"))
lvl_10.add(Task(text="22 * 3 =", answer="66"))
lvl_10.add(Task(text="1 * 17 =", answer="17"))
lvl_10.add(Task(text="3 * 14 =", answer="42"))
lvl_10.add(Task(text="80 / 20 =", answer="4"))
lvl_10.add(Task(text="60 / 20 =", answer="3"))


topic_6.add_level(lvl_1)
topic_6.add_level(lvl_2)
topic_6.add_level(lvl_3)
topic_6.add_level(lvl_4)
topic_6.add_level(lvl_5)
topic_6.add_level(lvl_10)
year_3.add_level(topic_6)



topic_7 = Topic('Пероверка деления.')

lvl_1 = Level(1, info='Привет! Проверь уравнения!')
lvl_1.add(Task(text="21 / 3 = 7", answer="да", choice=["да", "нет"]))
lvl_1.add(Task(text="4 / 1 = 4", answer="да", choice=["да", "нет"]))
lvl_1.add(Task(text="20 / 10 = 3", answer="нет", choice=["да", "нет"]))
lvl_1.add(Task(text="23 / 2 = 12", answer="нет", choice=["да", "нет"]))

lvl_2 = Level(1, info='еще разок ')
lvl_2.add(Task(text="3 / 1 = 3", answer="да", choice=["да", "нет"]))
lvl_2.add(Task(text="14 / 1 = 7", answer="нет", choice=["да", "нет"]))
lvl_2.add(Task(text="21 / 3 = 7", answer="да", choice=["да", "нет"]))

lvl_3 = Level(1, info='Проверка умножения ')
lvl_3.add(Task(text="16 * 2 = 31", answer="нет", choice=["да", "нет"]))
lvl_3.add(Task(text="9 * 2 = 18", answer="да", choice=["да", "нет"]))
lvl_3.add(Task(text="21 * 8 = 168", answer="да", choice=["да", "нет"]))

lvl_4 = Level(1, info='еще разок.')
lvl_4.add(Task(text="2 * 10 = 12", answer="нет", choice=["да", "нет"]))
lvl_4.add(Task(text="7 * 4 = 28", answer="да", choice=["да", "нет"]))
lvl_4.add(Task(text="18 * 7 = 125", answer="нет", choice=["да", "нет"]))
lvl_4.add(Task(text="20 * 10 = 200", answer="да", choice=["да", "нет"]))


lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Умножение!')
lvl_10.add(Task(text="21 / 3 = 7", answer="да", choice=["да", "нет"]))
lvl_10.add(Task(text="4 / 1 = 4", answer="да", choice=["да", "нет"]))
lvl_10.add(Task(text="14 / 1 = 7", answer="нет", choice=["да", "нет"]))
lvl_10.add(Task(text="21 / 3 = 7", answer="да", choice=["да", "нет"]))
lvl_10.add(Task(text="18 * 7 = 125", answer="нет", choice=["да", "нет"]))
lvl_10.add(Task(text="20 * 10 = 200", answer="да", choice=["да", "нет"]))

topic_7.add_level(lvl_1)
topic_7.add_level(lvl_2)
topic_7.add_level(lvl_3)
topic_7.add_level(lvl_4)
topic_7.add_level(lvl_5)
topic_7.add_level(lvl_10)
year_3.add_level(topic_7)


topic_8 = Topic('Деление с остатком.')

lvl_1 = Level(1, info='Привет! Найди остаток!')
lvl_1.add(Task(text='27 / 3 = ', answer='0'))
lvl_1.add(Task(text='26 / 3 =', answer='2'))
lvl_1.add(Task(text='28 / 3 = ', answer='1'))

lvl_2 = Level(1, info='Выполни деление, используя рисунки')
lvl_2.add(Task(text='6 : 2', answer='3', image='pic/126.jpg'))
lvl_2.add(Task(text='10 : 2', answer='5', image='pic/127.jpg'))
lvl_2.add(Task(text='8 : 4', answer='2', image='pic/128.jpg'))

lvl_3 = Level(1, info='Реши уравнения!')
lvl_3.add(Task(text='х - 8 = 75', answer='83'))
lvl_3.add(Task(text='14 - х = 6', answer='8'))

lvl_4 = Level(1, info='Вычисли, заменяя умножение сложением.')
lvl_4.add(Task(text='2 * 5', answer='10'))
lvl_4.add(Task(text='4 * 3', answer='12'))
lvl_4.add(Task(text='7 * 4', answer='28'))
lvl_4.add(Task(text='9 * 3', answer='27'))

lvl_5 = Level(1, info='Сравнение + умножение!')
lvl_5.add(Task(text='7 * 3 ? 7 + 7 + 7 + 7', answer='<', choice=['>', '<', '=']))
lvl_5.add(Task(text='6 + 6 + 6 + 6 + 6 + 6 ? 6 * 5', answer='>', choice=['>', '<', '=']))

lvl_6 = Level(1, info='Задачки!')
lvl_6.add(Task(text='На 5 лошадей сели по одному всаднику, сколько всего всадников?', answer='5'))
lvl_6.add(Task(text='После обеда на столе осталось 4 тарелки, ни на одной не осталось ни одной сосиски.'
                    ' Сколько всего сосисок на этих тарелках?', answer='0'))

lvl_7 = Level(1, info='Примеры!')
lvl_7.add(Task(text='1 * 26', answer='26'))
lvl_7.add(Task(text='0 * (21 - 8)', answer='0'))
lvl_7.add(Task(text='17 + 80 + 3', answer='100'))

lvl_8 = Level(1, info='Используй свойство умножения.')
lvl_8.add(Task(text='4 * 5 = 20, 5 * 4 = ?', answer='20'))
lvl_8.add(Task(text='7 * 4 = 28, 4 * 7 = ?', answer='28'))
lvl_8.add(Task(text='9 * 3 = 27, 3 * 9 = ?', answer='27'))

lvl_9 = Level(1, info='Найди значение выражения 65 - b')
lvl_9.add(Task(text='Где b = 65.', answer='0'))
lvl_9.add(Task(text='А если b = 20?', answer='45'))
lvl_9.add(Task(text='А при b = 49?', answer='16'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Деление!')
lvl_10.add(Task(text='1 * 26', answer='26'))
lvl_10.add(Task(text='9 * 3', answer='27'))
lvl_10.add(Task(text='3 * 12', answer='36'))
lvl_10.add(Task(text='7 * 3 ? 6 * 4', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='2 * 14 ? 6 * 4', answer='>', choice=['>', '<', '=']))

topic_8.add_level(lvl_1)
topic_8.add_level(lvl_2)
topic_8.add_level(lvl_3)
topic_8.add_level(lvl_4)
topic_8.add_level(lvl_5)
topic_8.add_level(lvl_6)
topic_8.add_level(lvl_7)
topic_8.add_level(lvl_8)
topic_8.add_level(lvl_9)
topic_8.add_level(lvl_10)
year_2.add_level(topic_8)


