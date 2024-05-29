from company.company_creator import *

year_4 = Class(4)

topic_1 = Topic('Нумерация от 100 до 1000')

lvl_1 = Level(1, info='Привет! Давай посчитаем')
lvl_1.add(Task(text='Какое число является средним арифметическим всех чисел от 200 до 300?', answer='250'))
lvl_1.add(Task(text='Какое число находится между 300 и 400?', answer='350'))
lvl_1.add(Task(text='Если от числа 500 отнять 300, то сколько получится?', answer='200'))

lvl_2 = Level(1, info='Ещё немного примеров!')
lvl_2.add(Task(text='Заполните пропуски в последовательности чисел: 145, 150, ___, 160, 165', answer='155'))
lvl_2.add(Task(text='Заполните пропуски в последовательности чисел: 275, 280, ___, 290, 295', answer='285'))
lvl_2.add(Task(text='Заполните пропуски в последовательности чисел: 410, 415, 420, ___, 430', answer='425'))

lvl_3 = Level(1, info='Бонусная задача на логику!')
lvl_3.add(Task(text='Является ли число 101 простым?', answer='Да', choice=['Да', 'Нет']))
lvl_3.add(Task(text='Является ли число 200 простым?', answer='Нет', choice=['Да', 'Нет']))
lvl_3.add(Task(text='Является ли число 311 простым?', answer='Да', choice=['Да', 'Нет']))

lvl_4 = Level(1, info='Еще на нумерацию.')
lvl_4.add(Task(text='Сравните числа, используя знаки >, < или =: 345 ___ 543', answer='<', choice=['<', '>', '=']))
lvl_4.add(Task(text='Сравните числа, используя знаки >, < или =: 876 ___ 768', answer='>', choice=['<', '>', '=']))
lvl_4.add(Task(text='Сравните числа, используя знаки >, < или =: 490 ___ 490', answer='=', choice=['<', '>', '=']))

lvl_5 = Level(1, info='Проверь выражения и напиши Верно или Неверно')
lvl_5.add(Task(text='Найдите пропущенное число в последовательности: 321, 322, ___, 324, 325', answer='323'))
lvl_5.add(Task(text='Найдите пропущенное число в последовательности: 685, 686, ___, 688, 689', answer='687'))
lvl_5.add(Task(text='Найдите пропущенное число в последовательности: 999, ___, 997, 996, 995', answer='998'))

lvl_6 = Level(1, info='еще чучуть!')
lvl_6.add(Task(text='Если из числа 900 вычесть 300, какое число получится?', answer='600'))
lvl_6.add(Task(text='Сколько десятков содержится в числе 360?', answer='36'))
lvl_6.add(Task(text='Если к числу 400 прибавить 100, какое число получится?', answer='500'))

lvl_7 = Level(1, info='Примеры!')
lvl_7.add(Task(text='(50 - 38) : 4', answer='3'))
lvl_7.add(Task(text='24 : 4', answer='6'))
lvl_7.add(Task(text='36 : 6', answer='6'))

lvl_8 = Level(1, info='Устные задачи')
lvl_8.add(Task(text='В куске 20 м. ткани. На каждый костюм необходимо 3 м, можно ли сшить 6 таких?', answer='Да',
               choice=['Да', 'Нет']))
lvl_8.add(Task(text='А 7 таких костюмов получится сшить?', answer='Нет', choice=['Да', 'Нет']))
lvl_8.add(Task(text='Найди длину стороны квадрата, если его периметр 24 см.', answer='6'))

lvl_9 = Level(1, info='осталось совсем чучуть')
lvl_9.add(Task(text='Какое число получится, если к числу 250 прибавить 150?', answer='400'))
lvl_9.add(Task(text='Найди разницу между числами 800 и 450.', answer='350'))
lvl_9.add(Task(text='Выпиши пропущенные числа в последовательности: 100, 110, ___, 130, 140', answer='120'))
lvl_9.add(Task(text='Какое число находится между 500 и 600?', answer='550'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='Сравните числа, используя знаки >, < или =: 876 ___ 768', answer='>', choice=['<', '>', '=']))
lvl_10.add(Task(text='Сравните числа, используя знаки >, < или =: 490 ___ 490', answer='=', choice=['<', '>', '=']))
lvl_10.add(Task(text='Сравните числа, используя знаки >, < или =: 876 ___ 768', answer='>', choice=['<', '>', '=']))
lvl_10.add(Task(text='Сравните числа, используя знаки >, < или =: 490 ___ 490', answer='=', choice=['<', '>', '=']))
lvl_10.add(Task(text='Какое число находится между 300 и 400?', answer='350'))
lvl_10.add(Task(text='Если от числа 500 отнять 300, то сколько получится?', answer='200'))
lvl_10.add(Task(text='Найдите пропущенное число в последовательности: 685, 686, ___, 688, 689', answer='687'))
lvl_10.add(Task(text='Найдите пропущенное число в последовательности: 999, ___, 997, 996, 995', answer='998'))

topic_1.add_level(lvl_1)
topic_1.add_level(lvl_2)
topic_1.add_level(lvl_3)
topic_1.add_level(lvl_4)
topic_1.add_level(lvl_5)
topic_1.add_level(lvl_6)
topic_1.add_level(lvl_7)
topic_1.add_level(lvl_8)
topic_1.add_level(lvl_9)
topic_1.add_level(lvl_10)
year_4.add_level(topic_1)

topic_2 = Topic('Числа больше 1000')

lvl_1 = Level(1, info='Привет! Определи что больше!')
lvl_1.add(Task(text='Какое из чисел больше 1000: 999, 1001, 1000?', answer='1001', choice=['999', '1001', '1000']))
lvl_1.add(Task(text='Какое из чисел больше 1000: 500, 1500, 1000?', answer='1500', choice=['500', '1500', '1000']))
lvl_1.add(Task(text='Какое из чисел больше 1000: 800, 900, 1100?', answer='1100', choice=['800', '900', '1100']))

lvl_2 = Level(1, info='Найдите число в последовательности')
lvl_2.add(Task(text='Найдите пропущенное число в последовательности: 1005, 1010, ___, 1020, 1025', answer='1015'))
lvl_2.add(Task(text='Найдите пропущенное число в последовательности: 1500, 1600, ___, 1800, 1900', answer='1700'))
lvl_2.add(Task(text='Найдите пропущенное число в последовательности: 2000, 2005, 2010, ___, 2020', answer='2015'))

