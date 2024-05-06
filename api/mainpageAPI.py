from flask import render_template, redirect
from forms.mainpageForm import MainPageForm
from flask_login import login_user
from data import db_session
from data.users import User, Info
import flask

blueprint = flask.Blueprint(
    'main_page_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/', methods=['GET', 'POST'])
def main_page_unlog():
    form = MainPageForm()
    return render_template('index.html', form=form)


@blueprint.route('/key=<rdm_string>', methods=['GET', 'POST'])
def main_page_log(rdm_string):
    form = MainPageForm()
    return render_template('index.html', form=form)
