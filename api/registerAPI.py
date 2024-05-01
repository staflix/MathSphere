from flask import render_template, redirect
import flask
from forms.registerForm import RegisterForm
from data import db_session
from data.users import User

blueprint = flask.Blueprint(
    'register_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.submit.data:
        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.surname = form.surname.data
        user.profile_level = 1
        user.email = form.email.data
        user.set_password(form.password.data)
        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='MathSphere', form=form)
