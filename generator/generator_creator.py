class Task:
    def __init__(self, text='', choice=None, answer='', image=None):
        self.task, self.choice, self.answer, self.image = text, choice, answer, image

    def check_answer(self, answer):
        return self.answer == answer


class Topic:
    def __init__(self, name=''):
        self.levels = []  # Переносим определение списка сюда
        self.name = name

    def add(self, task):
        self.levels.append(task)


class Class:
    def __init__(self, num=1):
        self.topics = []  # Переносим определение списка сюда
        self.number = num

    def add_level(self, topic):
        self.topics.append(topic)