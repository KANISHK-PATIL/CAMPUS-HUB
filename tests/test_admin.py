from tests.conftest import login

def test_student_cannot_access_admin(client,student):
    login(client);assert client.get('/admin').status_code==403

def test_admin_can_create_announcement_and_resource(client,admin):
    login(client,'admin@test.local')
    assert client.post('/admin/announcements',data={'title':'Exam','content':'Exam soon','category':'Exam','priority':'Important'}).status_code==302
    assert client.post('/admin/resources',data={'title':'Docs','description':'Docs','subject':'Python','resource_type':'Documentation','url':'https://docs.python.org/3/'}).status_code==302
