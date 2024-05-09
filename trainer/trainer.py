class Task:
    def __init__(self, text='', choice=None, answer='', image=''):
        self.task, self.choice, self.answer, self.image = text, choice, answer, image

    def check_answer(self, answer):
        return self.answer == answer


