from company import *


year = Class(1)
first_topic = Topic('Счет предметов. Сравнение групп предметов. Пространственные и временные представления.')
lvl_11 = Level(1, info='Привет! Посчитай количество предметов на картинке и ответь на вопрос.')
lvl_11.add(Task(text='Сколько здесь желтых яблок?', answer='4', image='pic/1.jpg'))
lvl_11.add(Task(text='А сколько здесь всего яблок?', answer='9', image='pic/1.jpg'))
lvl_11.add(Task(text='Сколько же здесь грибов?', answer='8', image='pic/2.jpg'))
lvl_11.add(Task(text='А здесь сколько девочек?', answer='4', image='pic/3.jpg'))

lvl_21 = Level(1, info='Ты отлично справляешься! Смотри какие красивые пчелы!')
lvl_21.add(Task(text='Сколько здесь пчелок?', answer='6', image='pic/4.jpg'))
lvl_21.add(Task(text='А сколько у одной пчелки крылышек?', answer='2', image='pic/4.jpg'))
lvl_21.add(Task(text='Сколько же у них всего крыльев?', answer='12', image='pic/4.jpg'))
lvl_21.add(Task(text='А сколько на этой картинке цветов?', answer='3', image='pic/4.jpg'))

lvl_31 = Level(1, info='Быстро ты! Давай сравнивать группы.')
lvl_31.add(
    Task(text='Где предметов больше: слева и справа?', choice=['Слева', 'Справа'], answer='Слева', image='pic/5.jpg'))
lvl_31.add(Task(text='Каких мишек больше?', choice=['Бурых', 'Белых'], answer='Бурых', image='pic/6.jpg'))
lvl_31.add(Task(text='Чего больше: шляп или конфет?', choice=['Шляп', 'Конфет', "Поровну"], answer='Конфет',
                image='pic/7.jpg'))
lvl_31.add(Task(text='Чего больше: снежинок или лягушек?', choice=['Лягушек', 'Снежинок', "Поровну"], answer='Поровну',
                image='pic/7.jpg'))

lvl_41 = Level(1, info='Добро пожаловать! Продолжим наше занятие')
lvl_41.add(Task(text='Свеклы больше, меньше или равно?', choice=['Больше', 'Меньше', 'Равно'], answer='Равно',
                image='pic/8.jpg'))
lvl_41.add(Task(text='Морковки больше, меньше или равно?', choice=['Больше', 'Меньше', 'Равно'], answer='Равно',
                image='pic/9.jpg'))
lvl_41.add(Task(text='Лука больше, меньше или равно?', choice=['Больше', 'Меньше', 'Равно'], answer='Больше',
                image='pic/10.jpg'))
lvl_41.add(Task(text='Желудей больше, меньше или равно по сравнению с клубникой?', choice=['Больше', 'Меньше', 'Равно'],
                answer='Меньше', image='11.jpg'))

lvl_51 = Level(1, info='Отлично, а теперь блиц')
lvl_51.add(Task(text='Кто больше: волк или жук?', choice=['Волк', 'Жук', 'Похожие по размеру'], answer='Волк'))
lvl_51.add(Task(text='А что выше: светофор или дом?', choice=['Дом', 'Светофор', 'Похожие по размеру'], answer='Дом'))
lvl_51.add(Task(text='Кто умнее: филин или кабан?', choice=['Кабан', 'Филин', 'Похожие по уму'], answer='Филин'))

lvl_61 = Level(1, info='Уже неплохо получается! Давай займемся пространством')
lvl_61.add(Task(text='Как мальчику дойти до школы?', choice=['Пойти направо', 'Пойти налево', 'Пойти вперёд'],
                answer='Пойти направо', image='pic/12.jpg'))
lvl_61.add(Task(text='А как дойти до кинотеатра?', choice=['Пойти направо', 'Пойти налево', 'Пойти вперёд'],
                answer='Пойти налево', image='pic/12.jpg'))
lvl_61.add(Task(text='Сколько цветов справа от мальчика?', answer='2', image='pic/12.jpg'))
lvl_61.add(Task(text='А сколько слева от мальчика?', answer='3', image='pic/12.jpg'))

lvl_71 = Level(1, info='Посмотри какой красивый зайчик!')
lvl_71.add(Task(text='Что он сделал первым делом?', choice=['Поел', 'Проснулся', 'Сделал зарядку', "Пошёл в школу"],
                answer='Проснулся', image='pic/13.jpg'))
