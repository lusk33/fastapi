from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def teste_root():
    client = TestClient(app)  # Arrange
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert
