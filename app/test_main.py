import pytest
from app.main import app

@pytest.fixture
def client():
    return app.test_client()

def test_health_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"VPP-UNIT-DE-01" in response.data