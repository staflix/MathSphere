# 1 класс
from company.company_creator import *


year_1 = Class(1)

topic_1 = Topic('Счет предметов. Сравнение групп предметов. Пространственные и временные представления.')

lvl_1 = Level(1, info='Привет! Посчитай количество предметов на картинке и ответь на вопрос.')
lvl_1.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_1.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))
lvl_1.add(Task(text='Сколько же здесь грибов?', answer='8', image='pic/2.jpg'))
lvl_1.add(Task(text='А здесь сколько девочек?', answer='4', image='pic/3.jpg'))

lvl_2 = Level(1, info='Ты отлично справляешься! Смотри какие красивые пчелы!')
lvl_2.add(Task(text='Сколько здесь пчелок?', answer='6', image='pic/4.jpg'))
lvl_2.add(Task(text='А сколько у одной пчелки крылышек?', answer='2', image='pic/4.jpg'))
lvl_2.add(Task(text='Сколько же у них всего крыльев?', answer='12', image='pic/4.jpg'))
lvl_2.add(Task(text='А сколько на этой картинке цветов?', answer='3', image='pic/4.jpg'))

lvl_3 = Level(1, info='Быстро ты! Давай сравнивать группы.')
lvl_3.add(Task(text='Где предметов больше: слева и справа?', choice=['Слева', 'Справа'], answer='Слева', image='pic/5.jpg'))
lvl_3.add(Task(text='Каких мишек больше?', choice=['Бурых', 'Белых'], answer='Бурых', image='pic/6.jpg'))
lvl_3.add(Task(text='Чего больше: шляп или конфет?', choice=['Шляп', 'Конфет', "Поровну"], answer='Конфет', image='pic/7.jpg'))
lvl_3.add(Task(text='Чего больше: снежинок или лягушек?', choice=['Лягушек', 'Снежинок', "Поровну"], answer='Поровну', image='pic/7.jpg'))

lvl_4 = Level(1, info='Добро пожаловать! Продолжим наше занятие')
lvl_4.add(Task(text='Свеклы больше, меньше или равно?', choice=['Больше', 'Меньше', 'Равно'], answer='Равно', image='pic/8.jpg'))
lvl_4.add(Task(text='Морковки больше, меньше или равно?', choice=['Больше', 'Меньше', 'Равно'], answer='Равно', image='pic/9.jpg'))
lvl_4.add(Task(text='Лука больше, меньше или равно?', choice=['Больше', 'Меньше', 'Равно'], answer='Больше', image='pic/10.jpg'))
lvl_4.add(Task(text='Желудей больше, меньше или равно по сравнению с клубникой?', choice=['Больше', 'Меньше', 'Равно'], answer='Меньше', image='11.jpg'))

lvl_5 = Level(1, info='Отлично, а теперь блиц')
lvl_5.add(Task(text='Кто больше: волк или жук?', choice=['Волк', 'Жук', 'Похожие по размеру'], answer='Волк'))
lvl_5.add(Task(text='А что выше: светофор или дом?', choice=['Дом', 'Светофор', 'Похожие по размеру'], answer='Дом'))
lvl_5.add(Task(text='Кто умнее: филин или кабан?', choice=['Кабан', 'Филин', 'Похожие по уму'], answer='Филин'))

lvl_6 = Level(1, info='Уже неплохо получается! Давай займемся пространством')
lvl_6.add(Task(text='Как мальчику дойти до школы?', choice=['Пойти направо', 'Пойти налево', 'Пойти вперёд'], answer='Пойти направо', image='pic/12.jpg'))
lvl_6.add(Task(text='А как дойти до кинотеатра?', choice=['Пойти направо', 'Пойти налево', 'Пойти вперёд'], answer='Пойти налево', image='pic/12.jpg'))
lvl_6.add(Task(text='Сколько цветов справа от мальчика?', answer='2', image='pic/12.jpg'))
lvl_6.add(Task(text='А сколько слева от мальчика?', answer='3', image='pic/12.jpg'))

lvl_7 = Level(1, info='Посмотри какой красивый зайчик!')
lvl_7.add(Task(text='Что он сделал первым делом?', choice=['Поел', 'Проснулся', 'Сделал зарядку', "Пошёл в школу"], answer='Проснулся', image='pic/13.jpg'))
lvl_7.add(Task(text='Что он сделал потом?', choice=['Поел', 'Проснулся', 'Сделал зарядку', "Пошёл в школу"], answer='Сделал зарядку', image='pic/13.jpg'))
lvl_7.add(Task(text='Какое было его последнее действие?', choice=['Поесть', 'Проснуться', 'Сделать зарядку', "Пойти в школу"], answer='Пойти в школу', image='pic/13.jpg'))
lvl_7.add(Task(text='А всего было действий?', answer='5', image='pic/13.jpg'))

lvl_8 = Level(1, info='Все знают сказку про колобка!')
lvl_8.add(Task(text='Кого он встретил первым?', choice=['Лису', 'Бабушку с дедушкой', 'Волка', "Зайца"], answer='Бабушку с дедушкой'))
lvl_8.add(Task(text='А потом он с кем встретился?', choice=['С лисой', 'С медведем', 'Волка', "Зайца"], answer='С зайцем'))
lvl_8.add(Task(text='На ком же закончился его путь?', choice=['Лиса', 'Бабушка с дедушкой', 'Волк', "Медведь"], answer='Лиса'))
lvl_8.add(Task(text='А кто был самым маленьким героем этой сказки?', choice=['Лиса', 'Колобок', 'Заяц', "Медведь"], answer='Колобок'))

