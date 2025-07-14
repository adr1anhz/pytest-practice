import requests

def test_duckduckgo_response():
    url = "https://api.duckduckgo.com/?q=python+programming&format=json&no_redirect=1"
    response = requests.get(url)
    assert response.status_code == 200

def test_duckduckgo_response_contains_python():
    url = "https://api.duckduckgo.com/?q=python+programming&format=json&no_redirect=1"
    response = requests.get(url)
    data = response.json()
    print(data)
    assert "Python" in data["AbstractText"]