from flask import render_template, redirect
import flask
from app.forms.change_avatar_Form import ChangeAvatarForm
from app.data import db_session
from app.data.users import Info

blueprint = flask.Blueprint(
    'changeavatar_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/change_avatar/key=<rdm_string>', methods=['GET', 'POST'])
def choice_class(rdm_string):
    form = ChangeAvatarForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()
    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()

    if form.submit1.data:
        user_info.avatar_href = 'https://i.ibb.co/C2WLdyY/avatar1.png'
        db_sess.commit()

    if form.submit2.data:
        user_info.avatar_href = 'https://i.ibb.co/0t3JTMz/avatar2.png'
        db_sess.commit()

    if form.submit3.data:
        user_info.avatar_href = 'https://i.ibb.co/K08BjJx/avatar3.png'
        db_sess.commit()

    if form.submit4.data:
        user_info.avatar_href = 'https://i.ibb.co/6XW1X2L/avatar4.png'
        db_sess.commit()

    if form.submit5.data:
        user_info.avatar_href = 'https://i.ibb.co/DVfTxB2/avatar5.png'
        db_sess.commit()

    if form.submit6.data:
        user_info.avatar_href = 'https://i.ibb.co/Bzvqgg3/avatar6.png'
        db_sess.commit()

    if form.submit7.data:
        user_info.avatar_href = 'https://i.ibb.co/FDg3t8m/avatar7.png'
        db_sess.commit()

    if form.back.data:
        db_sess.close()
        return redirect(f"/key={rdm_string}")

    return render_template("avatar.html", form=form, rdm_string=rdm_string)
