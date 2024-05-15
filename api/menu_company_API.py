from flask import render_template, redirect
import flask
from forms.menu_company_Form import MenuCompanyForm
from flask_login import login_user
from data import db_session
from data.users import User, Info

blueprint = flask.Blueprint(
    'menu_company_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/menu_company/key=<rdm_string>', methods=['GET', 'POST'])
def choice_class(rdm_string):
    form = MenuCompanyForm()

    return render_template("menu_company.html", form=form, rdm_string=rdm_string)
