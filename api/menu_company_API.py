from flask import render_template, request, jsonify, redirect
import flask
from forms.menu_company_Form import MenuCompanyForm
from forms.company_levelForm import CompanyLevelForm
from data import db_session
from data.users import User, Info
from company.company_second_class import *

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


        elif level_selected == "101":
            info_level = year_2.topics[0].levels[0].name
            topic_level = year_2.topics[0].name

        elif level_selected == "102":
            info_level = year_2.topics[0].levels[1].name
            topic_level = year_2.topics[0].name

        elif level_selected == "103":
            info_level = year_2.topics[0].levels[2].name
            topic_level = year_2.topics[0].name

        elif level_selected == "104":
            info_level = year_2.topics[0].levels[3].name
            topic_level = year_2.topics[0].name

        elif level_selected == "105":
            info_level = year_2.topics[0].levels[4].name
            topic_level = year_2.topics[0].name

        elif level_selected == "106":
            info_level = year_2.topics[0].levels[5].name
            topic_level = year_2.topics[0].name

        elif level_selected == "107":
            info_level = year_2.topics[0].levels[6].name
            topic_level = year_2.topics[0].name

        elif level_selected == "108":
            info_level = year_2.topics[0].levels[7].name
            topic_level = year_2.topics[0].name

        elif level_selected == "109":
            info_level = year_2.topics[0].levels[8].name
            topic_level = year_2.topics[0].name

        elif level_selected == "110":
            info_level = year_2.topics[0].levels[9].name
            topic_level = year_2.topics[0].name

        elif level_selected == "111":
            info_level = year_2.topics[1].levels[0].name
            topic_level = year_2.topics[1].name

        elif level_selected == "112":
            info_level = year_2.topics[1].levels[1].name
            topic_level = year_2.topics[1].name

        elif level_selected == "113":
            info_level = year_2.topics[1].levels[2].name
            topic_level = year_2.topics[1].name

        elif level_selected == "114":
            info_level = year_2.topics[1].levels[3].name
            topic_level = year_2.topics[1].name

        elif level_selected == "115":
            info_level = year_2.topics[1].levels[4].name
            topic_level = year_2.topics[1].name

        elif level_selected == "116":
            info_level = year_2.topics[1].levels[5].name
            topic_level = year_2.topics[1].name

        elif level_selected == "117":
            info_level = year_2.topics[1].levels[6].name
            topic_level = year_2.topics[1].name

        elif level_selected == "118":
            info_level = year_2.topics[1].levels[7].name
            topic_level = year_2.topics[1].name

        elif level_selected == "119":
            info_level = year_2.topics[1].levels[8].name
            topic_level = year_2.topics[1].name

        elif level_selected == "120":
            info_level = year_2.topics[1].levels[9].name
            topic_level = year_2.topics[1].name

        return jsonify({
            'levelIntro': f'{info_level}',
            'levelTheme': f'Тема уровня: {topic_level}'
        })

    return render_template("company.html", form=form, level=level, rdm_string=rdm_string)