lvl_9 = Level(1, info='Рассмотрим картинку')
lvl_9.add(Task(text='В первом случае яблоко лежит', choice=['Под стулом', 'Около стула', 'За стулом', "Перед стулом"], answer='Перед стулом', image='pic/14.jpg'))
lvl_9.add(Task(text='А на третьей картинке яблоко лежит', choice=['Под стулом', 'Около стула', 'За стулом', "На стуле"], answer='Около стула', image='pic/14.jpg'))
lvl_9.add(Task(text='А на пятой картинке где оно лежит?', choice=['Под стулом', 'Около стула', 'За стулом', "На стуле"], answer='Под стулом', image='pic/14.jpg'))

lvl_10 = Level(1, info='Рассмотрим картинку', style='test', time=60, topic='Счет предметов. Сравнение групп предметов. Пространственные и временные представления.')
lvl_10.add(Task(text='Сколько на картинке зонтиков?', answer='4', image='pic/16.jpg'))
lvl_10.add(Task(text='А батонов тут сколько?', answer='6', image='pic/16.jpg'))
lvl_10.add(Task(text='Хорошо, а чего больше: карандашей или снежинок?', choice=['Снежинок', 'Карандашей', 'Поровну'],
                 answer='Снежинок', image='pic/16.jpg'))
lvl_10.add(Task(text='А что больше по размеру: дом или зонтик?', choice=['Дом', 'Зонтик', 'Похожие'], answer='Дом',
                 image='pic/16.jpg'))
lvl_10.add(Task(text='Рассмотрим новую картинку. Где дети старше?', choice=['Слева', 'По краям', 'В центре'],
                 answer='Снежинок', image='pic/15.jpg'))
lvl_10.add(Task(text='Кто выше: мальчик в кепке или девочка с каре?', choice=['Девочка', 'Мальчик', 'Одного роста'],
                 answer='Мальчик', image='pic/15.jpg'))
lvl_10.add(Task(text='А у кого из них самые длинные брюки?',
                 choice=['Он стоит крайним', 'Он стоит справа от мальчика в кепке', 'Он слева от мальчика в кепке',
                         "У нее хвостик", "Он носит кепку"], answer='Он слева от мальчика в кепке', image='pic/15.jpg'))
lvl_10.add(Task(text='А у кого из девочек самая коротка стрижка?',
                 choice=['Она по центру', 'Она крайняя', 'Справа от нее стоит девочка', "Слева от нее мальчик"],
                 answer='Она крайняя', image='pic/15.jpg'))

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
year_1.add_level(topic_1)

# тема 2
topic_2 = Topic('Понятия «много», «один», «длиннее», «короче», «одинаковые по длине».')

lvl_1 = Level(1, info='Определи размер предметов и ответь на вопросы')
lvl_1.add(Task(text='Какая палочка самая длинная?', choice=['1', '2', '3'], answer='3', image='pic/18.jpg'))
lvl_1.add(Task(text='Какая морковка самая короткая?', choice=['1', '2', '3'], answer='1', image='pic/18.jpg'))

lvl_2 = Level(1, info="Определи на каком месте?")
lvl_2.add(Task(text="На каом месте четвертая по размеру гусиница?", choice=['1', '2', '3', '4', '5'], answer='3',
                image='pic/21.jpg'))

lvl_3 = Level(1, info='какой предмет толще ?')
lvl_3.add(Task(text="какой ствол толще?", choice=['правый', 'лелый'], answer='левый', image='pic/22.jpg'))
lvl_3.add(Task(text="Какая морковка толще?", choice=['правая', 'левая'], answer='правая', image="pic/23.jpg"))

lvl_3 = Level(1, info='одинаковые ли длинны?')
lvl_3.add(
    Task(text="Есть ли на картинке ленточки одинаковой длинны", choice=['нет', 'да'], answer='да', image='pic/23.jpg'))
lvl_3.add(Task(text="Все ли линии одиноковые по длинне?", choice=['да', 'нет'], answer='нет', image="pic/25.jpg"))

lvl_4 = Level(1, info="посчитай предметы на картинке")
lvl_4.add(Task(text='много или мало предметов?', image='pic/2.jpg', choice=["много", "мало"], answer="много" ))
lvl_4.add(Task(text='много или мало предметов?', image='pic/23.jpg', choice=["много", "мало"], answer="мало" ))
lvl_4.add(Task(text='много или мало предметов?', image='pic/1.jpg', choice=["много", "мало"], answer="много" ))

lvl_5 = Level(1, info="посчитай предметы на картинке")
lvl_5.add(Task(text='Какая палочка самая длинная?', choice=['1', '2', '3'], answer='3', image='pic/18.jpg'))
lvl_5.add(Task(text='Какая морковка самая короткая?', choice=['1', '2', '3'], answer='1', image='pic/18.jpg'))


lvl_6 = Level(1, info="посчитай предметы на картинке")
lvl_6.add(Task(text='сколько фигур на картинке?', image='pic/40.jpg', choice=["5", "20", "1"], answer="5" ))
lvl_6.add(Task(text='сколько фигур на картинке?', image='pic/23.jpg', choice=["много", "мало"], answer="мало" ))
lvl_6.add(Task(text='сколько кусочков на картинке?', image='pic/54.jpg', answer="2" ))

lvl_7 = Level(1, info="давай немного начнем повторять")
lvl_7.add(Task(text='Сколько же здесь грибов?', answer='8', image='pic/2.jpg'))
lvl_7.add(Task(text='А здесь сколько девочек?', answer='4', image='pic/3.jpg'))
lvl_7.add(Task(text='А сколько на этой картинке цветов?', answer='3', image='pic/4.jpg'))


lvl_8 = Level(1, info="продолжим повторять")
lvl_8.add(Task(text='Сколько же у них всего крыльев?', answer='12', image='pic/4.jpg'))
lvl_8.add(Task(text='А сколько на этой картинке цветов?', answer='3', image='pic/4.jpg'))

lvl_9 = Level(1, info="последний раз")
lvl_9.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_9.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))


lvl_10 = Level(1, info='Рассмотрим картинку', style='test', time=60, topic='Сравнение предметов по форме(длинна толщина).')
lvl_10.add(Task(text="какая палочка самая длинная?", choice=['зеланая', 'синяя', 'крассная'], answer='Крассная',
                image='pic/25.jpg'))
