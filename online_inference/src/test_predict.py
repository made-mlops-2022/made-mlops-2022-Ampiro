from fastapi.testclient import TestClient
from endpoints import app

client = TestClient(app)


def test_predict():
    data = {
        "age": 69,
        "sex": 1,
        "cp": 0,
        "trestbps": 160,
        "chol": 234,
        "fbs": 1,
        "restecg": 2,
        "thalach": 131,
        "exang": 0,
        "oldpeak": 0.1,
        "slope": 1,
        "ca": 1,
        "thal": 0
    }

    response = client.post(
        "/predict",
        json=data
    )

    assert response.status_code == 200
    assert response.json()["prediction"] in [0, 1]


def test_predict_invalid_data():
    data = {
        "age": 0,
        "sex": 0,
        "cp": 0,
        "trestbps": 0,
        "chol": 0,
        "fbs": 0,
        "restecg": 0,
        "thalach": 0,
        "exang": 0,
        "oldpeak": 0,
        "slope": 0,
        "ca": 0,
        "thal": 0
    }

    response = client.post(
        "/predict",
        json=data
    )

    assert response.status_code == 400
