# aura/tests/test_api/test_user_endpoints.py


def test_create_user(client):
    response = client.post(
        "/user/",
        headers={"Content-Type": "application/json"},
        json={
            "username": "test_create_user_api",
            "email": "test_api@example.com",
            "role": "student",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "test_create_user_api"
    assert data["email"] == "test_api@example.com"
    assert data["role"] == "student"