lvl_3 = Level(1, info='Сравнение чисел')
lvl_3.add(Task(text='Сравните числа, используя знаки >, < или =: 1500 ___ 1499', answer='>', choice=['>', '<', '=']))
lvl_3.add(Task(text='Сравните числа, используя знаки >, < или =: 2001 ___ 2001', answer='=', choice=['>', '<', '=']))
lvl_3.add(Task(text='Сравните числа, используя знаки >, < или =: 2500 ___ 2600', answer='<', choice=['>', '<', '=']))

lvl_4 = Level(1, info='Еще на нумерацию.')
lvl_4.add(Task(text='Сравните числа, используя знаки >, < или =: 345 ___ 543', answer='<', choice=['<', '>', '=']))
lvl_4.add(Task(text='Сравните числа, используя знаки >, < или =: 876 ___ 768', answer='>', choice=['<', '>', '=']))
lvl_4.add(Task(text='Сравните числа, используя знаки >, < или =: 490 ___ 490', answer='=', choice=['<', '>', '=']))

lvl_5 = Level(1, info='Арифметические операции с числами больше 1000')
lvl_5.add(Task(text='Увеличьте число 1100 на 150', answer='1250'))
lvl_5.add(Task(text='Уменьшите число 2000 на 500', answer='1500'))
lvl_5.add(Task(text='Увеличьте число 3000 на 1000', answer='4000'))
lvl_5.add(Task(text='Уменьшите число 4000 на 1000', answer='3000'))

lvl_6 = Level(1, info='еще чучуть!')
lvl_6.add(Task(text='Если из числа 900 вычесть 300, какое число получится?', answer='600'))
lvl_6.add(Task(text='Сколько десятков содержится в числе 360?', answer='36'))
lvl_6.add(Task(text='Если к числу 400 прибавить 100, какое число получится?', answer='500'))

lvl_7 = Level(1, info='Примеры!')
lvl_7.add(Task(text='(50 - 38) : 4', answer='3'))
lvl_7.add(Task(text='24 : 4', answer='6'))
lvl_7.add(Task(text='36 : 6', answer='6'))

lvl_8 = Level(1, info='Проверка на четность')
lvl_8.add(Task(text='Является ли число 1102 четным?', answer='Да', choice=['Да', 'Нет']))
lvl_8.add(Task(text='Является ли число 1509 четным?', answer='Нет', choice=['Да', 'Нет']))
lvl_8.add(Task(text='Является ли число 2100 четным?', answer='Да', choice=['Да', 'Нет']))

lvl_9 = Level(1, info='осталось совсем чучуть')
lvl_9.add(Task(text='Какое число получится, если к числу 250 прибавить 150?', answer='400'))
lvl_9.add(Task(text='Найди разницу между числами 800 и 450.', answer='350'))
lvl_9.add(Task(text='Выпиши пропущенные числа в последовательности: 100, 110, ___, 130, 140', answer='120'))
lvl_9.add(Task(text='Какое число находится между 500 и 600?', answer='550'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='Какое из чисел больше 1000: 500, 1500, 1000?', answer='1500', choice=['500', '1500', '1000']))
lvl_10.add(Task(text='Какое из чисел больше 1000: 800, 900, 1100?', answer='1100', choice=['800', '900', '1100']))
lvl_10.add(Task(text='Сравните числа, используя знаки >, < или =: 876 ___ 768', answer='>', choice=['<', '>', '=']))
lvl_10.add(Task(text='Сравните числа, используя знаки >, < или =: 490 ___ 490', answer='=', choice=['<', '>', '=']))
lvl_10.add(Task(text='Сколько десятков содержится в числе 360?', answer='36'))
lvl_10.add(Task(text='Если к числу 400 прибавить 100, какое число получится?', answer='500'))
lvl_10.add(Task(text='Найди длину стороны квадрата, если его периметр 24 см.', answer='6'))

topic_2.add_level(lvl_1)
topic_2.add_level(lvl_2)
topic_2.add_level(lvl_3)
topic_2.add_level(lvl_4)
topic_2.add_level(lvl_5)
topic_2.add_level(lvl_6)
topic_2.add_level(lvl_7)
topic_2.add_level(lvl_8)
topic_2.add_level(lvl_9)
topic_2.add_level(lvl_10)
year_4.add_level(topic_2)


topic_3 = Topic('скорости, расстояния и времени')

lvl_1 = Level(1, info='Нахождение времени по скорости и расстоянию')
lvl_1.add(Task(text='Если автомобиль едет со скоростью 60 км/ч, сколько времени ему потребуется, чтобы проехать 120 км?', answer='2'))
lvl_1.add(Task(text='Если велосипедист едет со скоростью 15 км/ч, сколько времени ему потребуется, чтобы проехать 45 км?', answer='3'))
lvl_1.add(Task(text='Если пешеход идет со скоростью 5 км/ч, сколько времени ему потребуется, чтобы пройти 15 км?', answer='3'))

lvl_2 = Level(1, info='Нахождение скорости по расстоянию и времени')
lvl_2.add(Task(text='Если автобус проехал 240 км за 4 часа, какая была его скорость?', answer='60'))
lvl_2.add(Task(text='Если поезд прошел 300 км за 5 часов, какая была его скорость?', answer='60'))
lvl_2.add(Task(text='Если самолет пролетел 600 км за 2 часа, какая была его скорость?', answer='300'))


lvl_3 = Level(1, info='Нахождение расстояния по скорости и времени')
lvl_3.add(Task(text='Если автомобиль двигался со скоростью 80 км/ч в течение 2 часов, какое расстояние он проехал?', answer='160'))
lvl_3.add(Task(text='Если велосипедист двигался со скоростью 20 км/ч в течение 3 часов, какое расстояние он проехал?', answer='60'))
lvl_3.add(Task(text='Если пешеход шел со скоростью 6 км/ч в течение 4 часов, какое расстояние он прошел?', answer='24'))

lvl_4 = Level(1, info='Расстояние между двумя точками')
lvl_4.add(Task(text='Если скорость машины составляет 50 км/ч, а она движется в течение 3 часов, какое расстояние она преодолеет?', answer='150'))
lvl_4.add(Task(text='Если скорость велосипедиста составляет 15 км/ч, а он движется в течение 2 часов, какое расстояние он преодолеет?', answer='30'))
lvl_4.add(Task(text='Если скорость пешехода составляет 6 км/ч, а он движется в течение 5 часов, какое расстояние он преодолеет?', answer='30'))


lvl_5 = Level(1, info='Смешанные задачи')
lvl_5.add(Task(text='Мотоциклист двигался со скоростью 80 км/ч в течение 2.5 часов. Сколько километров он проехал?', answer='200'))
lvl_5.add(Task(text='Поезд двигался со скоростью 100 км/ч в течение 3 часов. Какое расстояние он преодолел?', answer='300'))
lvl_5.add(Task(text='Лыжник двигался со скоростью 15 км/ч в течение 2 часов. Какое расстояние он преодолел?', answer='30'))

