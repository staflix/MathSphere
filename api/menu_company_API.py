from flask import render_template, request, jsonify, redirect
import flask
from forms.menu_company_Form import MenuCompanyForm
from forms.company_levelForm import CompanyLevelForm
from forms.mainpageForm import LogMainPageForm
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
    profile = LogMainPageForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()
    user_name = user.name
    user_surname = user.surname
    user_email = user.email
    user_avatar = f"../{user_info.avatar_href}"
    # user.profile_level = 200
    level = user.profile_level
    db_sess.commit()
    db_sess.close()

    if request.method == 'POST':
        data = request.get_json()
        level_selected = data.get('level')

        # if 1 <= level_selected <= 100:
        #     info_level, topic_level = get_level_info(year_1, level_selected)

        if 101 <= int(level_selected) <= 200:
            info_level, topic_level = get_level_info(year_2, level_selected)

        # elif 201 <= level_selected <= 300:
        #     info_level, topic_level = get_level_info(year_3, level_selected)
        #
        # elif 301 <= level_selected <= 400:
        #     info_level, topic_level = get_level_info(year_4, level_selected)

        return jsonify({
            'levelNumber': f'{level_selected}',
            'levelIntro': f'{info_level}',
            'levelTheme': f'{topic_level}'
        })
    return render_template("company.html", form=form, level=level, rdm_string=rdm_string, profile=profile,
                           avatar=user_avatar, name=user_name, surname=user_surname,
                           email=user_email)


def get_level_info(year, level_selected):
    topic_index = int(level_selected) // 10 % 10
    level_within_topic_index = (int(level_selected) - 1) % 10
    if int(level_selected) % 10 == 0 and int(level_selected) % 100 != 0:
        topic_index -= 1

    elif int(level_selected) % 10 == 0 and int(level_selected) % 100 == 0:
        topic_index = 9

    selected_topic = year.topics[topic_index]
    selected_level = selected_topic.levels[level_within_topic_index]

    info_level = selected_level.name
    topic_level = selected_topic.name

    return info_level, topic_level
