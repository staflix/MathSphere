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
topic_4.add_level(lvl_1)
topic_4.add_level(lvl_2)
topic_4.add_level(lvl_3)
topic_4.add_level(lvl_4)
topic_4.add_level(lvl_10)
year_3.add_level(topic_4)