lvl_6 = Level(1, info='Нахождение времени при различных скоростях')
lvl_6.add(Task(text='Если пешеход идет со скоростью 5 км/ч, сколько времени ему потребуется, чтобы пройти 25 км?', answer='5'))
lvl_6.add(Task(text='Если автомобиль едет со скоростью 60 км/ч, сколько времени ему потребуется, чтобы проехать 180 км?', answer='3'))
lvl_6.add(Task(text='Если велосипедист едет со скоростью 20 км/ч, сколько времени ему потребуется, чтобы проехать 40 км?', answer='2'))


lvl_7 = Level(1, info='Нахождение времени по скорости и расстоянию!')
lvl_7.add(Task(text='Если автомобиль едет со скоростью 60 км/ч, сколько времени ему потребуется, чтобы проехать 120 км?', answer='2 часа', choice=['1 час', '2 часа', '3 часа']))
lvl_7.add(Task(text='Если велосипедист едет со скоростью 15 км/ч, сколько времени ему потребуется, чтобы проехать 45 км?', answer='3 часа', choice=['2 часа', '3 часа', '4 часа']))
lvl_7.add(Task(text='Если пешеход идет со скоростью 5 км/ч, сколько времени ему потребуется, чтобы пройти 15 км?', answer='3 часа', choice=['2 часа', '3 часа', '4 часа']))


lvl_8 = Level(1, info='Нахождение скорости по расстоянию и времени')
lvl_8.add(Task(text='Если автобус проехал 240 км за 4 часа, какая была его скорость?', answer='60 км/ч', choice=['40 км/ч', '60 км/ч', '80 км/ч']))
lvl_8.add(Task(text='Если поезд прошел 300 км за 5 часов, какая была его скорость?', answer='60 км/ч', choice=['50 км/ч', '60 км/ч', '70 км/ч']))
lvl_8.add(Task(text='Если самолет пролетел 600 км за 2 часа, какая была его скорость?', answer='300 км/ч', choice=['200 км/ч', '300 км/ч', '400 км/ч']))


lvl_9 = Level(1, info='осталось совсем чучуть')
lvl_9.add(Task(text='Какое число получится, если к числу 250 прибавить 150?', answer='400'))
lvl_9.add(Task(text='Найди разницу между числами 800 и 450.', answer='350'))
lvl_9.add(Task(text='Выпиши пропущенные числа в последовательности: 100, 110, ___, 130, 140', answer='120'))
lvl_9.add(Task(text='Какое число находится между 500 и 600?', answer='550'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='Если поезд прошел 300 км за 5 часов, какая была его скорость?', answer='60'))
lvl_10.add(Task(text='Если самолет пролетел 600 км за 2 часа, какая была его скорость?', answer='300'))
lvl_10.add(Task(text='Если поезд прошел 300 км за 5 часов, какая была его скорость?', answer='60 км/ч', choice=['50 км/ч', '60 км/ч', '70 км/ч']))
lvl_10.add(Task(text='Если самолет пролетел 600 км за 2 часа, какая была его скорость?', answer='300 км/ч', choice=['200 км/ч', '300 км/ч', '400 км/ч']))
lvl_10.add(Task(text='Если автомобиль едет со скоростью 60 км/ч, сколько времени ему потребуется, чтобы проехать 180 км?', answer='3'))
lvl_10.add(Task(text='Если велосипедист едет со скоростью 20 км/ч, сколько времени ему потребуется, чтобы проехать 40 км?', answer='2'))
lvl_10.add(Task(text='Если скорость велосипедиста составляет 15 км/ч, а он движется в течение 2 часов, какое расстояние он преодолеет?', answer='30'))
lvl_10.add(Task(text='Если скорость пешехода составляет 6 км/ч, а он движется в течение 5 часов, какое расстояние он преодолеет?', answer='30'))
lvl_10.add(Task(text='Если велосипедист едет со скоростью 15 км/ч, сколько времени ему потребуется, чтобы проехать 45 км?', answer='3'))
lvl_10.add(Task(text='Если пешеход идет со скоростью 5 км/ч, сколько времени ему потребуется, чтобы пройти 15 км?', answer='3'))


topic_3.add_level(lvl_1)
topic_3.add_level(lvl_2)
topic_3.add_level(lvl_3)
topic_3.add_level(lvl_4)
topic_3.add_level(lvl_5)
topic_3.add_level(lvl_6)
topic_3.add_level(lvl_7)
topic_3.add_level(lvl_8)
topic_3.add_level(lvl_9)
topic_3.add_level(lvl_10)
year_4.add_level(topic_3)


topic_4 = Topic('умножения чисел, оканчивающихся нулями')

lvl_1 = Level(1, info='Умножение двузначного числа на число с нулями')
lvl_1.add(Task(text='Сколько будет 20 * 10?', answer='200'))
lvl_1.add(Task(text='Сколько будет 30 * 100?', answer='3000'))
lvl_1.add(Task(text='Сколько будет 40 * 1000?', answer='40000'))


lvl_2 = Level(1, info='Умножение трехзначного числа на число с нулями')
lvl_2.add(Task(text='Сколько будет 150 * 10?', answer='1500'))
lvl_2.add(Task(text='Сколько будет 250 * 100?', answer='25000'))
lvl_2.add(Task(text='Сколько будет 350 * 1000?', answer='350000'))


lvl_3 = Level(1, info='Умножение числа с нулями на число с нулями')
lvl_3.add(Task(text='Сколько будет 1000 * 100?', answer='100000'))
lvl_3.add(Task(text='Сколько будет 5000 * 10?', answer='50000'))
lvl_3.add(Task(text='Сколько будет 70000 * 1000?', answer='70000000'))

lvl_4 = Level(1, info='Умножение больших чисел, оканчивающихся нулями')
lvl_4.add(Task(text='Сколько будет 120 * 500?', answer='60000', choice=['60000', '6000', '600000', '600']))
lvl_4.add(Task(text='Сколько будет 250 * 800?', answer='200000', choice=['200000', '20000', '2000000', '2000']))
lvl_4.add(Task(text='Сколько будет 900 * 700?', answer='630000', choice=['630000', '63000', '6300000', '6300']))


lvl_5 = Level(1, info='Смешанные задачи')
lvl_5.add(Task(text='Мотоциклист двигался со скоростью 80 км/ч в течение 2.5 часов. Сколько километров он проехал?', answer='200'))
lvl_5.add(Task(text='Поезд двигался со скоростью 100 км/ч в течение 3 часов. Какое расстояние он преодолел?', answer='300'))
lvl_5.add(Task(text='Лыжник двигался со скоростью 15 км/ч в течение 2 часов. Какое расстояние он преодолел?', answer='30'))