lvl_71.add(Task(text='Что он сделал потом?', choice=['Поел', 'Проснулся', 'Сделал зарядку', "Пошёл в школу"],
                answer='Сделал зарядку', image='pic/13.jpg'))
lvl_71.add(
    Task(text='Какое было его последнее действие?', choice=['Поесть', 'Проснуться', 'Сделать зарядку', "Пойти в школу"],
         answer='Пойти в школу', image='pic/13.jpg'))
lvl_71.add(Task(text='А всего было действий?', answer='5', image='pic/13.jpg'))

lvl_81 = Level(1, info='Все знают сказку про колобка!')
lvl_81.add(Task(text='Кого он встретил первым?', choice=['Лису', 'Бабушку с дедушкой', 'Волка', "Зайца"],
                answer='Бабушку с дедушкой'))
lvl_81.add(
    Task(text='А потом он с кем встретился?', choice=['С лисой', 'С медведем', 'Волка', "Зайца"], answer='С зайцем'))
lvl_81.add(Task(text='На ком же закончился его путь?', choice=['Лиса', 'Бабушка с дедушкой', 'Волк', "Медведь"],
                answer='Лиса'))
lvl_81.add(Task(text='А кто был самым маленьким героем этой сказки?', choice=['Лиса', 'Колобок', 'Заяц', "Медведь"],
                answer='Колобок'))

lvl_91 = Level(1, info='Рассмотрим картинку')
lvl_91.add(Task(text='В первом случае яблоко лежит', choice=['Под стулом', 'Около стула', 'За стулом', "Перед стулом"],
                answer='Перед стулом', image='pic/14.jpg'))
lvl_91.add(
    Task(text='А на третьей картинке яблоко лежит', choice=['Под стулом', 'Около стула', 'За стулом', "На стуле"],
         answer='Около стула', image='pic/14.jpg'))
lvl_91.add(
    Task(text='А на пятой картинке где оно лежит?', choice=['Под стулом', 'Около стула', 'За стулом', "На стуле"],
         answer='Под стулом', image='pic/14.jpg'))

lvl_101 = Level(1, info='Рассмотрим картинку', style='test', time=60, topic='Счет предметов. Сравнение групп предметов. Пространственные и временные представления.')
lvl_101.add(Task(text='Сколько на картинке зонтиков?', answer='4', image='pic/16.jpg'))
lvl_101.add(Task(text='А батонов тут сколько?', answer='6', image='pic/16.jpg'))
lvl_101.add(Task(text='Хорошо, а чего больше: карандашей или снежинок?', choice=['Снежинок', 'Карандашей', 'Поровну'],
                 answer='Снежинок', image='pic/16.jpg'))
lvl_101.add(Task(text='А что больше по размеру: дом или зонтик?', choice=['Дом', 'Зонтик', 'Похожие'], answer='Дом',
                 image='pic/16.jpg'))
lvl_101.add(Task(text='Рассмотрим новую картинку. Где дети старше?', choice=['Слева', 'По краям', 'В центре'],
                 answer='Снежинок', image='pic/15.jpg'))
lvl_101.add(Task(text='Кто выше: мальчик в кепке или девочка с каре?', choice=['Девочка', 'Мальчик', 'Одного роста'],
                 answer='Мальчик', image='pic/15.jpg'))
lvl_101.add(Task(text='А у кого из них самые длинные брюки?',
                 choice=['Он стоит крайним', 'Он стоит справа от мальчика в кепке', 'Он слева от мальчика в кепке',
                         "У нее хвостик", "Он носит кепку"], answer='Он слева от мальчика в кепке', image='pic/15.jpg'))
lvl_101.add(Task(text='А у кого из девочек самая коротка стрижка?',
                 choice=['Она по центру', 'Она крайняя', 'Справа от нее стоит девочка', "Слева от нее мальчик"],
                 answer='Она крайняя', image='pic/15.jpg'))


# тема 2
second_topic = Topic('Понятия «много», «один», «длиннее», «короче», «одинаковые по длине».')

lvl_12 = Level(1, info='Определи размер предметов и ответь на вопросы')
lvl_12.add(Task(text='Какая палочка самая длинная?', choice=['1', '2', '3'], answer='3', image='pic/18.jpg'))
lvl_12.add(Task(text='Какая морковка самая короткая?', choice=['1', '2', '3'], answer='1', image='pic/18.jpg'))

