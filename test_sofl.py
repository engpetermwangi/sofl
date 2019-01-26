import pytest
from sofl import create_app

app = create_app('testing')
client = app.test_client()

def test_client_works():
    response = client.get('/nonexistent_endpoint')
    assert response.status_code == 404

if __name__ == '__main__':
	pytest.main()