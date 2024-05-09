from random import randint


class Generator1:
    def __init__(self, class_num, topic):
        self.class_num, self.topic = class_num, topic

    # Счет предметов. Сравнение групп предметов. Пространственные и временные представления.
    def generate_item_count(self):
        count_items = randint(1, 10)
