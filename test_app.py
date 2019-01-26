import pytest
from flask import Flask
from app import app

def test_app_instance():
    assert isinstance(app, Flask)

if __name__ == '__main__':
	pytest.main()