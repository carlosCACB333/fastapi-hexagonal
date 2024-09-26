"""Tests for user handler."""

import pytest
from fastapi.testclient import TestClient

test_cases = {
    "valid_user": {
        "data": {
            "email": "carlos@example.com",
            "password": "password",
            "first_name": "Carlos",
            "last_name": "Barros",
        },
        "expected": {
            "status": "SUCCEEDED",
            "status_code": 200,
        },
    },
    "another_valid_user": {
        "data": {
            "email": "maria@example.com",
            "password": "pass123",
            "first_name": "Maria",
            "last_name": "Lopez",
        },
        "expected": {
            "status": "SUCCEEDED",
            "status_code": 200,
        },
    },
    "invalid_email_user": {
        "data": {
            "email": "invalid-email",
            "password": "123456",
            "first_name": "Invalid",
            "last_name": "User",
        },
        "expected": {
            "status": "FAILED",
            "status_code": 422,
        },
    },
    "invalid_password_user": {
        "data": {
            "email": "de@gmail.com",
            "password": "123",
            "first_name": "Invalid",
            "last_name": "User",
        },
        "expected": {
            "status": "FAILED",
            "status_code": 422,
        },
    },
}


@pytest.mark.parametrize(
    "test_case",
    test_cases.values(),
    ids=test_cases.keys(),
)
def test_user_create(
    client: TestClient,
    test_case,
):
    """Test user creation."""
    response = client.post(
        "/api/v1/users",
        json=test_case["data"],
    )
    body = response.json()

    assert response.status_code == test_case["expected"]["status_code"]
    assert body["status"] == test_case["expected"]["status"]