lvl_10.add(
    Task(text="А какая самая короткая ?", choice=['зеланая', 'синяя', 'крассная'], answer='нет', image="pic/25.jpg"))
lvl_10.add(Task(text="Чего больше перцев или морковок?", choice=['морковок', 'перцев', 'одинакого'], answer='Одинокого',
                image='pic/9.jpg'))
lvl_10.add(Task(text="Какая палочка между длинной и короткой", choice=['2', '3', '1'], answer='2', image="pic/18.jpg"))
lvl_10.add(Task(text="под каким номером самая кароткая гусеница?", answer='2', image='pic/21.jpg'))
lvl_10.add(
    Task(text="Есть ли на картинке предметы одиниковой длинны?", choice=['нет', 'да'], answer='да', image="pic/17.jpg"))



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
year_1.add_level(topic_2)

# тема 3
topic_3= Topic('Знаки «+», «-». Состав числа 5 из двухслагаемых.')

lvl_1 = Level(1, info='Знаки «+», «-»')
lvl_1.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_1.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_1.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))
lvl_1.add(Task(text='Выберите знак', choice=['+', '-'], answer='-', image='pic/29.jpg'))
lvl_1.add(Task(text='Ну и последний раз', choice=['+', '-'], answer='+', image='pic/30.jpg'))

lvl_2 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_2.add(Task(text='Какую цифру нужно постаивть?', answer='2', image='pic/31.jpg'))
lvl_2.add(Task(text='Что нужно поставить ?', answer='1', image='pic/32.jpg'))
lvl_2.add(Task(text='', answer='1', image='pic/33.jpg'))
lvl_2.add(Task(text='Ну и последний раз', answer='5', image='pic/34.jpg'))


lvl_3 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_3.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_3.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_3.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))

lvl_4 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_4.add(Task(text='Ну и последний раз', choice=['+', '-'], answer='+', image='pic/30.jpg'))
lvl_4.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))


lvl_5 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_5.add(Task(text='+ или -', choice=['-', '+', '*', '/'], answer='+', image='pic/28.jpg'))
lvl_5.add(Task(text='Выберите знак', choice=['-', '+', '*', '/'], answer='-', image='pic/29.jpg'))
lvl_5.add(Task(text='Ну и последний раз', choice=['-', '+', '*', '/'], answer='+', image='pic/30.jpg'))

lvl_6 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_6.add(Task(text='какой знак нужно поставить?', choice=['-', '+', '*', '/'], answer='-', image='pic/26.jpg'))
lvl_6.add(Task(text='Выберите знак + или -', choice=['-', '+', '*', '/'], answer='+', image='pic/27.jpg'))
lvl_6.add(Task(text='+ или -', choice=['-', '+', '*', '/'], answer='+', image='pic/28.jpg'))


lvl_7 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_7.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_7.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_7.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))

lvl_8 = Level(1, info='давай немного повтарим прошлую тему')
lvl_8.add(Task(text='А здесь сколько девочек?', answer='4', image='pic/3.jpg'))
lvl_8.add(Task(text='А сколько на этой картинке цветов?', answer='3', image='pic/4.jpg'))

lvl_9 = Level(1, info='последний раз')
lvl_9.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_9.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))



lvl_10 = Level(1, info='Рассмотрим картинку', style='test', time=60, topic='Раставить знаки и числа в пропуски.')
lvl_10.add(Task(text='Какую цифру нужно постаивть?', answer='2', image='pic/31.jpg'))
lvl_10.add(Task(text='Что нужно поставить ?', answer='1', image='pic/32.jpg'))
lvl_10.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_10.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_10.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))

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
year_1.add_level(topic_3)

# тема 4
topic_4 = Topic('Знаки «<», «>», «=». Равенство. Неравенство')

lvl_1 = Level(1, info='Знаки «<», «>», «=».')
lvl_1.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/35.jpg'))
lvl_1.add(Task(text='', choice=['<', '>', '='], answer='<', image='pic/38.jpg'))
lvl_1.add(Task(text='', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))


lvl_2 = Level(1, info='Знаки «<», «>», «=».')
lvl_2.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/35.jpg'))
lvl_2.add(Task(text='', choice=['<', '>', '='], answer='>', image='pic/36.jpg'))
lvl_2.add(Task(text='', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))

lvl_3 = Level(1, info='Знаки «<», «>», «=».')
lvl_3.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/36.jpg'))
lvl_3.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))

lvl_4 = Level(1, info='Знаки «<», «>», «=».')
lvl_4.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_4.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))

lvl_5 = Level(1, info='давай повтарим прошлые темы.')
lvl_5.add(Task(text='А здесь сколько девочек?', answer='4', image='pic/3.jpg'))
lvl_5.add(Task(text='А сколько на этой картинке цветов?', answer='3', image='pic/4.jpg'))
lvl_5.add(Task(text='сколько фигур на картинке?', image='pic/23.jpg', choice=["много", "мало"], answer="мало" ))
lvl_5.add(Task(text='сколько кусочков на картинке?', image='pic/54.jpg', answer="2" ))

lvl_6 = Level(1, info='давай повтарим прошлые темы.')
lvl_6.add(Task(text="Есть ли на картинке ленточки одинаковой длинны", choice=['нет', 'да'], answer='да', image='pic/23.jpg'))
lvl_6.add(Task(text="Все ли линии одиноковые по длинне?", choice=['да', 'нет'], answer='нет', image="pic/25.jpg"))


lvl_7 = Level(1, info='еще повторим темы.')
lvl_7.add(Task(text='Что он сделал потом?', choice=['Поел', 'Проснулся', 'Сделал зарядку', "Пошёл в школу"], answer='Сделал зарядку', image='pic/13.jpg'))
lvl_7.add(Task(text='Какое было его последнее действие?', choice=['Поесть', 'Проснуться', 'Сделать зарядку', "Пойти в школу"], answer='Пойти в школу', image='pic/13.jpg'))
lvl_7.add(Task(text='А всего было действий?', answer='5', image='pic/13.jpg'))



