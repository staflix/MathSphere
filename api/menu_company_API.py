from flask import render_template, request, jsonify, redirect
import flask
from forms.menu_company_Form import MenuCompanyForm
from flask_login import current_user
from forms.mainpageForm import LogMainPageForm
from data import db_session
from data.users import Info
from company.company_second_class import *
from company.company_first_class import *
from company.company_third_class import *
from company.company_fourth_class import *

blueprint = flask.Blueprint(
    'menu_company_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/menu_company', methods=['GET', 'POST'])
def menu_company():
    form = MenuCompanyForm()
    profile = LogMainPageForm()
    page = 'company'

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.user_id == current_user.id).first()
    user_name = current_user.name
    user_surname = current_user.surname
    user_email = current_user.email
    user_avatar = f"../{user_info.avatar_href}"
    next_level = request.args.get('next_level')

    if next_level:
        if int(current_user.profile_level) <= user_info.current_level:
            current_user.profile_level = int(user_info.current_level) + 1
            db_sess.commit()

    level = current_user.profile_level
    db_sess.commit()
    db_sess.close()

    if request.method == 'POST':
        if profile.settings.data:
            return redirect(f"/settings?next={page}")

        if profile.change_avatar.data:
            return redirect(f"/change_avatar?next={page}")

        if profile.exit.data:
            return redirect(f"/logout")

        if request.is_json:
            data = request.get_json()
            level_selected = data.get('level')

            if 1 <= int(level_selected) <= 100:
                info_level, topic_level = get_level_info(year_1, level_selected)

            elif 101 <= int(level_selected) <= 200:
                info_level, topic_level = get_level_info(year_2, level_selected)

            elif 201 <= int(level_selected) <= 300:
                info_level, topic_level = get_level_info(year_3, level_selected)

            elif 301 <= int(level_selected) <= 400:
                info_level, topic_level = get_level_info(year_4, level_selected)

            return jsonify({
                'levelNumber': f'{level_selected}',
                'levelIntro': f'{info_level}',
                'levelTheme': f'{topic_level}'
            })

    return render_template("company.html", form=form, level=level, profile=profile,
                           avatar=user_avatar, name=user_name, surname=user_surname,
                           email=user_email, page=page)


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
