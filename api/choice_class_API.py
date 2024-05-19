from flask import render_template, redirect
import flask
from forms.choice_class_Form import ChoiceClassForm

blueprint = flask.Blueprint(
    'choiceclass_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/choice_class/key=<rdm_string>', methods=['GET', 'POST'])
def choice_class(rdm_string):
    form = ChoiceClassForm()

    if form.first_class.data:
        return redirect(f"/1/key={rdm_string}")

    elif form.second_class.data:
        return redirect(f"/2/key={rdm_string}")

    elif form.third_class.data:
        return redirect(f"/3/key={rdm_string}")

    elif form.fourth_class.data:
        return redirect(f"/4/key={rdm_string}")

    return render_template("choice_class.html", form=form, rdm_string=rdm_string)
