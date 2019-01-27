import pytest
from sofl import create_app

app = create_app('testing')
client = app.test_client()

def test_client_works():
    response = client.get('/nonexistent_endpoint')
    assert response.status_code == 404

def test_signup():
    response = client.post('/auth/signup', data = {
        'username': app.config['USERNAME'],
        'password': app.config['PASSWORD']
        })
    assert 'Successful signup!' in response.data

def test_login():
    response = client.post('/auth/login', data = {
        'username': app.config['USERNAME'],
        'password': app.config['PASSWORD']
        })
    assert 'Successful login!' in response.data

def test_logout():
    response = client.post('/auth/logout')
    assert 'Successful logout!' in response.data

if __name__ == '__main__':
	pytest.main()