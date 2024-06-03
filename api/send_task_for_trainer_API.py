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

    if num_class == 1:
        if topic == 'Счет предметов':
            text = task.task
            answer = task.answer
            path_img = task.image[0]
            count_img = len(task.image)
            print(text)
            print(answer)
            print(path_img)
            print(count_img)

    return render_template("task_trainer.html", text=text, answer=answer, path_img=path_img,
                           count_img=count_img, rdm_string=rdm_string, num_class=num_class, form=form)
