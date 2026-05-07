from fastapi.testclient import TestClient
from app.main import app

# Inizializza il client finto
client = TestClient(app)


def test_read_root():
    # Chiama l'endpoint "/"
    response = client.get("/")
    assert response.status_code == 200
    # Verifica che la risposta sia un JSON e contenga "Benvenuto"
    assert "benvenuto" in response.json()["message"]


def test_get_skills():
    response = client.get("/skills")
    assert response.status_code == 200
    data = response.json()
    # Verifica che esista la chiave e che contenga "Docker"
    assert "devops" in data
    assert "Docker" in data["devops"]


def test_get_contatti():
    response = client.get("/contatti")
    assert response.status_code == 200
    data = response.json()
    assert "github" in data
    # Verifica che il link inizi con https
    assert data["github"].startswith("https://")
