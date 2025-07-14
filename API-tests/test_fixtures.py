import pytest
import requests

url = "https://jsonplaceholder.typicode.com/posts/5"


@pytest.fixture
def get_post_data():
    response = requests.get(url)
    assert response.status_code == 200
    return response.json()


def test_post_has_userId(get_post_data):
    data = get_post_data
    assert "userId" in data

def test_post_hast_title(get_post_data):
    data = get_post_data
    assert "title" in data


def test_post_hastitle2(get_post_data):
    assert "title" in get_post_data



@pytest.fixture
def post_url():
    return "https://jsonplaceholder.typicode.com/posts/5"


def test_get_post_url(post_url):
    response = requests.get(post_url)
    assert response.status_code == 200


@pytest.fixture
def post_url2(post_id):
    return f"https://jsonplaceholder.typicode.com/posts/{post_id}"


@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_post_exists(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id



@pytest.mark.parametrize("post_id", [2, 6, 15])
def test_existed_posts(post_url2):
    response = requests.get(post_url2)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == int(post_url2.split("/")[-1])



