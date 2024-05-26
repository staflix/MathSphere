from generator_creator import *
import random


def generate(year, topic):
    if year == 1:
        if topic == 'Счет предметов':
            i = random.randint(1, 10)
            c = random.randint(2, 10)
            if i == 1:
                y = random.randint(2, 10)
                g = random.randint(2, 10)
                img = ['y_apple.png'] * y
                img.extend(['g_apple.png'] * g)
                return Task(text='Сколько здесь желтых яблок?', answer=str(y), image=img)
            if i == 2:
                y = random.randint(2, 10)
                g = random.randint(2, 10)
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
                img.extend(['bread.png'] * random.randint(2, 10))
                return Task(text='Сколько на картинке зонтиков?', answer=str(c), image=img)
            if i == 9:
                img = ['bread.png'] * c
                img.extend(['umbrella.png'] * random.randint(2, 10))
                img.extend(['bee.png'] * random.randint(2, 10))
                return Task(text='Сколько тут батонов?', answer=str(c), image=img)
            if i == 10:
                img = ['snow.png'] * c
                img.extend(['pencil.png'] * (c - 1))
                return Task(text='Чего больше: карандашей или снежинок?', choice=['Снежинок', 'Карандашей', 'Поровну'], answer='Снежинок', image=img)


