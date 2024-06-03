from flask import render_template, session
import flask
from forms.trainer_class_Form import TrainerClassForm
from data.tools import dictionary_trainer
from random import choice
from generator.generate import generate

blueprint = flask.Blueprint(
    'send_task_for_trainer_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/<int:num_class>/<topic>/key=<rdm_string>', methods=['GET', 'POST'])
def send_task_for_trainer(num_class, topic, rdm_string):
    form = TrainerClassForm()
    task = generate(num_class, topic)
    text = task.task
    answer = task.answer

    if topic == 'Многоугольники' or topic == 'Счет предметов':
        path_img = task.image[0]
        count_img = len(task.image)
        if str(path_img)[0] not in '1234567890':
            path_img = f'{path_img.split(".")[0]}{count_img}.png'
    else:
        path_img = None
        count_img = 0

    return render_template("task_trainer.html", text=text, answer=answer, path_img=path_img,
                           count_img=count_img, rdm_string=rdm_string, num_class=num_class, form=form)
