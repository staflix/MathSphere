from flask import render_template, redirect, request, jsonify, url_for
import flask
from forms.change_avatar_Form import ChangeAvatarForm
from data import db_session
from flask_login import current_user
from data.users import Info

blueprint = flask.Blueprint(
    'change_avatar_API',
    __name__,
    template_folder='templates'
)


@blueprint.route('/change_avatar', methods=['GET', 'POST'])
def change_avatar():
    form = ChangeAvatarForm()
    next_page = request.args.get('next')

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()
    user_info = db_sess.query(Info).filter(Info.user_id == current_user.id).first()

    if request.method == 'POST':
        avatar = request.form.get('avatar')
        if avatar:
            user_info.avatar_href = f'static/avatars_img/{avatar}.png'
            db_sess.commit()
            db_sess.close()
            return jsonify(success=True, next=next_page)
        return jsonify(success=False)

    return render_template("avatar.html", form=form, next_page=next_page)