lvl_6 = Level(1, info='Решение простых задач')
lvl_6.add(Task(text='Сколько будет 80 * 40?', answer='3200', choice=['3200', '320', '32000', '320000']))
lvl_6.add(Task(text='Сколько будет 60 * 50?', answer='3000', choice=['3000', '300', '30000', '300000']))
lvl_6.add(Task(text='Сколько будет 70 * 20?', answer='1400', choice=['1400', '140', '14000', '140000']))


lvl_7 = Level(1, info='Умножение чисел с ненулевым остатком')
lvl_7.add(Task(text='Сколько будет 70 * 40?', answer='2800', choice=['2800', '280', '28000', '280000']))
lvl_7.add(Task(text='Сколько будет 90 * 50?', answer='4500', choice=['4500', '450', '45000', '450000']))
lvl_7.add(Task(text='Сколько будет 120 * 30?', answer='3600', choice=['3600', '360', '36000', '360000']))


lvl_8 = Level(1, info='Нахождение скорости по расстоянию и времени')
lvl_8.add(Task(text='(50 - 38) : 4', answer='3'))
lvl_8.add(Task(text='24 : 4', answer='6'))
lvl_8.add(Task(text='36 : 6', answer='6'))

lvl_9 = Level(1, info='осталось совсем чучуть')
lvl_9.add(Task(text='Сравните числа, используя знаки >, < или =: 345 ___ 543', answer='<', choice=['<', '>', '=']))
lvl_9.add(Task(text='Сравните числа, используя знаки >, < или =: 876 ___ 768', answer='>', choice=['<', '>', '=']))
lvl_9.add(Task(text='Сравните числа, используя знаки >, < или =: 490 ___ 490', answer='=', choice=['<', '>', '=']))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='Сравните числа, используя знаки >, < или =: 876 ___ 768', answer='>', choice=['<', '>', '=']))
lvl_10.add(Task(text='Сравните числа, используя знаки >, < или =: 490 ___ 490', answer='=', choice=['<', '>', '=']))
lvl_10.add(Task(text='Сколько будет 60 * 50?', answer='3000', choice=['3000', '300', '30000', '300000']))
lvl_10.add(Task(text='Сколько будет 70 * 20?', answer='1400', choice=['1400', '140', '14000', '140000']))
lvl_10.add(Task(text='Сколько будет 30 * 100?', answer='3000'))
lvl_10.add(Task(text='Сколько будет 40 * 1000?', answer='40000'))
lvl_10.add(Task(text='Сколько будет 60 * 50?', answer='3000', choice=['3000', '300', '30000', '300000']))
lvl_10.add(Task(text='Сколько будет 70 * 20?', answer='1400', choice=['1400', '140', '14000', '140000']))
lvl_10.add(Task(text='Сколько будет 40 * 1000?', answer='40000'))
lvl_10.add(Task(text='24 : 4', answer='6'))
lvl_10.add(Task(text='36 : 6', answer='6'))


topic_4.add_level(lvl_1)
topic_4.add_level(lvl_2)
topic_4.add_level(lvl_3)
topic_4.add_level(lvl_4)
topic_4.add_level(lvl_5)
topic_4.add_level(lvl_6)
topic_4.add_level(lvl_7)
topic_4.add_level(lvl_8)
topic_4.add_level(lvl_9)
topic_4.add_level(lvl_10)
year_4.add_level(topic_4)


topic_5 = Topic('Деление чисел, оканчивающихся нулями')

lvl_1 = Level(1, info='Деление чисел, оканчивающихся нулями')
lvl_1.add(Task(text='Сколько будет 6000 / 300?', answer='20', choice=['20', '200', '2', '2000']))
lvl_1.add(Task(text='Сколько будет 8000 / 400?', answer='20', choice=['20', '200', '2', '2000']))
lvl_1.add(Task(text='Сколько будет 5000 / 50?', answer='100', choice=['100', '1000', '10', '200']))


lvl_2 = Level(1, info='Проверка правильности деления')
lvl_2.add(Task(text='Правильно ли вычислено: 4000 / 200 = 40?', answer='Да', choice=['Да', 'Нет']))
lvl_2.add(Task(text='Правильно ли вычислено: 6000 / 1000 = 600?', answer='Да', choice=['Да', 'Нет']))
lvl_2.add(Task(text='Правильно ли вычислено: 9000 / 90 = 100?', answer='Да', choice=['Да', 'Нет']))


lvl_3 = Level(1, info='Деление больших чисел, оканчивающихся нулями')
lvl_3.add(Task(text='Сколько будет 90000 / 300?', answer='300', choice=['300', '3000', '30', '3']))
lvl_3.add(Task(text='Сколько будет 60000 / 600?', answer='100', choice=['100', '1000', '10', '1']))
lvl_3.add(Task(text='Сколько будет 80000 / 80?', answer='1000', choice=['1000', '10000', '10', '1']))


lvl_4 = Level(1, info='Решение простых задач')
lvl_4.add(Task(text='Сколько будет 4000 / 200?', answer='20', choice=['20', '200', '2', '2000']))
lvl_4.add(Task(text='Сколько будет 7000 / 70?', answer='100', choice=['100', '1000', '10', '200']))
lvl_4.add(Task(text='Сколько будет 8000 / 800?', answer='10', choice=['10', '100', '1', '1000']))


lvl_5 = Level(1, info='Деление многозначных чисел на числа, оканчивающиеся нулями')
lvl_5.add(Task(text='Сколько будет 50000 / 500?', answer='100', choice=['100', '1000', '10', '1']))
lvl_5.add(Task(text='Сколько будет 90000 / 900?', answer='100', choice=['100', '1000', '10', '1']))
lvl_5.add(Task(text='Сколько будет 60000 / 6000?', answer='10', choice=['10', '100', '1', '1000']))


lvl_6 = Level(1, info='Деление чисел с нулевым остатком')
lvl_6.add(Task(text='Сколько будет 8000 / 80?', answer='100', choice=['100', '1000', '10', '1']))
lvl_6.add(Task(text='Сколько будет 70000 / 700?', answer='100', choice=['100', '1000', '10', '1']))
lvl_6.add(Task(text='Сколько будет 60000 / 60?', answer='1000', choice=['1000', '10000', '10', '1']))


