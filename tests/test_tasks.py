import json
from tests.conftest import login

def test_task_crud_and_ownership(client,student,app):
    login(client)
    r=client.post('/api/tasks',json={'title':'Study Flask','priority':'high','category':'exam','due_date':'2030-01-01'}); assert r.status_code==201; task=r.get_json()['data']; tid=task['id']
    assert client.get('/api/tasks').status_code==200
    assert client.put(f'/api/tasks/{tid}',json={'completed':True}).status_code==200
    assert client.delete(f'/api/tasks/{tid}').status_code==200

def test_protected_task_api(client):
    assert client.get('/api/tasks').status_code==401
