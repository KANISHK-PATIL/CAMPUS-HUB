from functools import wraps
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app.extensions import db
from app.models import User, Task, Resource, Announcement
from app.utils.validation import limited, valid_url

admin_bp=Blueprint('admin',__name__,url_prefix='/admin')

def admin_required(fn):
    @wraps(fn)
    @login_required
    def wrapped(*args,**kwargs):
        if current_user.role!='admin': return render_template('error.html',code=403,message='Admin access required.'),403
        return fn(*args,**kwargs)
    return wrapped

@admin_bp.get('')
@admin_required
def dashboard():
    return render_template('admin.html',students=User.query.filter_by(role='student').count(),tasks=Task.query.count(),announcements=Announcement.query.count(),resources=Resource.query.count(),users=User.query.order_by(User.joined_at.desc()).limit(8).all(),recent_resources=Resource.query.order_by(Resource.created_at.desc()).limit(8).all(),recent_announcements=Announcement.query.order_by(Announcement.created_at.desc()).limit(5).all())

@admin_bp.route('/announcements',methods=['POST'])
@admin_required
def create_announcement():
    try:
        a=Announcement(title=limited(request.form.get('title'),150),content=limited(request.form.get('content'),5000),category=limited(request.form.get('category'),30),priority=limited(request.form.get('priority'),20))
        db.session.add(a);db.session.commit();flash('Announcement created.','success')
    except ValueError as e:flash(str(e),'error')
    return redirect(url_for('admin.dashboard'))

@admin_bp.post('/announcements/<int:item_id>/edit')
@admin_required
def edit_announcement(item_id):
    a=db.session.get(Announcement,item_id)
    if not a: flash('Announcement not found.','error'); return redirect(url_for('admin.dashboard'))
    try:
        a.title=limited(request.form.get('title'),150); a.content=limited(request.form.get('content'),5000); a.category=limited(request.form.get('category'),30); a.priority=limited(request.form.get('priority'),20)
        db.session.commit(); flash('Announcement updated.','success')
    except ValueError as e: flash(str(e),'error')
    return redirect(url_for('admin.dashboard'))

@admin_bp.post('/announcements/<int:item_id>/delete')
@admin_required
def delete_announcement(item_id):
    a=db.session.get(Announcement,item_id)
    if a:db.session.delete(a);db.session.commit();flash('Announcement deleted.','success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/resources',methods=['POST'])
@admin_required
def create_resource():
    try:
        url=limited(request.form.get('url'),500)
        if not valid_url(url): raise ValueError('Enter a valid http/https URL.')
        r=Resource(title=limited(request.form.get('title'),150),description=limited(request.form.get('description'),2000,False),subject=limited(request.form.get('subject'),100,False),resource_type=limited(request.form.get('resource_type'),30),url=url,added_by=current_user.id)
        db.session.add(r);db.session.commit();flash('Resource added.','success')
    except ValueError as e:flash(str(e),'error')
    return redirect(url_for('admin.dashboard'))

@admin_bp.post('/resources/<int:item_id>/edit')
@admin_required
def edit_resource(item_id):
    r=db.session.get(Resource,item_id)
    if not r: flash('Resource not found.','error'); return redirect(url_for('admin.dashboard'))
    try:
        url=limited(request.form.get('url'),500)
        if not valid_url(url): raise ValueError('Enter a valid http/https URL.')
        r.title=limited(request.form.get('title'),150); r.description=limited(request.form.get('description'),2000,False); r.subject=limited(request.form.get('subject'),100,False); r.resource_type=limited(request.form.get('resource_type'),30); r.url=url
        db.session.commit(); flash('Resource updated.','success')
    except ValueError as e: flash(str(e),'error')
    return redirect(url_for('admin.dashboard'))

@admin_bp.post('/resources/<int:item_id>/delete')
@admin_required
def delete_resource(item_id):
    r=db.session.get(Resource,item_id)
    if r:db.session.delete(r);db.session.commit();flash('Resource deleted.','success')
    return redirect(url_for('admin.dashboard'))
