from company.company_creator import *

year_2 = Class(2)
topic_1 = Topic('Числа от 1 до 100. Нумерация.')
lvl_1 = Level(1, info='Привет! Немного повторения на числа от 1 до 20.')
lvl_1.add(Task(text='Назови число, которы встречаются при счете между 17 и 19', answer='18'))
lvl_1.add(Task(text='А теперь число между 15 и 17', answer='16'))
lvl_1.add(Task(text='Что же находится между 11 и 9?', answer='10'))
lvl_1.add(Task(text='А чему равна сумма чисел между 2 и 5?', answer='7'))

lvl_2 = Level(1, info='Теперь немного примеров!')
lvl_2.add(Task(text='Увеличь на 3 число 7, напиши ответ.', answer='10'))
lvl_2.add(Task(text='А теперь увеличь на 2 число 10', answer='12'))
lvl_2.add(Task(text='Теперь уменьши на 2 число 12', answer='10'))
lvl_2.add(Task(text='Уменьши 9 на 3', answer='6'))

lvl_3 = Level(1, info='Порешаем задачи!')
lvl_3.add(Task(text='В первом ряду кинотеатра 8 мест, а во втором на 2 места больше. Сколько мест во втором ряду?',
               answer='10'))
lvl_3.add(Task(text='А сколько всего мест в кинотеатре?', answer='18'))
lvl_3.add(Task(text='Длина первого звена ломаной 1 дм, а второго 3 см. Какая длина всей этой ломанной в сантиметрах?',
               answer='13'))
lvl_3.add(Task(text='Дима старше Оли на 6 лет, а Даша моложе димы на 4 года. Кто старше: Оля или Даша?', answer='Даша'))

lvl_4 = Level(1, info='Будем учиться вести счёт десятками!')
lvl_4.add(Task(text='Сколько будет 3 дес. + 1 дес.? Ответ дай в десятках.', answer='2'))
lvl_4.add(Task(text='Сколько будет 4 дес. + 5 дес.? Теперь ответ уже числом.', answer='90'))
lvl_4.add(Task(text='А сколько числом 9 дес. - 5 дес.?', answer='40'))
lvl_4.add(Task(text='Сколько будет 5 дес. - 2 дес. числом?', answer='30'))

lvl_5 = Level(1, info='Теперь задачи на десятки!')
lvl_5.add(
    Task(text='У Васи было 3 десятка марок. Он подарил другу 10 марок. Сколько у Васи осталось марок?', answer='20'))
lvl_5.add(Task(text='Папе 40 лет, а маме 30. На сколько лет папа старше мамы?', answer='10'))
lvl_5.add(Task(text='У Вари было 30 пуговиц, она пришила двадцать. Сколько у нее осталось пуговиц?', answer='10'))

lvl_6 = Level(1, info='Добавим к десяткам единицы!')
lvl_6.add(Task(text='Назови число, в котором 1 дес. 9 ед.', answer='19'))
lvl_6.add(Task(text='А теперь число, в котором 9 дес. 1 ед.', answer='91'))
lvl_6.add(Task(text='Назови число, в котором 10 дес.', answer='100'))
lvl_6.add(Task(text='Осталось число, в котором 2 дес. 3 ед.', answer='23'))

lvl_7 = Level(1, info='Какое число пропущено в ряду?')
lvl_7.add(Task(text='39, 40, ?, 42, 43', answer='41'))
lvl_7.add(Task(text='89, ?, 91, 92, 93', answer='90'))
lvl_7.add(Task(text='76, ?, 74, 73, 72', answer='75'))

lvl_8 = Level(1, info='Ребусы!')
lvl_8.add(Task(text='** + 1 = ***. Что обозначено **?', answer='99'))
lvl_8.add(Task(text='39 + ? = 40.', answer='1'))
lvl_8.add(Task(text='? - 1 = 79', answer='80'))
lvl_8.add(Task(text='? + 1 = 90', answer='89'))

lvl_9 = Level(1, info='Задачки.')
lvl_9.add(Task(text='Миша выиграл 6 партий, а Ваня на 2 партии больше. Сколько раз сыграл Миша?', answer='14'))
lvl_9.add(Task(text='У Коли 10 книг дома, он отнёс 2 в школу. Сколько у него осталось книг дома?', answer='8'))
lvl_9.add(Task(text='На столе лежат: морковка, помидор, огурец и свекла.'
                    ' Сколькими способами можно составить набор и двух овощей?', answer='12'))

lvl_10 = Level(1, info='Закрепим материалы!', style='test', time=60, topic='Числа   от   1   до   100. Нумерация.')
lvl_10.add(Task(text='Назови число, в котором 3 дес. 9 ед.', answer='39'))
lvl_10.add(Task(text='На столе лежат: помидор, кабачок и картошка. Сколькими '
                     'способами можно составить набор и двух овощей?', answer='6'))
