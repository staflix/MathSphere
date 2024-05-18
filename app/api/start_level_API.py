from flask import render_template, request, redirect
import flask
from app.forms.company_levelForm import CompanyLevelForm
from app.data import db_session
from app.data.users import User, Info
from app.company.company_creator import *

blueprint = flask.Blueprint(
    'start_level_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/start_level/<level>/key=<rdm_string>', methods=['GET', 'POST'])
def start_level(level, rdm_string):
    form = CompanyLevelForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()

    db_sess.close()

    if request.method == 'POST' and form.validate_on_submit():
        if form.leave.data:
            return redirect(f'/menu_company/key={rdm_string}')

    if level == "1":
        timer = None
        return render_template("level.html", timer=timer, form=form)
