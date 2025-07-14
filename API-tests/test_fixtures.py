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