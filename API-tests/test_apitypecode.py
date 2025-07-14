import requests

url = "https://jsonplaceholder.typicode.com/posts/5"
url2 = "https://jsonplaceholder.typicode.com/"
send_post_url = "https://jsonplaceholder.typicode.com/posts"


def test_status_info():
    response = requests.get(url)
    assert response.status_code == 200


def test_id():
    response = requests.get(url)
    data = response.json()
    assert "userId" in data
    

def test_allinfo():
    response = requests.get(url)
    data = response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data


def test_in_one_line():
    response = requests.get(url)
    data = response.json()
    together_keys = ["userId", "id", "title", "body"]
    assert all(key in data for key in together_keys)


def test_not_found():
    response = requests.get(f"{url2}/posts/1500")
    assert response.status_code == 404


def test_loop():
    for i in range(50, 52):
        response = requests.get(f"{url2}/posts/{i}")
        assert response.status_code == 200
        data = response.json()
        together_keys = ["userId", "id", "title", "body"]
        assert all(key in data for key in together_keys)



def test_create_post():
    payload = {
        "title": "Moja notatka",
        "userId": 10,
        "id": 101,
        "body": "Tresc nowego posta"
    }
    response = requests.post(send_post_url, json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Moja notatka"
    assert data["title"] == payload["title"]
    assert data["userId"] == 10
    assert data["userId"] == payload["userId"]
    assert data["body"] == "Tresc nowego posta"
    assert data["id"] == 101


def test_deleting_post():
    response = requests.delete(url)
    assert response.status_code == 200


def test_multiple_deleting_post():
    response = requests.delete(url)
    assert response.status_code in [200, 204]


def test_patch():
    payload = {
        "title": "Nowy tytul",
        "test": "teest"
    }
    response = requests.patch(url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["test"] == payload["test"]







