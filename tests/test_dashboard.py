from tests.conftest import login

def test_dashboard_stats(client,student):
    login(client);client.post('/api/tasks',json={'title':'One','completed':False});client.post('/api/tasks',json={'title':'Two'})
    data=client.get('/api/dashboard').get_json()['data'];assert data['total']==2;assert data['pending']==2;assert data['completed']==0;assert data['productivity']==0
