import pytest
# This refers to the folder 'app' and the file 'main.py'
from app.main import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"VPP-UNIT-DE-01" in response.data