lvl_10.add(Task(text='? - 6 = 74', answer='80'))
lvl_10.add(Task(text='86, 85, ?, 83, 82', answer='84'))
lvl_10.add(Task(text='Петя выиграл 2 партии, а Ваня на 6 партии больше. Сколько раз сыграл Ваня?', answer='10'))
lvl_10.add(
    Task(text='В первом ряду кинотеатра 10 мест, а во втором на 4 места больше. Сколько всего мест?', answer='24'))
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
year_2.add_level(topic_1)

topic_2 = Topic('Числа от 1 до 100. Сложение и вычитание')
lvl_1 = Level(1, info='Привет! Рассмотрим отрезки.')
lvl_1.add(Task(text='Сколько отрезков на этом чертеже?', answer='3', image='pic/100.jpg'))
lvl_1.add(Task(text='Чему равна длина самого большого отрезка?', answer='8', image='pic/100.jpg'))
lvl_1.add(Task(text='Начерти отрезок 10 см. Поставь точку так,'
                    ' чтобы получился отрезок 4 см. Какова длина второго отрезка?', answer='6', image='pic/100.jpg'))

lvl_2 = Level(1, info='Немного примеров!')
lvl_2.add(Task(text='12 - 8 + 9', answer='13'))
lvl_2.add(Task(text='17 - 8 + 6', answer='15'))
lvl_2.add(Task(text='48 - 40 - 8', answer='0'))
lvl_2.add(Task(text='0 + 88 - 8', answer='80'))

lvl_3 = Level(1, info='Ещё примеры!')
lvl_3.add(Task(text='60 - 50 + 3', answer='13'))
lvl_3.add(Task(text='11 - 8 + 7', answer='10'))
lvl_3.add(Task(text='100 - 60 + 3', answer='43'))
lvl_3.add(Task(text='30 + 20 + 3', answer='53'))

lvl_4 = Level(1, info='Составь задачу по картинке и реши ее!')
lvl_4.add(Task(answer='9', image='101.jpg'))
lvl_4.add(Task(answer='4', image='102.jpg'))
lvl_4.add(Task(text='Задача первая', answer='5', image='103.jpg'))
lvl_4.add(Task(text='А теперь вторая', answer='11', image='103.jpg'))

lvl_5 = Level(1, info='Сравнение!')
lvl_5.add(Task(text='38 мм ? 4 см', answer='<', choice=['>', '<', '=']))
lvl_5.add(Task(text='23 мм ? 2 см', answer='>', choice=['>', '<', '=']))
lvl_5.add(Task(text='1 см 8 мм ? 20 мм', answer='<', choice=['>', '<', '=']))
lvl_5.add(Task(text='1 дм 1 см ? 100 мм', answer='>', choice=['>', '<', '=']))

lvl_6 = Level(1, info='А теперь задачи на часы и минуты.')
lvl_6.add(
    Task(text='Первая игра заняла 50 минут, а вторая шла на 10 дольше. Сколько целых часов всего играли?', answer='1'))
lvl_6.add(Task(text='Мальчик делал домашнее задание час, а потом играл в игры 30 минут. Сколько всего минут прошло? ',
               answer='90'))

lvl_7 = Level(1, info='Поработаем с ломаными, готовь линейку, карандаш и циркуль!')
lvl_7.add(Task(answer='=', choice=['>', '<', '='], image='104.jpg'))
lvl_7.add(Task(text='Какая длина этой ломаной в сантиметрах?', answer='11', image='105.jpg'))
lvl_7.add(Task(text='А теперь найди её длину', answer='7', image='106.jpg'))

lvl_8 = Level(1, info='Ребусы!')
lvl_8.add(Task(text='? + 8 = 15', answer='7'))
lvl_8.add(Task(text='14 ... = 18', answer='+ 7', choice=['+ 7', '+ 6', '- 4']))
lvl_8.add(Task(text='19 ... = 10', answer='- 9'))
lvl_8.add(Task(text='0 ,,, = 10', answer='+ 10'))