lvl_7 = Level(1, info='еще пару раз.')
lvl_7.add(Task(text='А здесь сколько девочек?', answer='4', image='pic/3.jpg'))
lvl_7.add(Task(text='А сколько на этой картинке цветов?', answer='3', image='pic/4.jpg'))


lvl_8 = Level(1, info='еще пару раз.')
lvl_8.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_8.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_8.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))


lvl_9 = Level(1, info="последний раз")
lvl_9.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_9.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))

lvl_10 = Level(1, info='Рассмотрим картинку', style='test', time=40, topic='Раставить знаки в пропуски.')
lvl_10.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_10.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/36.jpg'))
lvl_10.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))
lvl_10.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_10.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))

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
year_1.add_level(topic_4)


# тема 5

topic_5 = Topic("Многоугольники.")
lvl_1 = Level(1, info='Многоугольники')
lvl_1.add(Task(text='сколько углов у синей фигуры?', answer='8', image='pic/40.jpg'))
lvl_1.add(Task(text='как называется эта фигура?', choice=['восьмиугольник', 'треугольник', 'квадрат'], answer='восьмиугольник', image='pic/40.jpg'))
lvl_1.add(Task(text='как называется красная фигура?', choice=['восьмиугольник', 'треугольник', 'квадрат'], answer='треугольник', image='pic/41.jpg'))
lvl_1.add(Task(text='сколько углов у фигуры под номером 9? ', answer='12', image='pic/42.jpg'))

lvl_2 = Level(1, info='сколько всего углов?')
lvl_2.add(Task(text='сколько углов у синей фигуры?', answer='4', image='pic/118.jpg'))
lvl_2.add(Task(text='как называется эта фигура?', choice=['восьмиугольник', 'треугольник', 'квадрат'], answer='восьмиугольник', image='pic/40.jpg'))
lvl_2.add(Task(text='как называется красная фигура?', choice=['восьмиугольник', 'треугольник', 'квадрат'], answer='треугольник', image='pic/41.jpg'))
lvl_2.add(Task(text='сколько всего прямых углов на картинке ', answer='4', image='pic/119.jpg'))

lvl_3 = Level(1, info='посчитай все углы на картинке')
lvl_3.add(Task(text='сколько углов?', answer='26', image='pic/40.jpg'))
lvl_3.add(Task(text='сколько углов всего на картинке?', answer='30', image='pic/127.jpg'))

lvl_4 = Level(1, info='определи количество углов по описанию')
lvl_4.add(Task(text='если фигуру называют триугольник то сколько у нее углов ?', answer='3'))
lvl_4.add(Task(text='если фигуру называют восьмиугольник то сколько у нее углов ?', answer='8'))

lvl_5 = Level(1, info='определи фигуру по колличеству углов')
lvl_5.add(Task(text='если у фигуры 3 угла как ее называют?', answer='треугольник', choice=['триугольник', 'восьмиугольник', 'пятиугольник']))
lvl_5.add(Task(text='если у фигуры 6 угла как ее называют?', answer='шестиугольник', choice=['триугольник', 'шестиугольник', 'пятиугольник']))

lvl_6 = Level(1, info='давай повтарим прошлые темы')
lvl_6.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_6.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))

lvl_7 = Level(1, info='еще')
lvl_7.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_7.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))

lvl_8 = Level(1, info='еще повторим темы.')
lvl_8.add(Task(text='Что он сделал потом?', choice=['Поел', 'Проснулся', 'Сделал зарядку', "Пошёл в школу"], answer='Сделал зарядку', image='pic/13.jpg'))
lvl_8.add(Task(text='Какое было его последнее действие?', choice=['Поесть', 'Проснуться', 'Сделать зарядку', "Пойти в школу"], answer='Пойти в школу', image='pic/13.jpg'))
lvl_8.add(Task(text='А всего было действий?', answer='5', image='pic/13.jpg'))


lvl_9 = Level(1, info='Рассмотрим картинку')
lvl_9.add(Task(text='В первом случае яблоко лежит', choice=['Под стулом', 'Около стула', 'За стулом', "Перед стулом"], answer='Перед стулом', image='pic/14.jpg'))
lvl_9.add(Task(text='А на третьей картинке яблоко лежит', choice=['Под стулом', 'Около стула', 'За стулом', "На стуле"], answer='Около стула', image='pic/14.jpg'))
lvl_9.add(Task(text='А на пятой картинке где оно лежит?', choice=['Под стулом', 'Около стула', 'За стулом', "На стуле"], answer='Под стулом', image='pic/14.jpg'))



lvl_10 = Level(1, info='Рассмотрим картинку', style='test', time=40, topic='Многоугольники.')
lvl_10.add(Task(text='сколько фигур с 4 углами?', answer='2', image='pic/41.jpg'))
lvl_10.add(Task(text='сколько фигур с 2 углами?', answer='2', image='pic/41.jpg'))
lvl_10.add(Task(text='под каким номером фигура с 12 углами?', answer='7', image='pic/42.jpg'))
lvl_10.add(Task(text='сколько углов у синей фигуры?', answer='8', image='pic/40.jpg'))

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
year_1.add_level(topic_5)

# тема 6

topic_6 = Topic('Задачи на увеличение (уменьшение) числа на несколько единиц.')
lvl_1 = Level(1, info='Задачи на увеличение (уменьшение) числа на несколько единиц.')