lvl_22 = Level(1, info="Определи на каком месте?")
lvl_22.add(Task(text="На каом месте четвертая по размеру гусиница?", choice=['1', '2', '3', '4', '5'], answer='3',
                image='pic/21.jpg'))

lvl_32 = Level(1, info='какой предмет толще ?')
lvl_32.add(Task(text="какой ствол толще?", choice=['правый', 'лелый'], answer='левый', image='pic/22.jpg'))
lvl_32.add(Task(text="Какая морковка толще?", choice=['правая', 'левая'], answer='правая', image="pic/23.jpg"))

lvl_32 = Level(1, info='одинаковые ли длинны?')
lvl_32.add(
    Task(text="Есть ли на картинке ленточки одинаковой длинны", choice=['нет', 'да'], answer='да', image='pic/23.jpg'))
lvl_32.add(Task(text="Все ли линии одиноковые по длинне?", choice=['да', 'нет'], answer='нет', image="pic/25.jpg"))



lvl_42 = Level(1, info='Рассмотрим картинку', style='test', time=60, topic='Сравнение предметов по форме(длинна толщина).')
lvl_42.add(Task(text="какая палочка самая длинная?", choice=['зеланая', 'синяя', 'крассная'], answer='Крассная',
                image='pic/25.jpg'))
lvl_42.add(
    Task(text="А какая самая короткая ?", choice=['зеланая', 'синяя', 'крассная'], answer='нет', image="pic/25.jpg"))
lvl_42.add(Task(text="Чего больше перцев или морковок?", choice=['морковок', 'перцев', 'одинакого'], answer='Одинокого',
                image='pic/9.jpg'))
lvl_42.add(Task(text="Какая палочка между длинной и короткой", choice=['2', '3', '1'], answer='2', image="pic/18.jpg"))
lvl_42.add(Task(text="под каким номером самая кароткая гусеница?", answer='2', image='pic/21.jpg'))
lvl_42.add(
    Task(text="Есть ли на картинке предметы одиниковой длинны?", choice=['нет', 'да'], answer='да', image="pic/17.jpg"))

# тема 3
third_topic = Topic('Знаки «+», «-». Состав числа 5 из двухслагаемых.')

lvl_13 = Level(1, info='Знаки «+», «-»')
lvl_13.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_13.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_13.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))
lvl_13.add(Task(text='Выберите знак', choice=['+', '-'], answer='-', image='pic/29.jpg'))
lvl_13.add(Task(text='Ну и последний раз', choice=['+', '-'], answer='+', image='pic/30.jpg'))

lvl_23 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_23.add(Task(text='Какую цифру нужно постаивть?', answer='2', image='pic/31.jpg'))
lvl_23.add(Task(text='Что нужно поставить ?', answer='1', image='pic/32.jpg'))
lvl_23.add(Task(text='', answer='1', image='pic/33.jpg'))
lvl_23.add(Task(text='Ну и последний раз', answer='5', image='pic/34.jpg'))

lvl_33 = Level(1, info='Рассмотрим картинку', style='test', time=60, topic='Раставить знаки и числа в пропуски.')
lvl_33.add(Task(text='Какую цифру нужно постаивть?', answer='2', image='pic/31.jpg'))
lvl_33.add(Task(text='Что нужно поставить ?', answer='1', image='pic/32.jpg'))
lvl_33.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_33.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_33.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))

# тема 4
four_topic = Topic('Знаки «<», «>», «=». Равенство. Неравенство')

lvl_14 = Level(1, info='Знаки «<», «>», «=».')
lvl_14.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/35.jpg'))
lvl_14.add(Task(text='', choice=['<', '>', '='], answer='>', image='pic/36.jpg'))
lvl_14.add(Task(text='', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))
lvl_14.add(Task(text='', choice=['<', '>', '='], answer='<', image='pic/38.jpg'))
lvl_14.add(Task(text='', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))


lvl_24 = Level(1, info='Рассмотрим картинку', style='test', time=40, topic='Раставить знаки в пропуски.')
lvl_24.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_24.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/36.jpg'))
lvl_24.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))
lvl_24.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='<', image='pic/39.jpg'))
lvl_24.add(Task(text='какой знак нужно поставить?', choice=['<', '>', '='], answer='>', image='pic/37.jpg'))

# тема 4

