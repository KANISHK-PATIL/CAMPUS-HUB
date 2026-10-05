from datetime import date, timedelta
from app.extensions import db
from app.models import User, Task, Note, Resource, Announcement, Notification

def seed_database():
    if User.query.first(): return
    admin=User(name='Campus Admin',email='admin@campushub.local',role='admin',department='Administration',year='Staff'); admin.set_password('Admin@12345')
    student=User(name='Demo Student',email='student@campushub.local',role='student',department='Computer Science',year='2nd Year'); student.set_password('Student@12345')
    db.session.add_all([admin,student]);db.session.flush()
    db.session.add_all([
      Task(user_id=student.id,title='DBMS Assignment',description='Finish normalization questions.',priority='high',category='assignment',due_date=date.today()+timedelta(days=1)),
      Task(user_id=student.id,title='OS Revision',priority='medium',category='exam',due_date=date.today()+timedelta(days=4)),
      Task(user_id=student.id,title='Submit Lab Record',priority='low',category='personal',due_date=date.today()-timedelta(days=1),completed=True),
      Note(user_id=student.id,title='CN Quick Notes',content='OSI layers, TCP vs UDP, common ports.',subject='Computer Networks'),
      Note(user_id=student.id,title='DBMS Revision',content='Keys, normalization, joins and transactions.',subject='DBMS'),
      Resource(title='MDN Web Docs',description='Practical HTML, CSS and JavaScript documentation.',subject='Web Development',resource_type='Documentation',url='https://developer.mozilla.org/',added_by=admin.id),
      Resource(title='Python Official Tutorial',description='Official Python learning material.',subject='Python',resource_type='Course',url='https://docs.python.org/3/tutorial/',added_by=admin.id),
      Announcement(title='Mid-Sem Exam Schedule',content='Check the department notice board for the latest exam schedule.',category='Exam',priority='Important'),
      Announcement(title='Open Source Contribution Drive',content='Students can contribute to CampusHub during the college event.',category='Event',priority='Normal'),
      Notification(user_id=student.id,title='Welcome to CampusHub',message='Your demo workspace is ready.',kind='success')
    ]);db.session.commit()