lvl_7 = Level(1, info='Деление чисел с ненулевым остатком')
lvl_7.add(Task(text='Сколько будет 5000 / 80?', answer='62', choice=['62', '63', '61', '64']))
lvl_7.add(Task(text='Сколько будет 7000 / 90?', answer='77', choice=['77', '78', '76', '75']))
lvl_7.add(Task(text='Сколько будет 6000 / 95?', answer='63', choice=['63', '64', '62', '61']))


lvl_8 = Level(1, info='Примеры!')
lvl_8.add(Task(text='1 * 26', answer='26'))
lvl_8.add(Task(text='0 * (21 - 8)', answer='0'))
lvl_8.add(Task(text='17 + 80 + 3', answer='100'))

lvl_9 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_9.add(Task(text='+ или -', choice=['-', '+', '*', '/'], answer='+', image='pic/28.jpg'))
lvl_9.add(Task(text='Выберите знак', choice=['-', '+', '*', '/'], answer='-', image='pic/29.jpg'))
lvl_9.add(Task(text='Ну и последний раз', choice=['-', '+', '*', '/'], answer='+', image='pic/30.jpg'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='Сколько будет 7000 / 90?', answer='77', choice=['77', '78', '76', '75']))
lvl_10.add(Task(text='Сколько будет 6000 / 95?', answer='63', choice=['63', '64', '62', '61']))
lvl_10.add(Task(text='Ну и последний раз', choice=['-', '+', '*', '/'], answer='+', image='pic/30.jpg'))
lvl_10.add(Task(text='Сколько будет 70000 / 700?', answer='100', choice=['100', '1000', '10', '1']))
lvl_10.add(Task(text='Сколько будет 60000 / 60?', answer='1000', choice=['1000', '10000', '10', '1']))
lvl_10.add(Task(text='Сколько будет 60000 / 600?', answer='100', choice=['100', '1000', '10', '1']))
lvl_10.add(Task(text='Сколько будет 80000 / 80?', answer='1000', choice=['1000', '10000', '10', '1']))
lvl_10.add(Task(text='Сколько будет 8000 / 400?', answer='20', choice=['20', '200', '2', '2000']))
lvl_10.add(Task(text='Сколько будет 5000 / 50?', answer='100', choice=['100', '1000', '10', '200']))
lvl_10.add(Task(text='Сколько будет 90000 / 900?', answer='100', choice=['100', '1000', '10', '1']))
lvl_10.add(Task(text='Сколько будет 60000 / 6000?', answer='10', choice=['10', '100', '1', '1000']))
lvl_10.add(Task(text='Сколько будет 7000 / 70?', answer='100', choice=['100', '1000', '10', '200']))
lvl_10.add(Task(text='Сколько будет 8000 / 800?', answer='10', choice=['10', '100', '1', '1000']))

topic_5.add_level(lvl_1)
topic_5.add_level(lvl_2)
topic_5.add_level(lvl_3)
topic_5.add_level(lvl_4)
topic_5.add_level(lvl_5)
topic_5.add_level(lvl_6)
topic_5.add_level(lvl_7)
topic_5.add_level(lvl_8)
topic_5.add_level(lvl_9)
topic_5.add_level(lvl_10)
year_4.add_level(topic_5)


topic_6 = Topic('умножения и деления на трехзначные и двухзначные числа')

lvl_1 = Level(1, info='Умножение на трехзначное число')
lvl_1.add(Task(text='Сколько будет 123 * 4?', answer='492', choice=['492', '4920', '49200', '49']))
lvl_1.add(Task(text='Сколько будет 256 * 3?', answer='768', choice=['768', '7680', '76800', '76']))
lvl_1.add(Task(text='Сколько будет 345 * 5?', answer='1725', choice=['1725', '17250', '172500', '172']))


lvl_2 = Level(1, info='Умножение на двузначное число')
lvl_2.add(Task(text='Сколько будет 87 * 6?', answer='522', choice=['522', '5220', '52200', '52']))
lvl_2.add(Task(text='Сколько будет 56 * 9?', answer='504', choice=['504', '5040', '50400', '50']))
lvl_2.add(Task(text='Сколько будет 72 * 4?', answer='288', choice=['288', '2880', '28800', '28']))



lvl_3 = Level(1, info='Деление на трехзначное число')
lvl_3.add(Task(text='Сколько будет 600 / 4?', answer='150', choice=['150', '15', '1.5', '0.15']))
lvl_3.add(Task(text='Сколько будет 800 / 8?', answer='100', choice=['100', '10', '1', '0.1']))
lvl_3.add(Task(text='Сколько будет 900 / 9?', answer='100', choice=['100', '10', '1', '0.1']))


lvl_4 = Level(1, info='Деление на двузначное число')
lvl_4.add(Task(text='Сколько будет 300 / 6?', answer='50', choice=['50', '5', '0.5', '0.05']))
lvl_4.add(Task(text='Сколько будет 400 / 4?', answer='100', choice=['100', '10', '1', '0.1']))
lvl_4.add(Task(text='Сколько будет 600 / 3?', answer='200', choice=['200', '20', '2', '0.2']))


lvl_5 = Level(1, info='Деление на двузначное число')
lvl_5.add(Task(text='Сколько будет 300 / 6?', answer='50'))
lvl_5.add(Task(text='Сколько будет 400 / 4?', answer='100'))
lvl_5.add(Task(text='Сколько будет 600 / 3?', answer='200'))


lvl_6 = Level(1, info='Деление на трехзначное число')
lvl_6.add(Task(text='Сколько будет 600 / 4?', answer='150'))
lvl_6.add(Task(text='Сколько будет 800 / 8?', answer='100'))
lvl_6.add(Task(text='Сколько будет 900 / 9?', answer='100'))


lvl_7 = Level(1, info='повтарим пройденое')
lvl_7.add(Task(text='Сколько будет 70 * 40?', answer='2800', choice=['2800', '280', '28000', '280000']))
lvl_7.add(Task(text='Сколько будет 90 * 50?', answer='4500', choice=['4500', '450', '45000', '450000']))
lvl_7.add(Task(text='Сколько будет 120 * 30?', answer='3600', choice=['3600', '360', '36000', '360000']))
lvl_7.add(Task(text='Если автобус проехал 240 км за 4 часа, какая была его скорость?', answer='60 км/ч', choice=['40 км/ч', '60 км/ч', '80 км/ч']))
lvl_7.add(Task(text='Если поезд прошел 300 км за 5 часов, какая была его скорость?', answer='60 км/ч', choice=['50 км/ч', '60 км/ч', '70 км/ч']))
lvl_7.add(Task(text='Если самолет пролетел 600 км за 2 часа, какая была его скорость?', answer='300 км/ч', choice=['200 км/ч', '300 км/ч', '400 км/ч']))


