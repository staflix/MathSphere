from flask import render_template
import flask
import random
from forms.simplearithmeticForm import SimpleArithmeticForm
from data.tools import dictionary_trainer

blueprint = flask.Blueprint(
    'trainer_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/trainer/key=<rdm_string>', methods=['GET', 'POST'])
def trainer(rmd_string):
    return 'Тут выбор тем из карточек'
