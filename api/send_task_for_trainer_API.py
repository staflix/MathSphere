from flask import render_template, request
import flask
from forms.trainer_class_Form import TrainerClassForm
from generator.generate import generate

blueprint = flask.Blueprint(
    'send_task_for_trainer_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/<int:num_class>/<topic>', methods=['GET', 'POST'])
def send_task_for_trainer(num_class, topic):
    form = TrainerClassForm()
    task = generate(num_class, topic)
    text = task.task
    answer = task.answer

    minutes = request.form.get('minutes', 0, type=int)
    seconds = request.form.get('seconds', 0, type=int)
    correct_answers = request.form.get('correct_answers', 0, type=int)
    total_questions = request.form.get('total_questions', 0, type=int)

    if topic == 'Многоугольники' or topic == 'Счет предметов':
        path_img = task.image[0]
        count_img = len(task.image)
        if str(path_img)[0] not in '1234567890':
            path_img = f'{path_img.split(".")[0]}{count_img}.png'
    else:
        path_img = None
        count_img = 0

    return render_template("task_trainer.html", text=text, answer=answer, path_img=path_img, topic=topic,
                           count_img=count_img, num_class=num_class, form=form,
                           minutes=minutes, seconds=seconds, correct_answers=correct_answers,
                           total_questions=total_questions)
