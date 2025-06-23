from app.api import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client  # Esto permite reutilizar el cliente en múltiples tests

def test_reserva_exitosa(client):
    response = client.post('/reservar', json={"sala": "B", "hora": "14:00"})
    assert response.status_code == 201
    assert b"Reserva exitosa" in response.data

def test_reserva_duplicada(client):
    client.post('/reservar', json={"sala": "B", "hora": "14:00"})  # Primera reserva
    response = client.post('/reservar', json={"sala": "B", "hora": "14:00"})  # Duplicada
    assert response.status_code == 409
    assert b"Sala no disponible" in response.data