lvl_8 = Level(1, info='еще чучуть')
lvl_8.add(Task(text='Сколько будет 30 * 100?', answer='3000'))
lvl_8.add(Task(text='Сколько будет 40 * 1000?', answer='40000'))
lvl_8.add(Task(text='Сколько будет 60000 / 6000?', answer='10', choice=['10', '100', '1', '1000']))


lvl_9 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_9.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_9.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='Сколько будет 120 * 30?', answer='3600', choice=['3600', '360', '36000', '360000']))
lvl_10.add(Task(text='Если автобус проехал 240 км за 4 часа, какая была его скорость?', answer='60 км/ч', choice=['40 км/ч', '60 км/ч', '80 км/ч']))
lvl_10.add(Task(text='Если поезд прошел 300 км за 5 часов, какая была его скорость?', answer='60 км/ч', choice=['50 км/ч', '60 км/ч', '70 км/ч']))
lvl_10.add(Task(text='Если самолет пролетел 600 км за 2 часа, какая была его скорость?', answer='300 км/ч', choice=['200 км/ч', '300 км/ч', '400 км/ч']))
lvl_10.add(Task(text='Сколько будет 40 * 1000?', answer='40000'))
lvl_10.add(Task(text='Сколько будет 60000 / 6000?', answer='10', choice=['10', '100', '1', '1000']))
lvl_10.add(Task(text='Сколько будет 800 / 8?', answer='100'))
lvl_10.add(Task(text='Сколько будет 900 / 9?', answer='100'))
lvl_10.add(Task(text='Сколько будет 400 / 4?', answer='100', choice=['100', '10', '1', '0.1']))
lvl_10.add(Task(text='Сколько будет 600 / 3?', answer='200', choice=['200', '20', '2', '0.2']))


topic_6.add_level(lvl_1)
topic_6.add_level(lvl_2)
topic_6.add_level(lvl_3)
topic_6.add_level(lvl_4)
topic_6.add_level(lvl_5)
topic_6.add_level(lvl_6)
topic_6.add_level(lvl_7)
topic_6.add_level(lvl_8)
topic_6.add_level(lvl_9)
topic_6.add_level(lvl_10)
year_4.add_level(topic_6)


topic_7 = Topic('Давай повтарим прошлые классы и будет готовится к финлальному тесту')

lvl_1 = Level(1, info='повтри все за первый класс')
lvl_1.add(Task(text='Сколько же здесь грибов?', answer='8', image='pic/2.jpg'))
lvl_1.add(Task(text='А здесь сколько девочек?', answer='4', image='pic/3.jpg'))
lvl_1.add(Task(text='Какая палочка самая длинная?', choice=['1', '2', '3'], answer='3', image='pic/18.jpg'))
lvl_1.add(Task(text='Какая морковка самая короткая?', choice=['1', '2', '3'], answer='1', image='pic/18.jpg'))


lvl_2 = Level(1, info='ещё')
lvl_2.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_2.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))
lvl_2.add(Task(text='', answer='1', image='pic/33.jpg'))
lvl_2.add(Task(text='Ну и последний раз', answer='5', image='pic/34.jpg'))


lvl_3 = Level(1, info='это еще не все')
lvl_3.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_3.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))
lvl_3.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_3.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))


lvl_4 = Level(1, info='пока все просто ...')
lvl_4.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_4.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_4.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))
lvl_4.add(Task(text='', choice=['<', '>', '='], answer='>', image='pic/36.jpg'))
lvl_4.add(Task(text='', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))


lvl_5 = Level(1, info='таккк еще попробуй ')
lvl_5.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))
lvl_5.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_5.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))
lvl_5.add(Task(text='если у фигуры 3 угла как ее называют?', answer='треугольник',
               choice=['триугольник', 'восьмиугольник', 'пятиугольник']))
lvl_5.add(Task(text='если у фигуры 6 угла как ее называют?', answer='шестиугольник',
               choice=['триугольник', 'шестиугольник', 'пятиугольник']))


lvl_6 = Level(1, info='давай повтарим прошлые темы')
lvl_6.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_6.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))


lvl_7 = Level(1, info='еще')
lvl_7.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_7.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))

lvl_8 = Level(1, info='еще чучуть')
lvl_8.add(Task(text='Сколько будет 30 * 100?', answer='3000'))
lvl_8.add(Task(text='Сколько будет 40 * 1000?', answer='40000'))
lvl_8.add(Task(text='Сколько будет 60000 / 6000?', answer='10', choice=['10', '100', '1', '1000']))


lvl_9 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_9.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_9.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='А на третьей картинке яблоко лежит', choice=['Под стулом', 'Около стула', 'За стулом', "На стуле"],
               answer='Около стула', image='pic/14.jpg'))
lvl_10.add(Task(text='Сколько будет 60000 / 6000?', answer='10', choice=['10', '100', '1', '1000']))
lvl_10.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))
lvl_10.add(Task(text='если у фигуры 6 угла как ее называют?', answer='шестиугольник',
               choice=['триугольник', 'шестиугольник', 'пятиугольник']))
lvl_10.add(Task(text='', choice=['<', '>', '='], answer='>', image='pic/36.jpg'))
lvl_10.add(Task(text='', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))

topic_7.add_level(lvl_1)
topic_7.add_level(lvl_2)
topic_7.add_level(lvl_3)
topic_7.add_level(lvl_4)
topic_7.add_level(lvl_5)
topic_7.add_level(lvl_6)
topic_7.add_level(lvl_7)
topic_7.add_level(lvl_8)
topic_7.add_level(lvl_9)
topic_7.add_level(lvl_10)
year_4.add_level(topic_7)


topic_8 = Topic('Теперь второй класс')

lvl_1 = Level(1, info='Привет! Называй виды углов!')
lvl_1.add(Task(text='Какой это угол?', answer='Тупой', image='pic/108.jpg', choice=['Тупой', 'Прямой', 'Острый']))
lvl_1.add(Task(text='А этот угол?', answer='Прямой', image='pic/109.jpg', choice=['Тупой', 'Прямой', 'Острый']))
lvl_1.add(Task(text='Ну а этот?', answer='Острый', image='pic/110.jpg', choice=['Тупой', 'Прямой', 'Острый']))
lvl_1.add(Task(text='Сколько здесь тупых углов?', answer='2', image='pic/111.jpg'))


