from flask import render_template
import flask
import random
from forms.simplearithmeticForm import SimpleArithmeticForm

blueprint = flask.Blueprint(
    'simple_arithmetic_api',
    __name__,
    template_folder='templates'
)

flag, status, num1, num2, example, answer = True, None, None, None, None, None


@blueprint.route('/simple_arithmetic', methods=['GET', 'POST'])
def simple_arithmetic():
    global flag, status, num1, num2, example, answer
    form = SimpleArithmeticForm()
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
            return render_template('simple_arithmetic.html', example=example, status=status, form=form)
        elif form.answer.data != answer:
            status = 'Решено неверно!'
            return render_template('simple_arithmetic.html', example=example, status=status, form=form)
    return render_template('simple_arithmetic.html', example=example, status=status, form=form)
