import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_status_code():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_post_structure():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

def test_create_post():
    payload = {
        "title": "QA test title",
        "body": "QA test body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "Updated title"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_post_not_found():
    response = requests.get(f"{BASE_URL}/posts/9999")
    assert response.status_code == 404 or response.json() == {}
