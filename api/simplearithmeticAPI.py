from flask import render_template
import flask
import random
from forms.simplearithmeticForm import SimpleArithmeticForm
from data.tools import main_dictionary

blueprint = flask.Blueprint(
    'simple_arithmetic_api',
    __name__,
    template_folder='templates'
)

flag, status, num1, num2, example, answer = True, None, None, None, None, None


@blueprint.route('/simple_arithmetic/<int:num_class>', methods=['GET', 'POST'])
def select_topic(num_class):
    topics = main_dictionary['classes'][num_class]
    if not topics:
        return render_template('select_topic.html', topics=topics,
                               message='тут будут темы для выбранного класса', selected_class=num_class)
    return render_template('select_topic.html', topics=topics, selected_class=num_class)


@blueprint.route('/simple_arithmetic/<topic>', methods=['GET', 'POST'])
def simple_arithmetic(topic):
    # тут есть класс, потом нужно сделать для какого класса какие темы и примеры для них
    global flag, status, num1, num2, example, answer
    form = SimpleArithmeticForm()
    if topic == 'addition':
        if flag:
            num1 = str(random.randint(1, 10))
            num2 = str(random.randint(1, 10))
            example = str(num1) + '+' + str(num2) + '=?'
            answer = float(eval(f'{num1} + {num2}'))
            status = 'Не решено'
            flag = False
        else:
            if status == 'Решено верно!':
                if form.next.data:
                    status = 'Не решено'
                    num1 = str(random.randint(1, 10))
                    num2 = str(random.randint(1, 10))
                    example = str(num1) + '+' + str(num2) + '=?'
                    answer = float(eval(f'{num1} + {num2}'))
        if form.check.data:
            if float(form.answer.data) == answer:
                status = 'Решено верно!'
                return render_template('simple_arithmetic.html', example=example, status=status,
                                       form=form, topic=topic)
            elif form.answer.data != answer:
                status = 'Решено неверно!'
                return render_template('simple_arithmetic.html', example=example, status=status,
                                       form=form, topic=topic)
        return render_template('simple_arithmetic.html', example=example, status=status,
                               form=form, topic=topic)
    else:
        return f'тут тема {topic}'
