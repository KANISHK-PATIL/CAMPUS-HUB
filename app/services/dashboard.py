from datetime import date, timedelta
from sqlalchemy import func
from app.models import Task, Note, Announcement, Notification

def dashboard_stats(user):
    tasks=Task.query.filter_by(user_id=user.id)
    total=tasks.count(); completed=tasks.filter_by(completed=True).count(); pending=total-completed
    upcoming=tasks.filter(Task.completed.is_(False), Task.due_date.isnot(None), Task.due_date>=date.today()).order_by(Task.due_date.asc()).limit(5).all()
    recent_notes=Note.query.filter_by(user_id=user.id).order_by(Note.updated_at.desc()).limit(5).all()
    announcements=Announcement.query.order_by(Announcement.created_at.desc()).limit(5).all()
    productivity=round((completed/total)*100) if total else 0
    days=[date.today()-timedelta(days=i) for i in range(6,-1,-1)]
    daily=[]
    for day in days:
        count=tasks.filter(Task.completed.is_(True), func.date(Task.updated_at)==day.isoformat()).count()
        daily.append({'day':day.strftime('%a'),'count':count})
    return {'total':total,'completed':completed,'pending':pending,'productivity':productivity,'upcoming':upcoming,'recent_notes':recent_notes,'announcements':announcements,'daily':daily}

def generate_notifications(user):
    from app.extensions import db
    today=date.today(); tomorrow=today+timedelta(days=1)
    existing={(n.title,n.message) for n in user.notifications if n.created_at.date()==today}
    for task in user.tasks:
        if not task.completed and task.due_date:
            if task.due_date < today: title='Task overdue'; message=f'"{task.title}" is overdue.'; kind='warning'
            elif task.due_date == tomorrow: title='Task due tomorrow'; message=f'"{task.title}" is due tomorrow.'; kind='info'
            else: continue
            if (title,message) not in existing: db.session.add(Notification(user_id=user.id,title=title,message=message,kind=kind))
    db.session.commit()
