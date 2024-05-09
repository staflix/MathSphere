from flask import render_template, redirect
from forms.mainpageForm import UnLogMainPageForm, LogMainPageForm
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
    form = UnLogMainPageForm()
    return render_template('unlog_index.html', form=form)


# главная страница для зарегестрированного пользователя
@blueprint.route('/key=<rdm_string>', methods=['GET', 'POST'])
def main_page_log(rdm_string):
    form = LogMainPageForm()
    return render_template('log_index.html', form=form)
