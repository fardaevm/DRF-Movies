import json

from django.urls import reverse

def test_hello_wordl():
    assert "hello world" == "hello world"
    assert "foo" != "bar"

def test_ping(client):
    url = reverse('ping')
    response = client.get(url)
    content = json.loads(response.content)

    assert response.status_code == 200
    assert content["ping"] == "pong!"