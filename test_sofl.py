import pytest
from sofl import create_app

app = create_app('testing')
client = app.test_client()

def test_client_works():
    response = client.get('/nonexistent_endpoint')
    assert response.status_code == 404

def signup(client, username, password):
    return client.post('/auth/signup', data = {
        'username': username,
        'password': password
        }, follow_redirects = True)

def login(client, username, password):
    return client.post('/login', data = {
        'username': username,
        'password', password
        }, follow_redirects = True)

def logout(client):
    return client.post('/logout', follow_redirects = True)

def test_signup(client):
    response = signup(client, app.config['USERNAME'], app.config['PASSWORD'])
    assert 'Successful signup!' in response.data

def test_login(clinet):
    response = login(client, app.config['USERNAME'], app.config['PASSWORD'])
    assert 'Successful login!' in response.data

def test_logout(client):
    response = logout(client)
    assert 'Successful logout!' in response.data

if __name__ == '__main__':
	pytest.main()