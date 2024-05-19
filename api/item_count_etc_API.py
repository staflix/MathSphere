from flask import render_template, session
import flask
from forms.item_count_etc_Form import ItemCountEtcForm
from data.tools import dictionary_trainer
from random import choice

blueprint = flask.Blueprint(
    'itemcountetc_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/<int:num_class>/<topic>/key=<rdm_string>', methods=['GET', 'POST'])
def item_count_etc(num_class, topic, rdm_string):
    form = ItemCountEtcForm()

    # Проверяем, есть ли текущее задание в сессии
    if 'current_task' not in session:
        # Если нет, выбираем новое задание
        task = choice(dictionary_trainer["Class"][num_class][topic])
        session['current_task'] = task
    else:
        # Если есть, используем сохраненное задание
        task = session['current_task']

    answer = task["answer"]
    count_images = task["count_images"]
    img_path = task["image"]
    text = task["text"]

    print(answer)

    if form.check.data:
        if float(answer) == float(form.answer_text.data):
            # Если ответ правильный, удаляем текущее задание из сессии
            session.pop('current_task', None)
            return render_template("item_count_etc.html", form=form, text=text, answer=answer,
                                   count_images=count_images, img_path=img_path, message_type="next",
                                   message='Ты красава все верно!!!', rdm_string=rdm_string)
        else:
            return render_template("item_count_etc.html", form=form, text=text,
                                   answer=answer, count_images=count_images, img_path=img_path, message_type="check",
                                   message='Неверно', rdm_string=rdm_string)

    return render_template("item_count_etc.html", form=form, text=text, answer=answer,
                           count_images=count_images, img_path=img_path, message_type="check", rdm_string=rdm_string)