lvl_9 = Level(1, info='Примеры!')
lvl_9.add(Task(text='40 - 21 + 11', answer='30'))
lvl_9.add(Task(text='11 + 10 - 4', answer='17'))
lvl_9.add(Task(text='80 - 40 + 11', answer='51'))
lvl_9.add(Task(text='23 - 13 + 0', answer='10'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60,
               topic='Числа   от   1   до   100. Сложение и вычитание.')
lvl_10.add(Task(text='80 + 12', answer='92'))
lvl_10.add(Task(text='Первая игра заняла 1 час, а вторая шла на 10 минут. Сколько минут шли ргы вместе?', answer='70'))
lvl_10.add(Task(text='? + 11 = 20', answer='9'))
lvl_10.add(Task(text='80 - ? = 30', answer='50'))
lvl_10.add(Task(text='1 дм 12 см ? 13 см 100 мм', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='64 - 62 + 4', answer='6'))

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
year_2.add_level(topic_2)

topic_3 = Topic('Порядок выполнения действий')
lvl_1 = Level(1, info='Привет! Прочитай записи и выполни действия')
lvl_1.add(Task(text='6 + (3 - 1)', answer='8'))
lvl_1.add(Task(text='(8 - 2) + 3', answer='9'))
lvl_1.add(Task(text='(6 + 3) - 1', answer='8'))
lvl_1.add(Task(text='13 - (1 + 3)', answer='9'))

lvl_2 = Level(1, info='Продолжаем!')
lvl_2.add(Task(text='Из числа 16 вычесть разность числе 9 и 7.', answer='14'))
lvl_2.add(Task(text='К числу 10 прибавить разность чисел 7 и 5.', answer='12'))
lvl_2.add(Task(text='Из числа 20 вычесть сумму 2 и 3', answer='15'))
lvl_2.add(Task(text='Из числа 14 вычесть разность чисел 5 и 2', answer='11'))

lvl_3 = Level(1, info='Найди значения выражений')
lvl_3.add(Task(text='18 - (4 + 6)', answer='8'))
lvl_3.add(Task(text='25 - (15 - 10)', answer='20'))
lvl_3.add(Task(text='30 + 6 + 1', answer='37'))
lvl_3.add(Task(text='15 - 7 + 3', answer='11'))

lvl_4 = Level(1, info='Немного задачек!')
lvl_4.add(Task(text='У Димы две монеты: 2 р. и 5 р. Он купил тетрадь за 3 р., сколько у него осталось?', answer='4'))
lvl_4.add(
    Task(text='Слава согнул проволоку в треугольник со сторонами 3, 5, 7 см. Какой длины была проволока?', answer='15'))
lvl_4.add(Task(text='А теперь у него вышли стороны 7, 9 и 2 см. Какой длины проволоку он использовал?', answer='18'))

lvl_5 = Level(1, info='Расшифруй! Чтобы прочитать шифр, замени каждое число суммой.')
lvl_5.add(Task(text='55, 51, 29', answer='кот', image='107.jpg'))
lvl_5.add(Task(text='21, 51, 27, 53', answer='сова', image='107.jpg'))
lvl_5.add(Task(text='27, 51, 25, 55', answer='волк', image='107.jpg'))

lvl_6 = Level(1, info='Используй свойства сложения. Устный счёт!')
lvl_6.add(Task(text='20 + 2 + 8 + 40', answer='70'))
lvl_6.add(Task(text='6 + 40 + 4 + 20', answer='70'))
lvl_6.add(Task(text='1 + 10 + 9 + 60', answer='80'))
lvl_6.add(Task(text='30 + 3 + 50 + 7', answer='90'))

lvl_7 = Level(1, info='Вычисли, проговаривая устно!')
lvl_7.add(Task(text='50 - 6', answer='44'))
lvl_7.add(Task(text='100 - 4', answer='96'))
lvl_7.add(Task(text='90 - 3', answer='87'))
lvl_7.add(Task(text='81 - 3', answer='78'))

lvl_8 = Level(1, info='Задачки!')
lvl_8.add(Task(text='Две девочки шли навстречу друг другу. Одна прошла 20 метров до встречи, а другая на 8 больше. '
                    'Какова длина дороги?', answer='48'))
lvl_8.add(Task(text='Таня пробежала 60 метров, а Катя на 4 меньше. Сколько метров пробежала Катя?', answer='54'))
lvl_8.add(Task(text='В нараже стояло 40 машин. 10 уехали перевозить арбузы, и еще 3 на перевозку овощей. '
                    'Сколько осталось в гараже?', answer='27'))

lvl_9 = Level(1, info='Определи по какому правилу построен ряд и найди пропущенный элемент.')
lvl_9.add(Task(text='12, 2, 13, 3, 14, ?, 15, 5', answer='4'))
lvl_9.add(Task(text='20, 2, 18, 3, 15, 1, ?', answer='14'))
lvl_9.add(Task(text='1, 3, 5, ?, 9', answer='7'))

lvl_10 = Level(1, info='Время теста!', style='test', time=60, topic='Порядок выполнения действий')
lvl_10.add(Task(text='(5 - 3) + 22 - (2 + 18) + 50', answer='54'))
lvl_10.add(Task(text='66 - (9 - 3) + 11', answer='71'))
lvl_10.add(Task(text='12 + 55 + 3 + 8 + 7 + 15', answer='100'))
lvl_10.add(Task(text='Последовательность: 65 ? 66 2 68 4 72', answer='1'))
lvl_10.add(Task(text='К числу 20 прибавить разность чисел 7 и 5.', answer='22'))
lvl_10.add(
    Task(text='Ваня согнул проволоку в треугольник со сторонами 6, 24, 4 см. Какой длины была проволока?', answer='34'))
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
year_2.add_level(topic_3)

topic_4 = Topic('Буквенные выражения')
lvl_1 = Level(1, info='Привет! Выражения, содержащие буквы, называются буквенными.')
lvl_1.add(Task(text='Найди значение выражения 8 + d. При d = 8', answer='16'))
lvl_1.add(Task(text='А теперь k - 8. При k = 21', answer='13'))
lvl_1.add(Task(text='(6 + 3) - 1', answer='8'))
lvl_1.add(Task(text='13 - (1 + 3)', answer='9'))

lvl_2 = Level(1, info='Вычисли значение выражения (a + 8) + (a - 8)')
lvl_2.add(Task(text='При а = 8', answer='16'))
lvl_2.add(Task(text='При а = 12', answer='24'))
lvl_2.add(Task(text='При а = 20', answer='40'))
lvl_2.add(Task(text='При а = 40', answer='80'))

lvl_3 = Level(1, info='Порешаем уравнения (равенства, содержащие неизвестные). Чему равен х?')
lvl_3.add(Task(text='4 + х = 12', answer='8'))
lvl_3.add(Task(text='10 - х = 5', answer='5'))
lvl_3.add(Task(text='11 - х + 4 = 15', answer='0'))
lvl_3.add(Task(text='х - 1 = 0', answer='1'))

lvl_4 = Level(1, info='Побери такое значение неизвестной, при которой равенство будет верно.')
lvl_4.add(Task(text='х + 3 = 13', answer='10'))
lvl_4.add(Task(text='18 = у + 5', answer='13'))
lvl_4.add(Task(text='14 = х + 7', answer='7'))
lvl_4.add(Task(text='63 = у + 10', answer='53'))

lvl_5 = Level(1, info='Сравни выражения.')
lvl_5.add(Task(text='3 + 67 ? 67 + 3', answer='=', choice=['>', '<', '=']))
lvl_5.add(Task(text='34 - (18 - 9) ? 34 - 8', answer='=', choice=['>', '<', '=']))
lvl_5.add(Task(text='75 - (14 - 6) ? 75 - 7', answer='<', choice=['>', '<', '=']))
lvl_5.add(Task(text='х + 3 ? 4 х + 10', answer='<', choice=['>', '<', '=']))

lvl_6 = Level(1, info='Ещё немного уравнений')
lvl_6.add(Task(text='30 - х = 6', answer='24'))
lvl_6.add(Task(text='89 - х = 80', answer='9'))
lvl_6.add(Task(text='7 + х = 100', answer='93'))
lvl_6.add(Task(text='30 + 3 + 50 + 7', answer='90'))

lvl_7 = Level(1, info='Проверь выражения и напиши Верно или Неверно')
lvl_7.add(Task(text='42 + 7 = 49', answer='Верно'))
lvl_7.add(Task(text='20 + 68 = 78', answer='Неверно'))
lvl_7.add(Task(text='36 + 23 = 59', answer='Верно'))
lvl_7.add(Task(text='76 + 21 = 87', answer='Неверно'))

lvl_8 = Level(1, info='Проверь выражения и напиши Верно или Неверно')
lvl_8.add(Task(text='69 - 50 = 19', answer='Верно'))
lvl_8.add(Task(text='100 - 8 = 92', answer='Верно'))
lvl_8.add(Task(text='74 - 30 = 54', answer='Неверно'))
lvl_8.add(Task(text='40 - 9 = 31', answer='Верно'))

lvl_9 = Level(1, info='Вычисли и выполни проверку')
lvl_9.add(Task(text='28 + 9', answer='37'))
lvl_9.add(Task(text='51 + 12', answer='63'))
lvl_9.add(Task(text='87 - 17', answer='70'))

lvl_10 = Level(1, info='Время теста!', style='test', time=60, topic='Буквенные выражения')
lvl_10.add(Task(text='89 - х = 72. х=?', answer='17'))
lvl_10.add(Task(text='76 + 15 = х. х=?', answer='91'))
lvl_10.add(Task(text='100 - х + (23 - х) + 2. При х = 20', answer='85'))
lvl_10.add(Task(text='Последовательность: 87 80 73 66 59 ?', answer='52'))
lvl_10.add(Task(text='Найди значение с + 7 + (с - 4) При с = 10', answer='23'))
lvl_10.add(Task(text='На одной тарелке 5 пирожков, а на второй 15. После обеда пирожков осталось 9. Сколько съели?',
                answer='11'))
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
year_2.add_level(topic_4)

topic_5 = Topic('Угол. Виды углов.')

lvl_1 = Level(1, info='Привет! Называй виды углов!')
lvl_1.add(Task(text='Какой это угол?', answer='Тупой', image='pic/108.jpg', choice=['Тупой', 'Прямой', 'Острый']))
lvl_1.add(Task(text='А этот угол?', answer='Прямой', image='pic/109.jpg', choice=['Тупой', 'Прямой', 'Острый']))
lvl_1.add(Task(text='Ну а этот?', answer='Острый', image='pic/110.jpg', choice=['Тупой', 'Прямой', 'Острый']))
lvl_1.add(Task(text='Сколько здесь тупых углов?', answer='2', image='pic/111.jpg'))

lvl_2 = Level(1, info='Привет! Рассмотрим фигуры.')
lvl_2.add(Task(text='Сколько углов у второй фигуры?', answer='4', image='pic/107.jpg'))
lvl_2.add(Task(text='Сколько на картинке прямых углов?', answer='4', image='pic/107.jpg'))
lvl_2.add(Task(text='Напиши сумму чисел, написанных на острых углах', answer='19', image='pic/107.jpg'))

lvl_3 = Level(1, info='А теперь рассмотрим чертёж.')
lvl_3.add(Task(text='Сколько острых углов на чертеже?', answer='2', image='pic/112.jpg'))
lvl_3.add(Task(text='А сколько прямых углов?', answer='5', image='pic/112.jpg'))
lvl_3.add(Task(text='Сколько же тогда тупых углов?', answer='1', image='pic/112.jpg'))

lvl_4 = Level(1, info='Немного примеров!')
lvl_4.add(Task(text='80 - (12 - 7)', answer='75'))
lvl_4.add(Task(text='90 - (14 - 8)', answer='84'))
lvl_4.add(Task(text='32 - 7', answer='25'))

lvl_5 = Level(1, info='Бонусное задание!')
lvl_5.add(Task(text='Продолжи ряд чисел: 1 3 7 13 21 ?', answer='31'))

lvl_6 = Level(1, info='А теперь рассмотрим картинку.')
lvl_6.add(Task(text='Фигура под номером 4 прямоугольник?', answer='Нет', image='pic/113.jpg', choice=['Да', 'Нет']))
lvl_6.add(Task(text='Прямоугольник это?', answer='Четырехугольник, у которого все угры прямые', image='pic/113.jpg',
               choice=['Четырехугольник, у которого все угры тупые', 'Четырехугольник', "Четырехугольник, у которого "
                                                                                        "все угры прямые"]))
lvl_6.add(Task(text='Сколько же тогда на картинке прямоугольников?', answer='3', image='pic/113.jpg'))

lvl_7 = Level(1, info='Немного уравнений')
lvl_7.add(Task(text='x - 9 = 4', answer='13'))
lvl_7.add(Task(text='35 - x = 30', answer='5'))
lvl_7.add(Task(text='y + 7 = 14', answer='7'))

lvl_8 = Level(1, info='Задача для любознательных!')
lvl_8.add(Task(text='Белка запасала орехи на зиму. В первый день она принесла 2 ореха, а в каждый последующий на 1 '
                    'больше. Сколько она запасла орехов за неделю?', answer='27'))
lvl_8.add(Task(text='А если бы она в первый день принесла три ореха?', answer='34'))

lvl_9 = Level(1, info='Найди правило, по которому в первом домике получено число 11 с использование остальных чисел'
                      ' и применяй его на остальных')
lvl_9.add(Task(text='Что напишем во второй домик?', answer='20', image='pic/114.jpg'))
lvl_9.add(Task(text='А в синий домик?', answer='16', image='pic/114.jpg'))
lvl_9.add(Task(text='Теперь в зелёный', answer='15', image='pic/114.jpg'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Угол. Виды углов. Логика.')
lvl_10.add(Task(text='(15 - 12) + (23 - 4)', answer='22'))
lvl_10.add(Task(text='Чей путь короче?', answer='Ёжика', image='pic/115.jpg', choice=['Зайчика', 'Мышки', 'Ёжика']))
lvl_10.add(Task(text='На полке было 12 книг. После того, как несколько взяли, осталось на 4 книги больше, чем забрали.'
                     ' Сколько книг взяли с полки?', answer='4'))
lvl_10.add(Task(text='Поменяй карточки с выражениями, имеющими одинаковые ответы, местами. Какое слово получилось?',
                answer='Гвоздика', image='pic/116.jpg'))
lvl_10.add(Task(text='70 - (15 - 15)', answer='70'))
lvl_10.add(Task(text='39 + 10 - 20 ? 30', answer='<', choice=['>', '<', '=']))
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
year_2.add_level(topic_5)

topic_6 = Topic('Квадрат.')

lvl_1 = Level(1, info='Привет! Немного задачек.')
lvl_1.add(Task(text='Какой периметр у прямоугольника, если длина одной стороны 4 см, а другой 5.', answer='18'))
lvl_1.add(Task(text='Длина комнаты 6 м, а её ширина 4 м. Какой должна быть длина полоски, наклеенной по верхнему краю '
                    'обоев?', answer='20'))

lvl_2 = Level(1, info='Что называют квадратом?.')
lvl_2.add(Task(text='Это квадрат?', answer='Нет', image='pic/117.jpg', choice=['Да', 'Нет']))
lvl_2.add(Task(text='А это квадрат?', answer='Нет', image='pic/118.jpg', choice=['Да', 'Нет']))
lvl_2.add(Task(text='Что насчёт этой фигуры, квадрат?', answer='Да', image='pic/119.jpg', choice=['Да', 'Нет']))
lvl_2.add(Task(text='Это квадрат?', answer='Нет', image='pic/120.jpg', choice=['Да', 'Нет']))

lvl_3 = Level(1, info='А теперь немного счёта!')
lvl_3.add(Task(text='Начерти квадрат со стороной 4 см. Какой у него периметр?', answer='16'))
lvl_3.add(Task(text='А если со стороной 7 см?', answer='28'))
lvl_3.add(Task(text='Самое сложное, со стороной 12 см.', answer='48'))

lvl_4 = Level(1, info='Реши уравнения!')
lvl_4.add(Task(text='75 - х = 75', answer='0'))
lvl_4.add(Task(text='4 + х = 84', answer='80'))
lvl_4.add(Task(text='89 - х = 0', answer='89'))

lvl_5 = Level(1, info='Вычислительная машина!')
lvl_5.add(Task(text='Какое число будет на выходе, если ввести 11?', answer='8', image='pic/121.jpg'))
lvl_5.add(Task(text='А если ввести 22?', answer='19', image='pic/121.jpg'))
lvl_5.add(Task(text='А что получится из 34?', answer='32', image='pic/121.jpg'))
lvl_5.add(Task(text='Какое число нужно ввести, чтобы получить 65?', answer='68', image='pic/121.jpg'))

lvl_6 = Level(1, info='Сравни выражения.')
lvl_6.add(Task(text='54 + 7 ? 54 + 5 + 1', answer='>', choice=['>', '<', '=']))
lvl_6.add(Task(text='63 + 8 ? 63 + 3 + 5', answer='=', choice=['>', '<', '=']))
lvl_6.add(Task(text='1 м ? 8 дм 6 см', answer='>', choice=['>', '<', '=']))
lvl_6.add(Task(text='46 + 0 ? 46 - 0', answer='=', choice=['>', '<', '=']))

lvl_7 = Level(1, info='Немного уравнений')
lvl_7.add(Task(text='x - 9 = 4', answer='13'))
lvl_7.add(Task(text='35 - x = 30', answer='5'))
lvl_7.add(Task(text='y + 7 = 14', answer='7'))

lvl_8 = Level(1, info='Сравни уравнения!')
lvl_8.add(Task(text='а + 1 ? а + 0', answer='>', choice=['>', '<', '=']))
lvl_8.add(Task(text='1 + b ? b + (89 - 88)', answer='=', choice=['>', '<', '=']))

lvl_9 = Level(1, info='Верно или нет?')
lvl_9.add(Task(text='Если число 47 увеличить на 30 получится 17', answer='Неверно', choice=['Верно', 'Неверно']))
lvl_9.add(Task(text='Разность чисел 32 и 8 равна 24', answer='Верно', choice=['Верно', 'Неверно']))
lvl_9.add(
    Task(text='Если вместо ? поставить 73 то будет верно ? - 4 = 68', answer='Неверно', choice=['Верно', 'Неверно']))
lvl_9.add(Task(text='Число 34 больше 9 на 25', answer='Верно', choice=['Верно', 'Неверно']))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Квадрат.')
lvl_10.add(Task(text='с + 12 ? с + 21', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='Какой у него периметр у квадрата со стороной 7 см?', answer='28'))
lvl_10.add(Task(text='Число 40 настолько же больше, чем 6, на сколько 35 больше 1', answer='Верно',
                choice=['Верно', 'Неверно']))
lvl_10.add(Task(text='1 м ? 9 дм 16 см', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='Реши уравнение 75 - x = 67', answer='8'))

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
year_2.add_level(topic_6)

topic_7 = Topic('Умножение.')

lvl_1 = Level(1, info='Привет! Немного логики, выбери знак!')
lvl_1.add(Task(text='10 ? 9 > 1', answer='+', choice=['+', '-']))
lvl_1.add(Task(text='10 ? 9 = 1', answer='-', choice=['+', '-']))
lvl_1.add(Task(text='28 ? 12 < 30', answer='-', choice=['+', '-']))
lvl_1.add(Task(text='28 ? 12 > 30', answer='+', choice=['+', '-']))

lvl_2 = Level(1, info='Рассмотри подсказки и ответь.')
lvl_2.add(Task(text='6 * 3 = ?', answer='18', image='pic/122.jpg'))
lvl_2.add(Task(text='4 * 2 = ?', answer='8', image='pic/123.jpg'))
lvl_2.add(Task(text='10 * 5 = ?', answer='50', image='pic/124.jpg'))
lvl_2.add(Task(text='5 * 4 = ?', answer='20', image='pic/125.jpg'))

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

lvl_9 = Level(1, info='Сколько раз содержится ...')
lvl_9.add(Task(text='Сколько раз 4 содержится в числе 8?', answer='2'))
lvl_9.add(Task(text='А 2 содержится в числе 8?', answer='4'))
lvl_9.add(Task(text='Сколько раз 4 содержится в числе 16?', answer='4'))
lvl_9.add(Task(text='Сколько раз 8 содержится в числе 16?', answer='2'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Умножение!')
lvl_10.add(Task(text='1 * 26', answer='26'))
lvl_10.add(Task(text='9 * 3', answer='27'))
lvl_10.add(Task(text='3 * 12', answer='36'))
lvl_10.add(Task(text='7 * 3 ? 6 * 4', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='2 * 14 ? 6 * 4', answer='>', choice=['>', '<', '=']))

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
year_2.add_level(topic_7)

topic_8 = Topic('Деление.')

lvl_1 = Level(1, info='Привет! Начнем с примеров!')
lvl_1.add(Task(text='8 * 3 + 16', answer='40'))
lvl_1.add(Task(text='3 * 3 - 5', answer='4'))
lvl_1.add(Task(text='21 - 4 * 5', answer='1'))

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

topic_9 = Topic('Порядок выполнения действий 2.')

lvl_1 = Level(1, info='Привет! Начнем с примеров!')
lvl_1.add(Task(text='30 + 6 * (13 - 9)', answer='54'))
lvl_1.add(Task(text='18 : 2 - 2 * 3 ', answer='4'))
lvl_1.add(Task(text='24 : (3 * 2)', answer='4'))

lvl_2 = Level(1, info='Ещё немного примеров!')
lvl_2.add(Task(text='43 - (20 - 7) + 15', answer='45'))
lvl_2.add(Task(text='21 : 7 * 9', answer='27'))
lvl_2.add(Task(text='60 : (4 + 6) * 3', answer='18'))

lvl_3 = Level(1, info='Бонусная задача на логику!')
lvl_3.add(Task(text='Масса одного котёнка и одного щенка вместе равна 8 кг. А трёх щенков и двух котят 22 кг. '
                    'Сколько весит щенок?', answer='6'))

lvl_4 = Level(1, info='Найди значение х в уравнениях.')
lvl_4.add(Task(text='х + х + х = 30', answer='10'))
lvl_4.add(Task(text='43 * х = 43 : х', answer='1'))
lvl_4.add(Task(text='х + 20 = 12 + 8', answer='0'))
lvl_4.add(Task(text='х - 18 = 23 - 23', answer='18'))

lvl_5 = Level(1, info='Проверь выражения и напиши Верно или Неверно')
lvl_5.add(Task(text='4 * 7 + 4 = 4 * 8', answer='Верно', choice=['Верно', "Неверно"]))
lvl_5.add(Task(text='27 : 3 < 10', answer='Верно', choice=['Верно', "Неверно"]))
lvl_5.add(Task(text='48 + (14 - 12) > 50', answer='Неверно', choice=['Верно', "Неверно"]))

lvl_6 = Level(1, info='Вопросы!')
lvl_6.add(Task(text='Во сколько раз 18 больше трех? Введи только число', answer='6'))
lvl_6.add(Task(text='Во сколько раз 4 меньше 16? Введи только число', answer='4'))
lvl_6.add(Task(text='А во сколько раз метр больше сантиметра? Введи только число', answer='100'))

lvl_7 = Level(1, info='Примеры!')
lvl_7.add(Task(text='(50 - 38) : 4', answer='3'))
lvl_7.add(Task(text='24 : 4', answer='6'))
lvl_7.add(Task(text='36 : 6', answer='6'))

lvl_8 = Level(1, info='Устные задачи')
lvl_8.add(Task(text='В куске 20 м. ткани. На каждый костюм необходимо 3 м, можно ли сшить 6 таких?', answer='Да',
               choice=['Да', 'Нет']))
lvl_8.add(Task(text='А 7 таких костюмов получится сшить?', answer='Нет', choice=['Да', 'Нет']))
lvl_8.add(Task(text='Найди длину стороны квадрата, если его периметр 24 см.', answer='6'))

lvl_9 = Level(1, info='Реши уравнения')
lvl_9.add(Task(text='х : 5 = 10', answer='50'))
lvl_9.add(Task(text='х : 7 - 6 = 0', answer='42'))
lvl_9.add(Task(text='у * 5 = 20', answer='4'))
lvl_9.add(Task(text='у * 6 + 2 = 38', answer='6'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Порядок действий 2!')
lvl_10.add(Task(text='32 + 8 * (13 - 9)', answer='64'))
lvl_10.add(Task(text='2 * х : 6 = 20', answer='60'))
lvl_10.add(Task(text='Во сколько раз 8 * 2 больше четырёх? Введи только число', answer='4'))
lvl_10.add(Task(text='45 : (9 + 6) * 3', answer='9'))
lvl_10.add(Task(text='48 : 2 + (14 - 12) * 6 > 36', answer='Неверно', choice=['Верно', "Неверно"]))

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
year_2.add_level(topic_9)

topic_10 = Topic('Площадь. Единицы площади.')

lvl_1 = Level(1, info='Привет! Начнем с примеров!')
lvl_1.add(Task(text='45 : (18 - 13)', answer='9'))
lvl_1.add(Task(text='(27 + 27) : 9', answer='6'))
lvl_1.add(Task(text='24 : (11 - 7)', answer='6'))

lvl_2 = Level(1, info='Расчёт площади!')
lvl_2.add(Task(text='Одна сторона прямоугольника 1 см, а другая 7 см. Какая у него площадь?'
                    ' Введи только число', answer='7'))
lvl_2.add(Task(text='Теперь одна сторона прямоугольника 3 см, а другая 2 см. Какая у него площадь?'
                    ' Введи только число', answer='6'))
lvl_2.add(Task(text='А если одна сторона прямоугольника 6 см, а другая 7 см. Какая у него площадь?'
                    ' Введи только число', answer='42'))

lvl_3 = Level(1, info='Найди число')
lvl_3.add(Task(text='Найди площадь сада по плану.', answer='45', image='pic/129.jpg'))
lvl_3.add(Task(text='А теперь дома', answer='49', image='pic/129.jpg'))

lvl_4 = Level(1, info='Примеры!')
lvl_4.add(Task(text='35 + 15 : 5 + 2', answer='40'))
lvl_4.add(Task(text='91 : 9 * 6', answer='54'))
lvl_4.add(Task(text='63 : 7 * 5', answer='45'))

lvl_5 = Level(1, info='Умножение на 1')
lvl_5.add(Task(text='1 * 12', answer='12'))
lvl_5.add(Task(text='(62 + 24) * 1', answer='86'))
lvl_5.add(Task(text='28 : 4 * 1', answer='7'))

lvl_6 = Level(1, info='Умножение на 0...')
lvl_6.add(Task(text='54 * 0', answer='0'))
lvl_6.add(Task(text='0 * 100', answer='0'))
lvl_6.add(Task(text='(24 + 21) * 0', answer='0'))

lvl_7 = Level(1, info='Деление нуля на число')
lvl_7.add(Task(text='0 : 3', answer='0'))
lvl_7.add(Task(text='0 : 24', answer='0'))
lvl_7.add(Task(text='100 - (6 * 9 + 64 : 8) : 2 * 3', answer='7'))

lvl_8 = Level(1, info='Устные задачи')
lvl_8.add(Task(text='В куске 70 м. ткани. На каждый костюм необходимо 10 м, можно ли сшить 7 таких?', answer='Да',
               choice=['Да', 'Нет']))
lvl_8.add(Task(text='А если удлинить костюмы то всё еще хватит?', answer='Нет', choice=['Да', 'Нет']))
lvl_8.add(Task(text='Найди длину стороны квадрата, если его периметр 24 см.', answer='6'))

lvl_9 = Level(1, info='Реши уравнения')
lvl_9.add(Task(text='х : 2 + 21 = 31', answer='5'))
lvl_9.add(Task(text='х * 7 - 6 = 1', answer='1'))
lvl_9.add(Task(text='у * 5 = 20', answer='4'))


lvl_10 = Level(1, info='Закрепим пройденное!', style='final_test', time=120, topic='Конец второго класса! Удачи.')
lvl_10.add(Task(text='Назови число, в котором 6 дес. 1 ед.', answer='61'))
lvl_10.add(Task(text='На столе лежат: помидор, кабачок и картошка. Сколькими '
                     'способами можно составить набор и двух овощей?', answer='6'))
lvl_10.add(Task(text='86, 85, ?, 83, 82', answer='84'))
lvl_10.add(Task(text='80 + 12', answer='92'))
lvl_10.add(Task(text='Первая игра заняла 1 час, а вторая шла на 10 минут. Сколько минут шли игры вместе?', answer='70'))
lvl_10.add(Task(text='1 дм 12 см ? 13 см 100 мм', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='64 - 62 + 4', answer='6'))
lvl_10.add(Task(text='(5 - 3) + 22 - (2 + 18) + 50', answer='54'))
lvl_10.add(Task(text='66 - (9 - 3) + 11', answer='71'))
lvl_10.add(Task(text='12 + 55 + 3 + 8 + 7 + 15', answer='100'))
lvl_10.add(Task(text='К числу 20 прибавить разность чисел 7 и 5.', answer='22'))
lvl_10.add(
    Task(text='Ваня согнул проволоку в треугольник со сторонами 6, 24, 4 см. Какой длины была проволока?', answer='34'))
lvl_10.add(Task(text='89 - х = 72. х=?', answer='17'))
lvl_10.add(Task(text='100 - х + (23 - х) + 2. При х = 20', answer='85'))
lvl_10.add(Task(text='Последовательность: 87 80 73 66 59 ?', answer='52'))
lvl_10.add(Task(text='Найди значение с + 7 + (с - 4) При с = 10', answer='23'))
lvl_10.add(Task(text='На одной тарелке 5 пирожков, а на второй 15. После обеда пирожков осталось 9. Сколько съели?',
                answer='11'))
lvl_10.add(Task(text='(15 - 12) + (23 - 4)', answer='22'))
lvl_10.add(Task(text='На полке было 12 книг. После того, как несколько взяли, осталось на 4 книги больше, чем забрали.'
                     ' Сколько книг взяли с полки?', answer='4'))
lvl_10.add(Task(text='39 + 10 - 20 ? 30', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='с + 12 ? с + 21', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='Какой у него периметр у квадрата со стороной 7 см?', answer='28'))
lvl_10.add(Task(text='1 м ? 9 дм 16 см', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='Реши уравнение 75 - x = 67', answer='8'))
lvl_10.add(Task(text='7 * 3 ? 6 * 4', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='2 * 14 ? 6 * 4', answer='>', choice=['>', '<', '=']))
lvl_10.add(Task(text='32 + 8 * (13 - 9)', answer='64'))
lvl_10.add(Task(text='Во сколько раз 8 * 2 больше четырёх? Введи только число', answer='4'))
lvl_10.add(Task(text='45 : (9 + 6) * 3', answer='9'))
lvl_10.add(Task(text='48 : 2 + (14 - 12) * 6 > 36', answer='Неверно', choice=['Верно', "Неверно"]))

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
year_2.add_level(topic_10)