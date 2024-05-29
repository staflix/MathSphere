from generator_creator import *
import random
from random import randint


def generate(year, topic):
    if year == 1:
        if topic == 'Счет предметов':
            i = randint(1, 10)
            c = randint(2, 10)
            if i == 1:
                y = randint(2, 10)
                g = randint(2, 10)
                img = ['y_apple.png'] * y
                img.extend(['g_apple.png'] * g)
                return Task(text='Сколько здесь желтых яблок?', answer=str(y), image=img)
            if i == 2:
                y = randint(2, 10)
                g = randint(2, 10)
                img = ['y_apple.png'] * y
                img.extend(['g_apple.png'] * g)
                return Task(text='Сколько здесь всего яблок?', answer=str(y + g), image=img)
            if i == 3:
                img = ['mushroom.png'] * c
                return Task(text='Сколько здесь грибов?', answer=str(c), image=img)
            if i == 4:
                img = ['girl.png'] * c
                return Task(text='Сколько здесь девочек?', answer=str(c), image=img)
            if i == 5:
                img = ['bee.png'] * c
                return Task(text='Сколько здесь пчелок?', answer=str(c), image=img)
            if i == 6:
                img = ['bee.png'] * c
                return Task(text='Сколько же у них всего крыльев?', answer=str(c * 2), image=img)
            if i == 7:
                img = ['flower.png'] * c
                return Task(text='Сколько на этой картинке цветов?', answer=str(c), image=img)
            if i == 8:
                img = ['umbrella.png'] * c
                img.extend(['bread.png'] * randint(2, 10))
                return Task(text='Сколько на картинке зонтиков?', answer=str(c), image=img)
            if i == 9:
                img = ['bread.png'] * c
                img.extend(['umbrella.png'] * randint(2, 10))
                img.extend(['bee.png'] * randint(2, 10))
                return Task(text='Сколько тут батонов?', answer=str(c), image=img)
            if i == 10:
                img = ['snow.png'] * c
                img.extend(['pencil.png'] * (c - 1))
                return Task(text='Чего больше: карандашей или снежинок?', choice=['Снежинок', 'Карандашей', 'Поровну'],
                            answer='Снежинок', image=img)
        if topic == 'Многоугольники':
            typ = randint(1, 2)
            if typ == 1:
                i = randint(3, 10)
                img = f'{i}.png'
                return Task(text='Сколько углов у этой фигуры?', answer=str(i), image=[img])
            else:
                i_1 = randint(3, 10)
                i_2 = randint(3, 10)
                i_3 = randint(3, 10)
                c_1 = randint(2, 4)
                c_2 = randint(2, 4)
                c_3 = randint(2, 4)
                img = [f'{i_1}.png'] * c_1
                img.extend([f'{i_2}.png'] * c_2)
                img.extend([f'{i_3}.png'] * c_3)
                return Task(text=f'Сколько сколько здесь {i_1}-угольников?', answer=str(c_1), image=[img])
        if topic == 'Задачки на увеличение':
            typ = randint(1, 6)
            if typ == 1:
                n, m = randint(1, 4), randint(1, 3)
                txt = f'У бабушки было {n} пирожков, она испекла еще {m}. Сколько теперь у нее пирожков?'
                return Task(text=txt, answer=str(n + m))
            if typ == 2:
                n, m = randint(1, 4), randint(1, 3)
                txt = f'У Васи было {n} марок, папа подарил ему еще {m}. Сколько теперь у мальчика марок?'
                return Task(text=txt, answer=str(n + m))
            if typ == 3:
                n, m = randint(1, 4), randint(1, 3)
                txt = f'У Даши было {n} кукол, мама подарила ей {m} новых. Сколько теперь у нее кукол?'
                return Task(text=txt, answer=str(n + m))
            if typ == 4:
                n, m = randint(1, 4), randint(1, 3)
                txt = f'В саду росли {n} яблонь, в этом году посадили еще {m}. Сколько теперь яблонь в саду?'
                return Task(text=txt, answer=str(n + m))
            if typ == 5:
                n, m = randint(1, 6), randint(1, 3)
                txt = f'В сумке лежало {n} карандашей, положили еще {m}. Сколько теперь там карандашей?'
                return Task(text=txt, answer=str(n + m))
            if typ == 6:
                n, m = randint(1, 7), randint(1, 3)
                txt = f'На столе лежало {n} яблок, Вика положила еще {m}. Сколько теперь на столе яблок?'
                return Task(text=txt, answer=str(n + m))
        if topic == 'Задачки на уменьшение':
            n, m = randint(4, 7), randint(1, 3)
            typ = randint(1, 6)
            if typ == 1:
                txt = f'У бабушки было {n} пирожков, Вася съел {m}. Сколько теперь у нее пирожков?'
                return Task(text=txt, answer=str(n + m))
            if typ == 2:
                txt = f'У Васи было {n} марок, он подарил папе {m}. Сколько теперь у мальчика марок?'
                return Task(text=txt, answer=str(n + m))
            if typ == 3:
                txt = f'У Даши было {n} кукол, она отдала сестре {m}. Сколько теперь у Даши кукол?'
                return Task(text=txt, answer=str(n + m))
            if typ == 4:
                txt = f'В саду росли {n} яблонь, в этом году засохли {m}. Сколько теперь яблонь в саду?'
                return Task(text=txt, answer=str(n + m))
            if typ == 5:
                txt = f'В сумке лежало {n} карандашей, для урока Коля достал {m}. Сколько теперь в сумке карандашей?'
                return Task(text=txt, answer=str(n + m))
            if typ == 6:
                txt = f'На столе лежало {n} яблок, Боря забрал {m}. Сколько теперь на столе яблок?'
                return Task(text=txt, answer=str(n + m))
        if topic == 'Задачки (разнобой)':
            n, m = randint(4, 7), randint(1, 3)
            typ = randint(1, 12)
            if typ == 1:
                txt = f'У бабушки было {n} пирожков, Вася съел {m}. Сколько теперь у нее пирожков?'
                return Task(text=txt, answer=str(n + m))
            if typ == 2:
                txt = f'У Васи было {n} марок, он подарил папе {m}. Сколько теперь у мальчика марок?'
                return Task(text=txt, answer=str(n + m))
            if typ == 3:
                txt = f'У Даши было {n} кукол, она отдала сестре {m}. Сколько теперь у Даши кукол?'
                return Task(text=txt, answer=str(n + m))
            if typ == 4:
                txt = f'В саду росли {n} яблонь, в этом году засохли {m}. Сколько теперь яблонь в саду?'
                return Task(text=txt, answer=str(n + m))
            if typ == 5:
                txt = f'В сумке лежало {n} карандашей, для урока Коля достал {m}. Сколько теперь в сумке карандашей?'
                return Task(text=txt, answer=str(n + m))
            if typ == 6:
                txt = f'На столе лежало {n} яблок, Боря забрал {m}. Сколько теперь на столе яблок?'
                return Task(text=txt, answer=str(n + m))
            if typ == 7:
                txt = f'У бабушки было {n} пирожков, она испекла еще {m}. Сколько теперь у нее пирожков?'
                return Task(text=txt, answer=str(n + m))
            if typ == 8:
                txt = f'У Васи было {n} марок, папа подарил ему еще {m}. Сколько теперь у мальчика марок?'
                return Task(text=txt, answer=str(n + m))
            if typ == 9:
                txt = f'У Даши было {n} кукол, мама подарила ей {m} новых. Сколько теперь у нее кукол?'
                return Task(text=txt, answer=str(n + m))
            if typ == 10:
                txt = f'В саду росли {n} яблонь, в этом году посадили еще {m}. Сколько теперь яблонь в саду?'
                return Task(text=txt, answer=str(n + m))
            if typ == 11:
                txt = f'В сумке лежало {n} карандашей, положили еще {m}. Сколько теперь там карандашей?'
                return Task(text=txt, answer=str(n + m))
            if typ == 12:
                txt = f'На столе лежало {n} яблок, Вика положила еще {m}. Сколько теперь на столе яблок?'
                return Task(text=txt, answer=str(n + m))
        if topic == 'Примеры на счет':
            typ = randint(1, 12)
            if typ == 1:
                n, m = randint(0, 5), randint(0, 5)
                txt = f'{n} + {m}'
                return Task(text=txt, answer=str(n + m))
            if typ == 2:
                n, m = randint(4, 7), randint(0, 3)
                txt = f'{n} - {m}'
                return Task(text=txt, answer=str(n + m))
