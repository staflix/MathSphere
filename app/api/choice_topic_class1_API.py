from flask import render_template, redirect
import flask
from app.forms.choice_topic_class1_Form import ChoiceTopicClass1Form

blueprint = flask.Blueprint(
    'choicetopicclass1_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/<int:num_class>/key=<rdm_string>', methods=['GET', 'POST'])
def choice_topic_class1(num_class, rdm_string):
    form = ChoiceTopicClass1Form()

    if form.item_count_etc.data:
        topic = "Счет предметов. Сравнение групп предметов. Пространственные и временные представления."
        return redirect(f"/{num_class}/{topic}/key={rdm_string}")

    return render_template("choice_topic.html", num_class=num_class, form=form, rdm_string=rdm_string)
