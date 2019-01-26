import pytest
from flask import Flask
from app import create_app

app = create_app('testing')

def test_app_instance():
    assert isinstance(app, Flask)

client = app.test_client()

def test_client_works():
    response = client.get('/nonexistent_endpoint')
    assert response.status_code == 404

if __name__ == '__main__':
	pytest.main()