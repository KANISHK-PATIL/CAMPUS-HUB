from tests.conftest import login

def test_notes_crud(client,student):
    login(client);r=client.post('/api/notes',json={'title':'CN','content':'OSI layers','subject':'CN'});assert r.status_code==201;n=r.get_json()['data'];nid=n['id']
    assert client.put(f'/api/notes/{nid}',json={'title':'CN Updated','content':'TCP UDP','subject':'CN'}).status_code==200
    assert client.get('/api/notes').status_code==200
    assert client.delete(f'/api/notes/{nid}').status_code==200