lvl_1.add(Task(text='На площадке играет 7 детей. Потом к ним присоединилось 3 детей. Сколько детей играет на площадке теперь?', answer='10'))
lvl_1.add(Task(text='На красной ленте было 9 шариков, а потом еще прибавили 2 шарика. Сколько шариков на красной ленте теперь?', answer='11'))
lvl_1.add(Task(text='В коробке было 8 яблок, а потом в нее положили еще 4 яблока. Сколько яблок в коробке всего?', answer='12'))
lvl_1.add(Task(text='У Маши было 6 кукол, потом ее подруга подарила ей еще 5 кукол. Сколько кукол у Маши стало после подарка?', answer='11'))


lvl_2 = Level(1, info='решить еще чучуть подобных задачек')
lvl_2.add(Task(text=' В корзине было 5 яблок, а потом в нее положили еще 3 яблока. Сколько яблок стало в корзине?', answer='8'))
lvl_2.add(Task(text='У птички было 7 яиц, а потом она снесла еще 2 яйца. Сколько яиц у птички теперь?', answer='9'))


lvl_3 = Level(1, info='решить еще чучуть подобных задачек')
lvl_3.add(Task(text=' У Маши было 9 конфет, потом она отдала другу 4 конфеты. Сколько конфет осталось у Маши?', answer='5'))
lvl_3.add(Task(text='У кота было 6 мышей, а потом он поймал еще 5 мышей. Сколько мышей у кота всего?', answer='11'))

lvl_4 = Level(1, info='решить еще чучуть подобных задачек')
lvl_4.add(Task(text='У дерева было 10 ягод, но 3 упали на землю.', answer='7'))
lvl_4.add(Task(text=' В книге было 6 страниц, а дописали еще 4.', answer='10'))

lvl_5 = Level(1, info='последний раз и повтарим прошлое')
lvl_5.add(Task(text='На площадке играет 7 детей. Потом к ним присоединилось 4 детей. Сколько детей играет на площадке теперь?', answer='11'))
lvl_5.add(Task(text='На красной ленте было 8 шариков, а потом еще прибавили 2 шарика. Сколько шариков на красной ленте теперь?', answer='10'))
lvl_5.add(Task(text='В коробке было 4 яблок, а потом в нее положили еще 4 яблока. Сколько яблок в коробке всего?', answer='8'))
lvl_5.add(Task(text='У Маши было 5 кукол, потом ее подруга подарила ей еще 5 кукол. Сколько кукол у Маши стало после подарка?', answer='10'))

lvl_6 = Level(1, info='теперь повтрами прошлые темы')
lvl_6.add(Task(text='Где предметов больше: слева и справа?', choice=['Слева', 'Справа'], answer='Слева', image='pic/5.jpg'))
lvl_6.add(Task(text='Каких мишек больше?', choice=['Бурых', 'Белых'], answer='Бурых', image='pic/6.jpg'))
lvl_6.add(Task(text='Чего больше: шляп или конфет?', choice=['Шляп', 'Конфет', "Поровну"], answer='Конфет', image='pic/7.jpg'))
lvl_6.add(Task(text='Чего больше: снежинок или лягушек?', choice=['Лягушек', 'Снежинок', "Поровну"], answer='Поровну', image='pic/7.jpg'))

lvl_7 = Level(1, info='Все знают сказку про колобка!')
lvl_7.add(Task(text='Кого он встретил первым?', choice=['Лису', 'Бабушку с дедушкой', 'Волка', "Зайца"], answer='Бабушку с дедушкой'))
lvl_7.add(Task(text='А потом он с кем встретился?', choice=['С лисой', 'С медведем', 'Волка', "Зайца"], answer='С зайцем'))
lvl_7.add(Task(text='На ком же закончился его путь?', choice=['Лиса', 'Бабушка с дедушкой', 'Волк', "Медведь"], answer='Лиса'))
lvl_7.add(Task(text='А кто был самым маленьким героем этой сказки?', choice=['Лиса', 'Колобок', 'Заяц', "Медведь"], answer='Колобок'))

lvl_8 = Level(1, info="посчитай предметы на картинке")
lvl_8.add(Task(text='много или мало предметов?', image='pic/2.jpg', choice=["много", "мало"], answer="много" ))
lvl_8.add(Task(text='много или мало предметов?', image='pic/23.jpg', choice=["много", "мало"], answer="мало" ))
lvl_8.add(Task(text='много или мало предметов?', image='pic/1.jpg', choice=["много", "мало"], answer="много" ))


lvl_9 = Level(1, info='Рассмотрим картинку')
lvl_9.add(Task(text='В первом случае яблоко лежит', choice=['Под стулом', 'Около стула', 'За стулом', "Перед стулом"], answer='Перед стулом', image='pic/14.jpg'))
lvl_9.add(Task(text='А на третьей картинке яблоко лежит', choice=['Под стулом', 'Около стула', 'За стулом', "На стуле"], answer='Около стула', image='pic/14.jpg'))
lvl_9.add(Task(text='А на пятой картинке где оно лежит?', choice=['Под стулом', 'Около стула', 'За стулом', "На стуле"], answer='Под стулом', image='pic/14.jpg'))



lvl_10 = Level(1, info='посчитай', style='test', time=40, topic='Задачи на увеличение (уменьшение) числа на несколько единиц..')
lvl_10.add(Task(text='В сумке было 7 карандашей, а добавили еще 3.', answer='10'))
lvl_10.add(Task(text='У дерева было 10 ягод, но 3 упали на землю.', answer='7'))
lvl_10.add(Task(text=' В книге было 6 страниц, а дописали еще 4.', answer='10'))
lvl_10.add(Task(text='На тарелке было 5 печений, а съели еще 3', answer='2'))

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
year_1.add_level(topic_6)



# тема 7

topic_7 = Topic('Задачи на разностное сравнение чисел. Перестановка слагаемых.')


lvl_1 = Level(1, info='попробуй решаить эти задачки')
lvl_1.add(Task(text='У Маши было 5 красных конфет и 3 синих. После того, как она дала своему другу 2 красных конфеты, сколько у нее останется конфет каждого цвета?', answer='6'))
lvl_1.add(Task(text='Коля нарисовал 8 солнышек и 4 облака. Потом он добавил еще 3 солнышка. Сколько солнышек у него теперь?', answer='15'))
lvl_1.add(Task(text='У Вики было 7 карандашей, а у Миши было на 2 карандаша больше. Сколько карандашей у Миши?', answer='9'))


