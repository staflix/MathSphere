from trainer import Task
from app.data.tools import dictionary_trainer


class Generator1:
    def __init__(self, class_num, topic):
        self.class_num = class_num
        self.topic = topic

    def generate_item_count_etc(self, dictionary_trainer, num_add, task):
        # Проверяем, существует ли уже словарь для данного класса
        if "Class" not in dictionary_trainer:
            dictionary_trainer["Class"] = {}

        class_dict = dictionary_trainer["Class"]

        # Проверяем, существует ли уже словарь для данного номера класса
        if self.class_num not in class_dict:
            class_dict[self.class_num] = {}

        num_class_dict = class_dict[self.class_num]

        # Проверяем, существует ли уже список задач для данной темы
        if self.topic not in num_class_dict:
            num_class_dict[self.topic] = []

        topic_tasks = num_class_dict[self.topic]

        for i in range(1, num_add):
            text = task.task
            image = task.image
            answer = i

            # Добавляем задачу в список задач для текущей темы
            topic_tasks.append({
                "text": text,
                "image": image,
                "answer": answer,
                "count_images": answer
            })


# Создаем экземпляр генератора
generator = Generator1(1, 'Счет предметов. Сравнение групп предметов. Пространственные и временные представления.')

# Добавляем задачи и сохраняем обновленный словарь
generator.generate_item_count_etc(dictionary_trainer, 11,
                                  Task(text='А сколько здесь всего яблок?',
                                       image='img_trainer/item_count_etc/apple.jpg'))

# Выводим обновленный словарь
print(dictionary_trainer)
