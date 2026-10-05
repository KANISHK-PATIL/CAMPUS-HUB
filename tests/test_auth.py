from tests.conftest import login

def test_register(client):
    r=client.post('/register',data={'name':'New User','email':'new@test.local','password':'Password123'},follow_redirects=True); assert r.status_code==200; assert b'Welcome back' in r.data

def test_invalid_login(client):
    r=client.post('/login',data={'email':'bad@test.local','password':'wrong'}); assert r.status_code==200; assert b'Invalid email or password' in r.data

def test_logout(client,student):
    login(client); r=client.post('/logout',follow_redirects=True); assert r.status_code==200; assert b'logged out' in r.data