lvl_2 = Level(1, info='попробуй решаить эти задачки')
lvl_2.add(Task(text=' У Маши было 5 красных конфет, а у Насти было 4. Какая из девочек получила больше конфет?', answer='Маша', choice=['Настя', "Маша"]))
lvl_2.add(Task(text='У Пети было 7 зеленых маркеров, а у Кати было 6. Кто из детей получил больше маркеров?', answer='Петя', choice=["Петя", "Катя"]))
lvl_2.add(Task(text='В коробке было 8 красных шариков и 3 синих. Сколько шариков было всего?', answer='11'))


lvl_3 = Level(1, info='попробуй решаить эти задачки')
lvl_3.add(Task(text='У Вики было 7 карандашей, а у Миши было на 1 карандаша больше. Сколько карандашей у Миши?', answer='8'))
lvl_3.add(Task(text='У Пети было 7 зеленых маркеров, а у Кати было 5. Кто из детей получил больше маркеров?', answer='Петя', choice=["Петя", "Катя"]))
lvl_3.add(Task(text='В коробке было 8 красных шариков и 2 синих. Сколько шариков было всего?', answer='10'))

lvl_4 = Level(1, info='теперь попробуй такие задачи ')
lvl_4.add(Task(text='В школе было 10 учеников, а в детском саду - 6. Сколько детей было всего?', answer='16'))
lvl_4.add(Task(text='В корзине было 11 яблок, а в сумке - 6. Сколько яблок было вместе?', answer='17'))
lvl_4.add(Task(text='У Кати было 9 конфет, а у Пети - 4. Кто из детей получил больше конфет?', answer='Катя', choice=["Катя", "Петя"]))


lvl_5 = Level(1, info='а такие задачи? ')
lvl_5.add(Task(text='У Вики было 7 карандашей, а у Миши было на 1 карандаша больше. Сколько карандашей у Миши?', answer='8'))
lvl_5.add(Task(text='В корзине было 11 яблок, а в сумке - 6. Сколько яблок было вместе?', answer='17'))


lvl_6 = Level(1, info='Давай повторим прошлые темы ')
lvl_6.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_6.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))
lvl_6.add(Task(text='сколько фигур на картинке?', image='pic/23.jpg', choice=["много", "мало"], answer="мало" ))
lvl_6.add(Task(text='сколько кусочков на картинке?', image='pic/54.jpg', answer="2" ))

lvl_7 = Level(1, info='хмммм, где-то ты это уже решал?')
lvl_7.add(Task(text='Сколько же здесь грибов?', answer='8', image='pic/2.jpg'))
lvl_7.add(Task(text='А здесь сколько девочек?', answer='4', image='pic/3.jpg'))
lvl_7.add(Task(text='А сколько на этой картинке цветов?', answer='3', image='pic/4.jpg'))


lvl_8 = Level(1, info='какие знакомые задачи, интерестно откуда они?')
lvl_8.add(Task(text='А потом он с кем встретился?', choice=['С лисой', 'С медведем', 'Волка', "Зайца"], answer='С зайцем'))
lvl_8.add(Task(text='На ком же закончился его путь?', choice=['Лиса', 'Бабушка с дедушкой', 'Волк', "Медведь"], answer='Лиса'))
lvl_8.add(Task(text='А кто был самым маленьким героем этой сказки?', choice=['Лиса', 'Колобок', 'Заяц', "Медведь"], answer='Колобок'))

lvl_9 = Level(1, info="последний раз")
lvl_9.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_9.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))



lvl_10 = Level(1, info='Реши задачки', style='test', time=40, topic='Задачи на разностное сравнение чисел. Перестановка слагаемых.')
lvl_10.add(Task(text='У Пети было 8 красных конфет, а у Кати было 2. Кто из детей получил больше конфет?', answer='Петя', choice=["Петя", "Катя"]))
lvl_10.add(Task(text='В школе было 10 учеников, а в детском саду - 6. Сколько детей было всего?', answer='16'))
lvl_10.add(Task(text='В корзине было 11 яблок, а в сумке - 6. Сколько яблок было вместе?', answer='17'))
lvl_10.add(Task(text='У Кати было 9 конфет, а у Пети - 4. Кто из детей получил больше конфет?', answer='Катя', choice=["Катя", "Петя"]))


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
year_1.add_level(topic_7)


# тема 8

topic_8 = Topic('Составление таблицы сложения +5,6,7,8,9.  Состав чисел в пределах 10.')


lvl_1 = Level(1, info='реши примеры')
lvl_1.add(Task(text='1+3=?', answer='4'))
lvl_1.add(Task(text='6+3', answer='9'))
lvl_1.add(Task(text='8+2', answer='10'))


lvl_2 = Level(1, info='составь примеры')
lvl_2.add(Task(text="1+?=7", answer='6'))
lvl_2.add(Task(text="3+?=10", answer='7'))
lvl_2.add(Task(text="7+?=10", answer='3'))


lvl_3 = Level(1, info='составь примеры')
lvl_3.add(Task(text="5+?=9", answer='4'))
lvl_3.add(Task(text="?+6=7", answer='6'))
lvl_3.add(Task(text="7+?=10", answer='3'))


lvl_4 = Level(1, info='ну здесь просто примеры')
lvl_4.add(Task(text="5+?=10", answer='5'))
lvl_4.add(Task(text="?+1=7", answer='6'))
lvl_4.add(Task(text="8+?=10", answer='2'))

lvl_5 = Level(1, info='еще разок')
lvl_5.add(Task(text="3+?=10", answer='7'))
lvl_5.add(Task(text="?+1=6", answer='5'))
lvl_5.add(Task(text="8+?=9", answer='1'))


