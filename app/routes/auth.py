from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from app.extensions import db
from app.models import User
from app.utils.validation import clean, valid_email, password_ok

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('main.dashboard'))
    if request.method == 'POST':
        email = clean(request.form.get('email','')).lower(); password = request.form.get('password','')
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            flash('Invalid email or password.', 'error')
        else:
            login_user(user)
            return redirect(url_for('admin.dashboard' if user.role == 'admin' else 'main.dashboard'))
    return render_template('auth.html', mode='login')

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated: return redirect(url_for('main.dashboard'))
    if request.method == 'POST':
        name=clean(request.form.get('name','')); email=clean(request.form.get('email','')).lower(); password=request.form.get('password','')
        department=clean(request.form.get('department','')); year=clean(request.form.get('year',''))
        if len(name)<2 or len(name)>80: flash('Name must be 2–80 characters.', 'error')
        elif not valid_email(email): flash('Enter a valid email address.', 'error')
        elif not password_ok(password): flash('Password must be at least 8 characters.', 'error')
        elif User.query.filter_by(email=email).first(): flash('An account with that email already exists.', 'error')
        else:
            user=User(name=name,email=email,department=department,year=year,role='student'); user.set_password(password)
            db.session.add(user); db.session.commit(); login_user(user)
            flash('Welcome to CampusHub!', 'success'); return redirect(url_for('main.dashboard'))
    return render_template('auth.html', mode='register')

@auth_bp.post('/logout')
def logout():
    logout_user(); flash('You have been logged out.', 'success'); return redirect(url_for('auth.login'))