lvl_2 = Level(1, info='Что называют квадратом?.')
lvl_2.add(Task(text='Это квадрат?', answer='Нет', image='pic/117.jpg', choice=['Да', 'Нет']))
lvl_2.add(Task(text='А это квадрат?', answer='Нет', image='pic/118.jpg', choice=['Да', 'Нет']))
lvl_2.add(Task(text='Что насчёт этой фигуры, квадрат?', answer='Да', image='pic/119.jpg', choice=['Да', 'Нет']))
lvl_2.add(Task(text='Это квадрат?', answer='Нет', image='pic/120.jpg', choice=['Да', 'Нет']))

lvl_3 = Level(1, info='Реши уравнения!')
lvl_3.add(Task(text='х - 8 = 75', answer='83'))
lvl_3.add(Task(text='14 - х = 6', answer='8'))


lvl_4 = Level(1, info='Вычисли, заменяя умножение сложением.')
lvl_4.add(Task(text='2 * 5', answer='10'))
lvl_4.add(Task(text='4 * 3', answer='12'))
lvl_4.add(Task(text='7 * 4', answer='28'))
lvl_4.add(Task(text='9 * 3', answer='27'))


lvl_5 = Level(1, info='Проверь выражения и напиши Верно или Неверно')
lvl_5.add(Task(text='4 * 7 + 4 = 4 * 8', answer='Верно', choice=['Верно', "Неверно"]))
lvl_5.add(Task(text='27 : 3 < 10', answer='Верно', choice=['Верно', "Неверно"]))
lvl_5.add(Task(text='48 + (14 - 12) > 50', answer='Неверно', choice=['Верно', "Неверно"]))


lvl_6 = Level(1, info='ну это элементарно!!!')
lvl_6.add(Task(text="3+?=3", answer='0'))
lvl_6.add(Task(text="?+1=1", answer='0'))
lvl_6.add(Task(text="8+?=8", answer='0'))


lvl_7 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_7.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_7.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_7.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))

lvl_8 = Level(1, info='давай повтарим перед тестом')
lvl_8.add(Task(text='под каким номером фигура с 12 углами?', answer='7', image='pic/42.jpg'))
lvl_8.add(Task(text='сколько углов у синей фигуры?', answer='8', image='pic/40.jpg'))
lvl_8.add(Task(text='6+3', answer='9'))
lvl_8.add(Task(text='5-?=3', answer="2"))

lvl_9 = Level(1, info="последний раз")
lvl_9.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_9.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))


lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='6+3', answer='9'))
lvl_10.add(Task(text='5-?=3', answer="2"))
lvl_10.add(Task(text="?+1=1", answer='0'))
lvl_10.add(Task(text="8+?=8", answer='0'))
lvl_10.add(Task(text='Что насчёт этой фигуры, квадрат?', answer='Да', image='pic/119.jpg', choice=['Да', 'Нет']))
lvl_10.add(Task(text='Это квадрат?', answer='Нет', image='pic/120.jpg', choice=['Да', 'Нет']))

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
year_4.add_level(topic_8)


topic_9 = Topic('Теперь третий класс')

lvl_1 = Level(1, info='Теперь просто без лишникх слов поделеи и поумнажаем')
lvl_1.add(Task(text="3 * 2 / 3 =", answer="2"))
lvl_1.add(Task(text="4 * 8 / 1 =", answer="32"))
lvl_1.add(Task(text="6 * 7 / 6 =", answer="7"))


lvl_2 = Level(1, info='Продолжаем!')
lvl_2.add(Task(text="24 * 1 =", answer="24"))
lvl_2.add(Task(text="30 * 1 =", answer="30"))
lvl_2.add(Task(text="22 * 1 =", answer="22"))
lvl_2.add(Task(text="51 * 1 =", answer="51"))


lvl_3 = Level(1, info='Деление на трехзначное число')
lvl_3.add(Task(text='Сколько будет 600 / 4?', answer='150', choice=['150', '15', '1.5', '0.15']))
lvl_3.add(Task(text='Сколько будет 800 / 8?', answer='100', choice=['100', '10', '1', '0.1']))
lvl_3.add(Task(text='Сколько будет 900 / 9?', answer='100', choice=['100', '10', '1', '0.1']))


lvl_4 = Level(1, info='Давай еще немного по чястям')
lvl_4.add(Task(text='сколько здесь частей выделено?', answer='1', image='pic/58.jpg', choice=['1', '2', '3']))
lvl_4.add(Task(text='а здесь?', answer='1', image='pic/58.jpg', choice=['1', '2', '3']))
lvl_4.add(Task(text='последний раз', answer='1', image='pic/59.jpg', choice=['1', '2', '3']))


lvl_5 = Level(1, info='Вычислительная машина!')
lvl_5.add(Task(text="(5 + 17) / 2 =", answer="11"))
lvl_5.add(Task(text="(7 + 8) / 6 =", answer="2"))
lvl_5.add(Task(text="(11 + 6) / 2 =", answer="8"))
lvl_5.add(Task(text="(21 + 1) / 7 =", answer="3"))
lvl_5.add(Task(text="(7 + 14) / 8 =", answer="2"))


lvl_6 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_6.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_6.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_6.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))


lvl_7 = Level(1, info='Примеры!')
lvl_7.add(Task(text='1 * 26', answer='26'))
lvl_7.add(Task(text='0 * (21 - 8)', answer='0'))
lvl_7.add(Task(text='17 + 80 + 3', answer='100'))


lvl_8 = Level(1, info='Нахождение скорости по расстоянию и времени')
lvl_8.add(Task(text='Если автобус проехал 240 км за 4 часа, какая была его скорость?', answer='60 км/ч', choice=['40 км/ч', '60 км/ч', '80 км/ч']))
lvl_8.add(Task(text='Если поезд прошел 300 км за 5 часов, какая была его скорость?', answer='60 км/ч', choice=['50 км/ч', '60 км/ч', '70 км/ч']))
lvl_8.add(Task(text='Если самолет пролетел 600 км за 2 часа, какая была его скорость?', answer='300 км/ч', choice=['200 км/ч', '300 км/ч', '400 км/ч']))


lvl_9 = Level(1, info='Реши уравнения')
lvl_9.add(Task(text='х : 2 + 21 = 31', answer='5'))
lvl_9.add(Task(text='х * 7 - 6 = 1', answer='1'))
lvl_9.add(Task(text='у * 5 = 20', answer='4'))


lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='х * 7 - 6 = 1', answer='1'))
lvl_10.add(Task(text='у * 5 = 20', answer='4'))
lvl_10.add(Task(text='Найди длину стороны квадрата, если его периметр 24 см.', answer='6'))
lvl_10.add(Task(text='17 + 80 + 3', answer='100'))
lvl_10.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_10.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))
lvl_10.add(Task(text="(7 + 14) / 8 =", answer="2"))
lvl_10.add(Task(text='последний раз', answer='1', image='pic/59.jpg', choice=['1', '2', '3']))

