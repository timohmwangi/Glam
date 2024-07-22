from flask import (
    render_template, abort, flash, url_for, 
    current_app, get_flashed_messages, send_file, 
    send_from_directory, jsonify, make_response, 
    redirect, request, session
)
from flask_login import (
    current_user, login_required, login_user, logout_user
)

from . import blueprint
from .forms import LoginForm
from ..models import Users, Client, Spa
# from ..extensions import login_manager


from ..main.forms import ClientForm
from ..config import Config

@blueprint.before_app_request
def check_admin_reg():
    """
    """
    if not Spa.query.first():
        spa_phone = Config.ADMIN_TEL
        spa_name = 'Glam SPa'
        password = Config.ADMIN_TEL
        spa = Spa(phone_number=spa_phone, name=spa_name,)
        spa.set_password(password)
        spa.save()

@blueprint.route('/login', methods=["GET", "POST"])
def login():
    """
    """
    if current_user and current_user.is_authenticated:
        flash('You are currently logged in to your account.', 'primary')
        return redirect(url_for(f'{current_user.type}.dashboard'))
    context = {
        "title": 'Login Page'
    }
    form = LoginForm()
    context["form"] = form
    if form.validate_on_submit():
        user = Users.query.filter_by(phone_number=form.phone_number.data).first()
        if user.type == 'client':
            user = user.client.scalar()
        elif user.type == 'employee':
            user = user.employee.scalar()
        else:
            user = user.spa.scalar()
        print(user, request.args.get('next'))
        if user.check_password(form.password.data) and login_user(user, form.remember_me.data, force=True):
            if user.type == "spa":
                flash(f'Welcome {user.name}', 'success')
            else:
                flash(f'Welcome {user.first_name}', 'success')
            if request.args.get("next"):
                return redirect(request.args.get("next"))
            return redirect(url_for(f'{user.type}.dashboard'))
        flash('Invalid phone number or password.', 'danger')
    login_page = render_template('auth/login.html', **context)
    return make_response(login_page)


@blueprint.route('/register', methods=["GET", "POST"])
def register():
    """
    """
    if current_user and current_user.is_authenticated:
        flash('You are currently logged in to your account.', 'primary')
        return redirect(url_for(f'{current_user.type}.dashboard'))
    
    context = {
        "title": 'Login Page'
    }
    form = ClientForm()
    context["form"] = form
    if form.validate_on_submit():
        user = Client()
        form.populate_obj(user)
        user.set_password(form.password_hash.data)
        new_user = user.save()
        print(new_user)
        if new_user:        
            flash(f'{new_user.first_name} {new_user.last_name} has been successfully registered.', 'success')
            return redirect(url_for('auth.login'))
        flash('There was an error in saving the user.', 'warning')
    login_page = render_template('auth/register.html', **context)
    return make_response(login_page)


@blueprint.route('/logout')
@login_required
def logout():
    """
    """
    logout_user()
    return redirect(url_for('main.home'))

