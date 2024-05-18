from flask import render_template, request, jsonify, redirect
import flask
from app.forms.menu_company_Form import MenuCompanyForm
from app.forms.company_levelForm import CompanyLevelForm
from app.data import db_session
from app.data.users import User, Info
from app.company.company_creator import *

blueprint = flask.Blueprint(
    'menu_company_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/menu_company/key=<rdm_string>', methods=['GET', 'POST'])
def menu_company(rdm_string):
    form = MenuCompanyForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()
    level = user.profile_level
    db_sess.commit()
    db_sess.close()

    if request.method == 'POST' and request.is_json:
        data = request.get_json()
        level_selected = data.get('level')

        if level_selected == "1":
            text = "уровень 1"
            topic = "хуйхуйхуй"
        elif level_selected == "2":
            text = "уровень 2"
            topic = "хуйхухйухй"

        return jsonify({
            'levelIntro': f'Предисловие к уровню: {text}',
            'levelTheme': f'Тема уровня: {topic}'
        })

    return render_template("company.html", form=form, level=level, rdm_string=rdm_string)
