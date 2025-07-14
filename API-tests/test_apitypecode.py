import requests

url = "https://jsonplaceholder.typicode.com/posts/5"

def test_status_info():
    response = requests.get(url)
    assert response.status_code == 200


def test_id():
    response = requests.get(url)
    data = response.json()
    assert "userId" in data