lvl_6 = Level(1, info='ну это элементарно!!!')
lvl_6.add(Task(text="3+?=3", answer='0'))
lvl_6.add(Task(text="?+1=1", answer='0'))
lvl_6.add(Task(text="8+?=8", answer='0'))

lvl_7 = Level(1, info='повтарим')
lvl_7.add(Task(text='В коробке было 8 яблок, а потом в нее положили еще 4 яблока. Сколько яблок в коробке всего?', answer='12'))
lvl_7.add(Task(text='У Маши было 6 кукол, потом ее подруга подарила ей еще 5 кукол. Сколько кукол у Маши стало после подарка?', answer='11'))

lvl_8 = Level(1, info="давай немного начнем повторять")
lvl_8.add(Task(text='Сколько же здесь грибов?', answer='8', image='pic/2.jpg'))
lvl_8.add(Task(text='А здесь сколько девочек?', answer='4', image='pic/3.jpg'))
lvl_8.add(Task(text='А сколько на этой картинке цветов?', answer='3', image='pic/4.jpg'))


lvl_9 = Level(1, info='Давай повторим прошлые темы ')
lvl_9.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_9.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))
lvl_9.add(Task(text='сколько фигур на картинке?', image='pic/23.jpg', choice=["много", "мало"], answer="мало" ))
lvl_9.add(Task(text='сколько кусочков на картинке?', image='pic/54.jpg', answer="2" ))



lvl_10 = Level(1, info='реши примеры или стоставь их', style='test', time=40, topic='Составление таблицы сложения +5,6,7,8,9.  Состав чисел в пределах 10.')
lvl_10.add(Task(text="5+2=?", answer='7'))
lvl_10.add(Task(text="2+6=?", answer='8'))
lvl_10.add(Task(text="7+?=8", answer='1'))
lvl_10.add(Task(text="5+?=8", answer='3'))
lvl_10.add(Task(text="?+6=6", answer='0'))
lvl_10.add(Task(text="7+?=9", answer='2'))
lvl_10.add(Task(text="5+?=6", answer='1'))
lvl_10.add(Task(text="?+6=9", answer='3'))
lvl_10.add(Task(text="7+?=8", answer='1'))




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
year_1.add_level(topic_8)


# тема 9


topic_9 = Topic('Вычитаемое. Разность. Вычитание вида 8-16.')


lvl_1 = Level(1, info='реши примеры или составь примеры ')
lvl_1.add(Task(text="8-3=?", answer='5'))
lvl_1.add(Task(text="8-1=?", answer='7'))
lvl_1.add(Task(text="8-4=?", answer='4'))


lvl_2 = Level(1, info='реши примеры или составь примеры ')
lvl_2.add(Task(text='5-2=?', answer="3"))
lvl_2.add(Task(text='5-1=?', answer="4"))
lvl_2.add(Task(text='5-5=?', answer="0"))


lvl_3 = Level(1, info='а теперь составь примеры.')
lvl_3.add(Task(text='5-?=2', answer="3"))
lvl_3.add(Task(text='5-?=1', answer="4"))
lvl_3.add(Task(text='5-?=0', answer="5"))

lvl_4 = Level(1, info='составь примеры.')
lvl_4.add(Task(text='2-?=2', answer="0"))
lvl_4.add(Task(text='6-?=1', answer="5"))
lvl_4.add(Task(text='0-?=0', answer="0"))

lvl_5 = Level(1, info='еще пару раз')
lvl_5.add(Task(text='5-?=2', answer="3"))
lvl_5.add(Task(text='6-?=1', answer="5"))
lvl_5.add(Task(text='1-?=0', answer="1"))

lvl_6 = Level(1, info='и еще немного.')
lvl_6.add(Task(text='5-?=2', answer="3"))
lvl_6.add(Task(text='5-?=1', answer="4"))
lvl_6.add(Task(text='5-?=0', answer="5"))


lvl_7 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_7.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_7.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_7.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))


lvl_8 = Level(1, info='еще пару раз.')
lvl_8.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_8.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_8.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))


lvl_9 = Level(1, info="последний раз")
lvl_9.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_9.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))


lvl_10 = Level(1, info='реши примеры или стоставь их', style='test', time=40, topic='Составление таблицы сложения +5,6,7,8,9.  Состав чисел в пределах 10.')
lvl_10.add(Task(text='6-?=0', answer="6"))
lvl_10.add(Task(text='5-?=5', answer="0"))
lvl_10.add(Task(text='5-?=3', answer="2"))
lvl_10.add(Task(text='6-3=?', answer="3"))
lvl_10.add(Task(text='5-3=?', answer="2"))
lvl_10.add(Task(text='5-?=0', answer="5"))

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
year_1.add_level(topic_9)

# тема 10

topic_10 = Topic('Нумерация от 10 до 20.')

lvl_1 = Level(1, info='раставь цифры в правильном порядке.')
lvl_1.add(Task(text='выполни задания на картинке', image="pic/44.jpg", answer="67891011121314151617"))
lvl_1.add(Task(text='запиши пропушеные цифры', image="pic/45.jpg", answer="24579"))
lvl_1.add(Task(text='найди соседние цифры', answer="1113", image="pic/46.jpg"))


lvl_2 = Level(1, info='найди соседние цифры')
lvl_2.add(Task(text='найди соседий', image="pic/46.jpg", answer="1113"))
lvl_2.add(Task(text='найди соседий', image="pic/47.jpg", answer="1618"))
lvl_2.add(Task(text='найди соседий', image="pic/48.jpg", answer="1517"))
lvl_2.add(Task(text='выполни задания на картинке', image="pic/44.jpg", answer="67891011121314151617"))

