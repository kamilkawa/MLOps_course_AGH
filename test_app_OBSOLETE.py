import requests

# Make sure to run a server (app) in terminal before executing this file - endpoint must be reachable.
# uv run uvicorn app:app --reload --port 8000
BASE_URL = "http://127.0.0.1:8000"


def test_root():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
