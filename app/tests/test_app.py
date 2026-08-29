import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from app import app


def test_index():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "devsecops-demo"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_info():
    client = app.test_client()

    response = client.get("/api/info")

    assert response.status_code == 200

    data = response.get_json()

    assert "instance" in data