lvl_3 = Level(1, info='раставить в порядку возрастания.')
lvl_3.add(Task(text=' Как называется единица измерения длины, которая равна 1 дециметру?', answer="Дециметр", choice=["Дециметр", "Метр", "Сантиметр"]))
lvl_3.add(Task(text='Расставь числа в порядке возрастания: 15 дм, 7 дм, 12 дм.', answer="71215"))
lvl_3.add(Task(text='Сколько дециметров в 1 метре?', answer="10"))
lvl_3.add(Task(text='А сколько дециметров в 4 метрах?', answer="40"))

lvl_4 = Level(1, info='найди соседние цифры')
lvl_4.add(Task(text='Коля измерил стол длиной 7 дм. Какая длина стола в метрах?', answer="70"))
lvl_4.add(Task(text='В классе лежит линейка длиной 10 дм. Сколько дециметров на ней?', answer="10"))
lvl_4.add(Task(text='На листе бумаги отмечено расстояние 5 дм. Если это расстояние разделить на 5 частей, сколько дециметров будет в каждой части?', answer="1"))
lvl_4.add(Task(text='Расставь числа в порядке возрастания: 15 дм, 7 дм, 12 дм.', answer="71215"))
lvl_4.add(Task(text="5+?=15", answer='10'))
lvl_4.add(Task(text="?+2=14", answer='12'))
lvl_4.add(Task(text="7+?=18", answer='11'))

lvl_5 = Level(1, info='найди соседние цифры')
lvl_5.add(Task(text='6-?=-15', answer="9"))
lvl_5.add(Task(text='5-?=-1', answer="6"))
lvl_5.add(Task(text='5-?=19', answer="14"))
lvl_5.add(Task(text='6-3=?', answer="3"))
lvl_5.add(Task(text='5-6=?', answer="-1"))
lvl_5.add(Task(text='5-?=-7', answer="2"))


lvl_6 = Level(1, info='давай повтарим перед тестом')
lvl_6.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_6.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_6.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))


lvl_7 = Level(1, info='давай повтарим перед тестом')
lvl_7.add(Task(text="Какая палочка между длинной и короткой", choice=['2', '3', '1'], answer='2', image="pic/18.jpg"))
lvl_7.add(Task(text="под каким номером самая кароткая гусеница?", answer='2', image='pic/21.jpg'))
lvl_7.add(Task(text="Есть ли на картинке предметы одиниковой длинны?", choice=['нет', 'да'], answer='да', image="pic/17.jpg"))
lvl_7.add(Task(text='', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))
lvl_7.add(Task(text='', choice=['<', '>', '='], answer='<', image='pic/38.jpg'))
lvl_7.add(Task(text='', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))


lvl_8 = Level(1, info='давай повтарим перед тестом')
lvl_8.add(Task(text='под каким номером фигура с 12 углами?', answer='7', image='pic/42.jpg'))
lvl_8.add(Task(text='сколько углов у синей фигуры?', answer='8', image='pic/40.jpg'))
lvl_8.add(Task(text='6+3', answer='9'))
lvl_8.add(Task(text='5-?=3', answer="2"))

lvl_9 = Level(1, info='готов скоро тест')
lvl_9.add(Task(text='Сколько дециметров в 2 метрах?', answer="20"))
lvl_9.add(Task(text='Расставь числа в порядке возрастания: 15 дм, 7 дм, 12 дм.', answer="71215"))
lvl_9.add(Task(text="7+?=15", answer='8'))
lvl_9.add(Task(text='6+5', answer='11'))
lvl_9.add(Task(text='6+6', answer='12'))


lvl_10 = Level(1, info='это финальный тест', style='final_test', time=40, topic='финал 1 класса')


lvl_10.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))
lvl_10.add(Task(text='Сколько же здесь грибов?', answer='8', image='pic/2.jpg'))
lvl_10.add(Task(text='А здесь сколько девочек?', answer='4', image='pic/3.jpg'))
lvl_10.add(Task(text='А сколько у одной пчелки крылышек?', answer='2', image='pic/4.jpg'))
lvl_10.add(Task(text='Сколько же у них всего крыльев?', answer='12', image='pic/4.jpg'))
lvl_10.add(Task(text='А сколько на этой картинке цветов?', answer='3', image='pic/4.jpg'))
lvl_10.add(Task(text="Все ли линии одиноковые по длинне?", choice=['да', 'нет'], answer='нет', image="pic/25.jpg"))
lvl_10.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_10.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/36.jpg'))
lvl_10.add(Task(text='как называется эта фигура?', choice=['восьмиугольник', 'треугольник', 'квадрат'], answer='восьмиугольник', image='pic/40.jpg'))
lvl_10.add(Task(text='как называется красная фигура?', choice=['восьмиугольник', 'треугольник', 'квадрат'], answer='треугольник', image='pic/41.jpg'))
lvl_10.add(Task(text='сколько углов у фигуры под номером 9? ', answer='12', image='pic/42.jpg'))
lvl_10.add(Task(text='сколько фигур с 2 углами?', answer='2', image='pic/41.jpg'))
lvl_10.add(Task(text='6-3=?', answer="3"))
lvl_10.add(Task(text='5-3=?', answer="2"))
lvl_10.add(Task(text='запиши пропушеные цифры', image="pic/45.jpg", answer="24579"))
lvl_10.add(Task(text='найди соседние цифры', answer="1113", image="pic/46.jpg"))
lvl_10.add(Task(text='найди соседий', image="pic/47.jpg", answer="1618"))
lvl_10.add(Task(text='найди соседий', image="pic/48.jpg", answer="1517"))
lvl_10.add(Task(text="7+?=15", answer='8'))
lvl_10.add(Task(text='6+5', answer='11'))
lvl_10.add(Task(text='6+6', answer='12'))
lvl_10.add(Task(text="5+?=15", answer='10'))
lvl_10.add(Task(text="?+2=14", answer='12'))
lvl_10.add(Task(text="7+?=18", answer='11'))
lvl_10.add(Task(text="5+?=12", answer='7'))


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
year_1.add_level(topic_10)










