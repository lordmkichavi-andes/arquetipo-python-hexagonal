def test_create_user(client):
    response = client.post("/users", json={"name": "Eve", "email": "eve@example.com", "is_active": False})
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Eve"

def test_get_user_not_found(client):
    response = client.get("/users/999")
    assert response.status_code == 404

def test_get_users(client):
    client.post("/users", json={"name": "Frank", "email": "frank@example.com", "is_active": False})
    client.post("/users", json={"name": "Gina", "email": "gina@example.com", "is_active": True})
    response = client.get("/users")
    data = response.get_json()
    assert len(data) == 2
