from generator.generator_creator import *
import random
from random import randint


def generate(year, topic):
    if year == 1:
        if topic == 'Счет предметов':
            i = randint(1, 9)
            c = randint(2, 10)
            if i == 1:
                y = randint(2, 10)
                img = ['y_apple.png'] * y
                return Task(text='Сколько здесь желтых яблок?', answer=str(y), image=img)
            if i == 2:
                y = randint(2, 10)
                img = ['y_apple.png'] * y
                return Task(text='Сколько здесь всего яблок?', answer=str(y), image=img)
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
                return Task(text='Сколько на картинке зонтиков?', answer=str(c), image=img)
            if i == 9:
                img = ['bread.png'] * c
                return Task(text='Сколько тут батонов?', answer=str(c), image=img)
        if topic == 'Многоугольники':
            i = randint(3, 10)
            img = f'{i}.png'
            return Task(text='Сколько углов у этой фигуры?', answer=str(i), image=[img])
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
                return Task(text=txt, answer=str(n - m))
            if typ == 2:
                txt = f'У Васи было {n} марок, он подарил папе {m}. Сколько теперь у мальчика марок?'
                return Task(text=txt, answer=str(n - m))
            if typ == 3:
                txt = f'У Даши было {n} кукол, она отдала сестре {m}. Сколько теперь у Даши кукол?'
                return Task(text=txt, answer=str(n - m))
            if typ == 4:
                txt = f'В саду росли {n} яблонь, в этом году засохли {m}. Сколько теперь яблонь в саду?'
                return Task(text=txt, answer=str(n - m))
            if typ == 5:
                txt = f'В сумке лежало {n} карандашей, для урока Коля достал {m}. Сколько теперь в сумке карандашей?'
                return Task(text=txt, answer=str(n - m))
            if typ == 6:
                txt = f'На столе лежало {n} яблок, Боря забрал {m}. Сколько теперь на столе яблок?'
                return Task(text=txt, answer=str(n - m))
        if topic == 'Задачки (разнобой)':
            n, m = randint(4, 7), randint(1, 3)
            typ = randint(1, 12)
            if typ == 1:
                txt = f'У бабушки было {n} пирожков, Вася съел {m}. Сколько теперь у нее пирожков?'
                return Task(text=txt, answer=str(n - m))
            if typ == 2:
                txt = f'У Васи было {n} марок, он подарил папе {m}. Сколько теперь у мальчика марок?'
                return Task(text=txt, answer=str(n + m))
            if typ == 3:
                txt = f'У Даши было {n} кукол, она отдала сестре {m}. Сколько теперь у Даши кукол?'
                return Task(text=txt, answer=str(n - m))
            if typ == 4:
                txt = f'В саду росли {n} яблонь, в этом году засохли {m}. Сколько теперь яблонь в саду?'
                return Task(text=txt, answer=str(n - m))
            if typ == 5:
                txt = f'В сумке лежало {n} карандашей, для урока Коля достал {m}. Сколько теперь в сумке карандашей?'
                return Task(text=txt, answer=str(n - m))
            if typ == 6:
                txt = f'На столе лежало {n} яблок, Боря забрал {m}. Сколько теперь на столе яблок?'
                return Task(text=txt, answer=str(n - m))
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
            typ = randint(1, 2)
            if typ == 1:
                n, m = randint(0, 5), randint(0, 5)
                txt = f'{n} + {m}'
                return Task(text=txt, answer=str(n + m))
            if typ == 2:
                n, m = randint(4, 7), randint(0, 3)
                txt = f'{n} - {m}'
                return Task(text=txt, answer=str(n - m))
    if year == 2:
        if topic == 'Числа от 1 до 20':
            i = randint(2, 18)
            typ = randint(1, 4)
            if typ == 1:
                return Task(text=f'Назови число, которое встречается при счете между {i} и {i + 2}', answer=str(i + 1))
            if typ == 2:
                return Task(text=f'Назови число, которое встречается при счете между {i + 2} и {i}', answer=str(i + 1))
            i_1 = randint(7, 13)
            i_2 = randint(2, 7)
            if typ == 3:
                return Task(text=f'Увеличь на {i_2} число {i_1}, напиши ответ.', answer=str(i_1 + i_2))
            if typ == 4:
                return Task(text=f'Уменьши на {i_2} число {i_1}, напиши ответ.', answer=str(i_1 - i_2))
        if topic == 'Счет десятками':
            i_1 = randint(0, 9)
            i_2 = randint(0, 9)
            return Task(text=f'Назови число, в котором {i_1} десятков и {i_2} единиц', answer=str(i_1 * 10 + i_2))
        if topic == 'Сложение и вычитание (Числа от 1 до 100)':
            typ = randint(1, 6)
            if typ == 1:
                i_1, i_2, i_3 = randint(40, 100), randint(20, 40), randint(1, 20)
                return Task(text=f'{i_1} - {i_2} + {i_3}', answer=str(eval(f'{i_1} - {i_2} + {i_3}')))
            if typ == 2:
                i_1, i_2, i_3 = randint(1, 30), randint(1, 30), randint(1, 40)
                return Task(text=f'{i_1} + {i_2} + {i_3}', answer=str(eval(f'{i_1} + {i_2} + {i_3}')))
            if typ == 3:
                i_1, i_2, i_3 = randint(40, 80), randint(1, 20), randint(1, 20)
                return Task(text=f'{i_1} - {i_2} - {i_3}', answer=str(eval(f'{i_1} - {i_2} - {i_3}')))
            if typ == 4:
                i_1, i_2, i_3 = randint(20, 40), randint(20, 60), randint(10, 40)
                return Task(text=f'{i_1} + {i_2} - {i_3}', answer=str(eval(f'{i_1} + {i_2} - {i_3}')))
        if topic == 'Уравнения':
            typ = randint(1, 5)
            if typ == 1:
                x = randint(10, 60)
                i = randint(1, 20)
                return Task(text=f'x + {i} = {x + i}', answer=str(x))
            if typ == 2:
                x = randint(20, 60)
                i = randint(1, 20)
                return Task(text=f'x - {i} = {x - i}', answer=str(x))
            if typ == 3:
                x = randint(10, 60)
                i_1 = randint(1, 20)
                i_2 = randint(1, 20)
                return Task(text=f'x + {i_1} - {i_2} = {x + i_1 - i_2}', answer=str(x))
            if typ == 4:
                x = randint(10, 60)
                i = randint(1, 20)
                return Task(text=f'{i} + x = {x + i}', answer=str(x))
            if typ == 5:
                x = randint(10, 30)
                i = randint(30, 60)
                return Task(text=f'{i} - x = {i - x}', answer=str(x))
        if topic == 'Деление и умножение (Начальные)':
            typ = randint(1, 6)
            if typ == 1:
                i_1 = random.choice([2, 4, 6, 8, 10])
                return Task(text=f'{i_1} : 2', answer=str(i_1 // 2))
            if typ == 2:
                i_1 = random.choice([3, 6, 9, 12])
                return Task(text=f'{i_1} : 3', answer=str(i_1 // 3))
            if typ == 3:
                i_1 = randint(1, 20)
                return Task(text=f'{i_1} : 1', answer=str(i_1))
            if typ == 4:
                i_1 = random.choice([4, 8, 12, 16])
                return Task(text=f'{i_1} : 4', answer=str(i_1 // 4))
            if typ == 5:
                i_1 = random.choice([5, 10, 15])
                return Task(text=f'{i_1} : 5', answer=str(i_1 // 5))
            if typ == 6:
                i_1, i_2 = randint(1, 10), randint(0, 5)
                return Task(text=f'{i_1} * {i_2}', answer=str(i_1 * i_2))
        if topic == 'Примеры':
            typ = randint(1, 10)
            i_1, i_2, i_3, i_4 = randint(40, 80), randint(10, 20), randint(30, 40), randint(20, 30)
            if typ == 1:
                return Task(text=f'{i_1} - ({i_3} - {i_2}) + {i_4}',
                            answer=str(eval(f'{i_1} - ({i_3} - {i_2}) + {i_4}')))
            if typ == 2:
                i_1, i_2, i_3, i_4 = randint(3, 10), randint(3, 10), randint(2, 10), randint(2, 7)
                return Task(text=f'{i_4 * (i_1 + i_3)} : ({i_1} + {i_3}) * {i_2}', answer=str(i_4 * i_2))
            if typ == 3:
                i_1, i_2, i_3, i_4 = randint(10, 20), randint(3, 10), randint(2, 10), randint(2, 7)
                i_5 = randint(2, 6)
                return Task(text=f'{i_4 * i_5} : {i_5} + ({i_1} - {i_2}) * {i_3}',
                            answer=str(eval(f'{i_4 * i_5} // {i_5} + ({i_1} - {i_2}) * {i_3}')))
            if typ == 4:
                return Task(text=f'({i_2} + {i_3}) * 0', answer='0')
            if typ == 5:
                i_2 = randint(1, 10)
                return Task(text=f'{i_3} + {i_2} * ({i_4} - {i_2})',
                            answer=str(eval(f'{i_3} + {i_2} * ({i_4} - {i_2})')))
            if typ == 6:
                return Task(text=f'{i_1} + {i_2} - ({i_3} - {i_4})',
                            answer=str(eval(f'{i_1} + {i_2} - ({i_3} - {i_4})')))
            if typ == 7:
                return Task(text=f'({i_1} + {i_2}) - ({i_3} - {i_4})',
                            answer=str(eval(f'({i_1} + {i_2}) - ({i_3} - {i_4})')))
            if typ == 8:
                return Task(text=f'{i_1} - {i_2} - ({i_3} - {i_4})',
                            answer=str(eval(f'{i_1} - {i_2} - ({i_3} - {i_4})')))
            if typ == 9:
                return Task(text=f'{i_1} - {i_2} * ({i_3} - {i_4})',
                            answer=str(eval(f'{i_1} - {i_2} * ({i_3} - {i_4})')))
            if typ == 10:
                return Task(text=f'({i_1} - {i_2} - {i_3} + {i_4}) : 1',
                            answer=str(eval(f'({i_1} - {i_2} - {i_3} + {i_4})')))
    if year == 3:
        if topic == 'Сложение (Трехзначные числа)':
            i_1 = randint(100, 790)
            i_2 = random.choice([r for r in range(100, 999 - i_1)])
            return Task(text=f'{i_1} + {i_2}', answer=str(i_1 + i_2))
        if topic == 'Вычитание (Трехзначные числа)':
            i_1 = randint(300, 999)
            i_2 = random.choice([r for r in range(100, i_1)])
            return Task(text=f'{i_1} - {i_2}', answer=str(i_1 - i_2))
        if topic == 'Деление (Среднее)':
            typ = randint(1, 5)
            if typ == 1:
                i = randint(0, 5) * 2 * 10
                return Task(text=f'{i} : 20', answer=str(i // 20))
            if typ == 2:
                i = randint(0, 3) * 3 * 10
                return Task(text=f'{i} : 30', answer=str(i // 30))
            if typ == 3:
                i = randint(0, 10) * 10
                return Task(text=f'{i} : 10', answer=str(i // 10))
            if typ == 4:
                i_1 = randint(1, 10)
                i_2 = randint(1, 10)
                return Task(text=f'{i_1 * i_2} : {i_1}', answer=str(i_2))
            if typ == 5:
                i_1 = randint(1, 10)
                i_2 = randint(1, 10)
                return Task(text=f'{i_1 * i_2} : x = {i_2}', answer=str(i_1))
        if topic == 'Умножение (Среднее)':
            typ = randint(1, 4)
            if typ == 1:
                i_1 = randint(10, 30)
                i_2 = randint(0, 10)
                return Task(text=f'{i_1} * {i_2}', answer=str(i_1 * i_2))
            if typ == 2:
                i_1 = randint(0, 10)
                i_2 = randint(0, 10)
                return Task(text=f'{i_1} * {i_2}', answer=str(i_1 * i_2))
            if typ == 3:
                i_1 = randint(20, 30)
                i_2 = randint(1, 5)
                return Task(text=f'{i_1} * {i_2}', answer=str(i_1 * i_2))
            if typ == 4:
                i_1 = randint(10, 25)
                i_2 = randint(1, 10)
                return Task(text=f'{i_1} * x = {i_1 * i_2}', answer=str(i_2))
        if topic == 'Деление (Трехзначные числа)':
            i_1 = randint(2, 10)
            i_2 = random.choice([r for r in range(100, 999) if r % i_1 == 0])
            return Task(text=f'{i_2} : {i_1}', answer=str(i_2 // i_1))
        if topic == 'Примеры (Трехзначные числа)':
            typ = randint(1, 5)
            if typ == 1:
                i_3 = randint(2, 10)
                i_5 = random.choice([r for r in range(300, 999) if r % i_3 == 0])
                i_1 = random.choice([r for r in range(200, i_5)])
                i_2 = i_5 - i_1
                i_4 = randint(2, 15)
                return Task(text=f'({i_1} + {i_2}) : {i_3} * {i_4}',
                            answer=str(eval(f'({i_1} + {i_2}) // {i_3} * {i_4}')))
            if typ == 2:
                i_2 = randint(2, 10)
                i_1 = random.choice([r for r in range(100, 400) if r % i_2 == 0])
                i_3 = randint(5, 25)
                i_4 = randint(15, 30)
                return Task(text=f'{i_1} : {i_2} + {i_3} * {i_4}', answer=str(eval(f'{i_1} // {i_2} + {i_3} * {i_4}')))
            if typ == 3:
                i_3 = randint(2, 900)
                i_4 = i_3 + randint(2, 10)
                i_2 = random.choice([r for r in range(300, 999) if r % (i_4 - i_3) == 0])
                i_1 = randint(2, 20)
                return Task(text=f'{i_1} * ({i_2} : ({i_4} - {i_3}))',
                            answer=str(eval(f'{i_1} * ({i_2} // ({i_4} - {i_3}))')))
            if typ == 4:
                i_3 = randint(2, 10)
                i_2 = random.choice([r for r in range(300, 900) if r % i_3 == 0])
                i_1 = randint(100, 300)
                i_4 = randint(100, 300)
                return Task(text=f'{i_1} + {i_2} : {i_3} - {i_4}', answer=str(eval(f'{i_1} + {i_2} // {i_3} - {i_4}')))
            if typ == 5:
                i_3 = randint(2, 10)
                i_5 = random.choice([r for r in range(300, 999) if r % i_3 == 0])
                i_1 = random.choice([r for r in range(200, i_5)])
                i_2 = i_5 - i_1
                i_4 = randint(2, 15)
                return Task(text=f'({i_1} - {i_2}) * {i_3} : {i_4}',
                            answer=str(eval(f'({i_1} + {i_2}) // {i_3} * {i_4}')))
    if year == 4:
        if topic == 'Сложение (Три слагаемых)':
            i_1 = randint(100, 700)
            i_2 = random.choice([r for r in range(100, 800 - i_1)])
            i_3 = randint(100, 1000 - i_1 - i_2)
            return Task(text=f'{i_1} + {i_2} + {i_3}', answer=str(i_1 + i_2 + i_3))
        if topic == 'Сложение (Числа больше 1000)':
            typ = randint(1, 3)
            if typ == 1:
                i_1 = randint(100, 900) * 1000
                i_2 = randint(100, 900)
                return Task(text=f'{i_1} + {i_2}', answer=str(i_1 + i_2))
            if typ == 2:
                i_1 = randint(100, 900) * 1000
                i_2 = randint(100, 900)
                i_3 = randint(100, 1000 - i_2)
                return Task(text=f'{i_1} + ({i_2} + {i_3})', answer=str(i_1 + i_2 + i_3))
            if typ == 3:
                i_1 = randint(100, 900) * 1000
                i_2 = randint(100, 900)
                i_3 = randint(1, 99)
                return Task(text=f'{i_1} + {i_2} + {i_3}', answer=str(i_1 + i_2 + i_3))
        if topic == 'Умножение (На произведение)':
            i_1 = randint(4, 10)
            i_2 = randint(4, 10)
            i_3 = randint(4, 20)
            typ = randint(1, 2)
            if typ == 1:
                return Task(text=f'{i_1} * ({i_2} * {i_3})', answer=str(i_1 * i_2 * i_3))
            if typ == 2:
                return Task(text=f'({i_1} * {i_2}) * {i_3}', answer=str(i_1 * i_2 * i_3))
            if typ == 3:
                i_2 = randint(100, 999)
                return Task(text=f'{i_2} * {i_1 * 10}', answer=str(i_1 * i_2 * 10))
        if topic == 'Умножение (Продвинутое)':
            typ = randint(1, 4)
            if typ == 1:
                i_1 = randint(200, 999)
                i_2 = randint(20, 99)
                return Task(text=f'{i_1} * {i_2}', answer=str(i_1 * i_2))
            if typ == 2:
                i_1 = randint(300, 999)
                i_2 = randint(100, 600)
                return Task(text=f'{i_1} * {i_2}', answer=str(i_1 * i_2))
            if typ == 3:
                i_1 = randint(400, 999)
                i_2 = randint(300, 999)
                return Task(text=f'{i_1} * {i_2}', answer=str(i_1 * i_2))
            if typ == 4:
                i_1 = randint(300, 900)
                i_2 = randint(300, 900)
                return Task(text=f'{i_1} * x = {i_1 * i_2}', answer=str(i_2))
        if topic == 'Деление (На двузначные)':
            typ = randint(1, 4)
            if typ == 1:
                i_1 = randint(20, 99)
                i_2 = randint(600, 99999)
                return Task(text=f'Напиши целую часть деления {i_2} : {i_1}', answer=str(i_2 // i_1))
            if typ == 2:
                i_1 = randint(20, 99)
                i_2 = randint(600, 99999)
                return Task(text=f'Напиши остаток от деления {i_2} : {i_1}', answer=str(i_2 % i_1))
            if typ == 3:
                i_1 = randint(20, 99) * 10
                i_2 = randint(600, 9999) * 100
                return Task(text=f'Напиши целую часть от деления {i_2} : {i_1}', answer=str(i_2 // i_1))
            if typ == 4:
                i_1 = randint(20, 99) * 10
                i_2 = randint(600, 9999) * 100
                return Task(text=f'Напиши остаток от деления {i_2} : {i_1}', answer=str(i_2 % i_1))
        if topic == 'Деление (Продвинутое)':
            typ = randint(1, 4)
            if typ == 1:
                i_1 = randint(100, 999)
                i_2 = randint(999, 999999)
                return Task(text=f'Напиши целую часть деления {i_2} : {i_1}', answer=str(i_2 // i_1))
            if typ == 2:
                i_1 = randint(100, 999)
                i_2 = randint(600, 999999)
                return Task(text=f'Напиши остаток от деления {i_2} : {i_1}', answer=str(i_2 % i_1))
            if typ == 3:
                i_1 = randint(200, 999) * 10
                i_2 = randint(600, 99999) * 100
                return Task(text=f'Напиши целую часть от деления {i_2} : {i_1}', answer=str(i_2 // i_1))
            if typ == 4:
                i_1 = randint(200, 999) * 10
                i_2 = randint(600, 99999) * 100
                return Task(text=f'Напиши остаток от деления {i_2} : {i_1}', answer=str(i_2 % i_1))
