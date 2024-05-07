class Task:
    def __init__(self, text='', choice=None, answer='', image=''):
        self.task, self.choice, self.answer, self.image = text, choice, answer, image

    def check_answer(self, answer):
        return self.answer == answer


class Level:
    tasks = []

    def __init__(self, num=0, topic='', style='base', time=0, class_num=0, info=''):
        if style == 'base':
            self.name = f'Уровень номер {num}. {info}'
        elif style == 'test':
            self.name = f'Тест на тему {topic}, даётся {time} минут, удачи!'
            self.text = 'Пройди этот тест для открытия следующего блока заданий! Проиграешь трижды и тема сбросится!'
        elif style == 'final_test':
            self.name = f'Контрольная работа за {class_num} класс, даётся {time} минут, удачи!'
            self.text = ('Ты шел(а) к этому очень долго! Пришло время закончить с этим классом, здесь встретятся задачи'
                         'на все темы этого года, попыток не ограниченное количество!')

    def add(self, task):
        self.tasks.append(task)


class Topic:
    levels = []

    def __init__(self, name=''):
        self.name = name

    def add_level(self, lvl):
        self.levels.append(lvl)


class Class:
    topics = []

    def __init__(self, num=1):
        self.number = num

    def add_level(self, topic):
        self.topics.append(topic)