topic_9.add_level(lvl_1)
topic_9.add_level(lvl_2)
topic_9.add_level(lvl_3)
topic_9.add_level(lvl_4)
topic_9.add_level(lvl_5)
topic_9.add_level(lvl_6)
topic_9.add_level(lvl_7)
topic_9.add_level(lvl_8)
topic_9.add_level(lvl_9)
topic_9.add_level(lvl_10)
year_4.add_level(topic_9)



topic_10 = Topic('общие повтарение')

lvl_1 = Level(1, info='повтарим и тест ')
lvl_6.add(Task(text='Если из числа 900 вычесть 300, какое число получится?', answer='600'))
lvl_6.add(Task(text='Сколько десятков содержится в числе 360?', answer='36'))
lvl_6.add(Task(text='Если к числу 400 прибавить 100, какое число получится?', answer='500'))


lvl_2 = Level(1, info='Привет! Определи что больше!')
lvl_2.add(Task(text='Какое из чисел больше 1000: 999, 1001, 1000?', answer='1001', choice=['999', '1001', '1000']))
lvl_2.add(Task(text='Какое из чисел больше 1000: 500, 1500, 1000?', answer='1500', choice=['500', '1500', '1000']))
lvl_2.add(Task(text='Какое из чисел больше 1000: 800, 900, 1100?', answer='1100', choice=['800', '900', '1100']))


lvl_3 = Level(1, info='примеры на 0')
lvl_3.add(Task(text="41 * 0 =", answer="0"))
lvl_3.add(Task(text="27 * 0 =", answer="0"))
lvl_3.add(Task(text="13 * 0 =", answer="0"))


lvl_4 = Level(1, info='Решение простых задач')
lvl_4.add(Task(text='Сколько будет 4000 / 200?', answer='20', choice=['20', '200', '2', '2000']))
lvl_4.add(Task(text='Сколько будет 7000 / 70?', answer='100', choice=['100', '1000', '10', '200']))
lvl_4.add(Task(text='Сколько будет 8000 / 800?', answer='10', choice=['10', '100', '1', '1000']))


lvl_5 = Level(1, info='таккк еще попробуй ')
lvl_5.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))
lvl_5.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_5.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))
lvl_5.add(Task(text='если у фигуры 3 угла как ее называют?', answer='треугольник',
               choice=['триугольник', 'восьмиугольник', 'пятиугольник']))
lvl_5.add(Task(text='если у фигуры 6 угла как ее называют?', answer='шестиугольник',
               choice=['триугольник', 'шестиугольник', 'пятиугольник']))


lvl_6 = Level(1, info='Решение простых задач')
lvl_6.add(Task(text='Сколько будет 80 * 40?', answer='3200', choice=['3200', '320', '32000', '320000']))
lvl_6.add(Task(text='Сколько будет 60 * 50?', answer='3000', choice=['3000', '300', '30000', '300000']))
lvl_6.add(Task(text='Сколько будет 70 * 20?', answer='1400', choice=['1400', '140', '14000', '140000']))

lvl_7 = Level(1, info='еще')
lvl_7.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_7.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))


lvl_8 = Level(1, info='Устные задачи')
lvl_8.add(Task(text='В куске 20 м. ткани. На каждый костюм необходимо 3 м, можно ли сшить 6 таких?', answer='Да',
               choice=['Да', 'Нет']))
lvl_8.add(Task(text='А 7 таких костюмов получится сшить?', answer='Нет', choice=['Да', 'Нет']))
lvl_8.add(Task(text='Найди длину стороны квадрата, если его периметр 24 см.', answer='6'))


lvl_9 = Level(1, info='Реши уравнения')
lvl_9.add(Task(text='х : 2 + 21 = 31', answer='5'))
lvl_9.add(Task(text='х * 7 - 6 = 1', answer='1'))
lvl_9.add(Task(text='у * 5 = 20', answer='4'))


lvl_10 = Level(1, info='все конец 4 класса ураааааа', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='Сколько будет 345 * 5?', answer='1725', choice=['1725', '17250', '172500', '172']))
lvl_10.add(Task(text='у * 5 = 20', answer='4'))
lvl_10.add(Task(text='Сколько будет 800 / 8?', answer='100', choice=['100', '10', '1', '0.1']))
lvl_10.add(Task(text='Сколько будет 900 / 9?', answer='100', choice=['100', '10', '1', '0.1']))
lvl_10.add(Task(text='Сколько будет 250 * 800?', answer='200000', choice=['200000', '20000', '2000000', '2000']))
lvl_10.add(Task(text='Сколько будет 900 * 700?', answer='630000', choice=['630000', '63000', '6300000', '6300']))
lvl_10.add(Task(text='Найдите пропущенное число в последовательности: 685, 686, ___, 688, 689', answer='687'))
lvl_10.add(Task(text='Найдите пропущенное число в последовательности: 999, ___, 997, 996, 995', answer='998'))
lvl_10.add(Task(text='Найдите пропущенное число в последовательности: 685, 686, ___, 688, 689', answer='687'))
lvl_10.add(Task(text='Найдите пропущенное число в последовательности: 999, ___, 997, 996, 995', answer='998'))
lvl_10.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_10.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_10.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))
lvl_10.add(Task(text='На 5 лошадей сели по одному всаднику, сколько всего всадников?', answer='5'))
lvl_10.add(Task(text='После обеда на столе осталось 4 тарелки, ни на одной не осталось ни одной сосиски. Сколько всего сосисок на этих тарелках?', answer='0'))
lvl_10.add(Task(text='54 * 0', answer='0'))
lvl_10.add(Task(text='0 * 100', answer='0'))
lvl_10.add(Task(text='(24 + 21) * 0', answer='0'))
lvl_10.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_10.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_10.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))
lvl_10.add(Task(text="14 / 1 = 7", answer="нет", choice=["да", "нет"]))
lvl_10.add(Task(text="21 / 3 = 7", answer="да", choice=["да", "нет"]))
lvl_10.add(Task(text="18 * 7 = 125", answer="нет", choice=["да", "нет"]))
lvl_10.add(Task(text="20 * 10 = 200", answer="да", choice=["да", "нет"]))


topic_10.add_level(lvl_1)
topic_10.add_level(lvl_2)
topic_10.add_level(lvl_3)
topic_10.add_level(lvl_4)
topic_10.add_level(lvl_5)
topic_10.add_level(lvl_6)
topic_10.add_level(lvl_7)
topic_10.add_level(lvl_8)
topic_10.add_level(lvl_9)
topic_10.add_level(lvl_10)
year_4.add_level(topic_10)
