from flask import render_template, redirect
import flask
from forms.choice_class_Form import ChoiceClassForm
from forms.mainpageForm import LogMainPageForm
from flask_login import current_user
from data import db_session
from data.users import Info, TrainerStatistics

blueprint = flask.Blueprint(
    'choiceclass_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/choice_class', methods=['GET', 'POST'])
def choice_class():
    form = ChoiceClassForm()
    profile = LogMainPageForm()

    page = 'choice_class'

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.user_id == current_user.id).first()
    user_name = current_user.name
    user_surname = current_user.surname
    user_email = current_user.email
    user_avatar = f"../{user_info.avatar_href}"

    class1 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                     1 == TrainerStatistics.num_class).all()
    class2 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                     2 == TrainerStatistics.num_class).all()
    class3 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                     3 == TrainerStatistics.num_class).all()
    class4 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                     4 == TrainerStatistics.num_class).all()

    def get_speed_accuracy_pairs(statistics):
        pairs = []
        for stat in statistics:
            speed = float(stat.speed) if stat.speed is not None else 0
            accuracy = float(stat.accuracy) if stat.accuracy is not None else 0
            topic = stat.topic
            pairs.append((speed, accuracy, topic))
        return pairs

    class1_pairs = get_speed_accuracy_pairs(class1)
    class2_pairs = get_speed_accuracy_pairs(class2)
    class3_pairs = get_speed_accuracy_pairs(class3)
    class4_pairs = get_speed_accuracy_pairs(class4)

    def find_best_and_worst_result(pairs):
        topic_bad = None
        topic_best = None
        max_value = float('-inf')
        min_value = float('inf')
        for speed, accuracy, topic in pairs:
            value = speed * accuracy
            if value > max_value:
                max_value = value
                topic_best = topic
            if value < min_value:
                min_value = value
                topic_bad = topic
        return topic_best, topic_bad

    best_result_class1, worst_result_class1 = find_best_and_worst_result(class1_pairs)
    best_result_class2, worst_result_class2 = find_best_and_worst_result(class2_pairs)
    best_result_class3, worst_result_class3 = find_best_and_worst_result(class3_pairs)
    best_result_class4, worst_result_class4 = find_best_and_worst_result(class4_pairs)

    db_sess.close()

    if form.first_class.data:
        return redirect(f"/1")

    if form.second_class.data:
        return redirect(f"/2")

    if form.third_class.data:
        return redirect(f"/3")

    if form.fourth_class.data:
        return redirect(f"/4")

    if profile.settings.data:
        return redirect(f"/settings?next={page}")

    if profile.change_avatar.data:
        return redirect(f"/change_avatar?next={page}")

    if profile.exit.data:
        return redirect(f"/logout")

    return render_template("choice_class.html", form=form, profile=profile,
                           avatar=user_avatar, name=user_name, surname=user_surname,
                           email=user_email,
                           best_result_class1=best_result_class1, worst_result_class1=worst_result_class1,
                           best_result_class2=best_result_class2, worst_result_class2=worst_result_class2,
                           best_result_class3=best_result_class3, worst_result_class3=worst_result_class3,
                           best_result_class4=best_result_class4, worst_result_class4=worst_result_class4)
