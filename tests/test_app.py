from app import app

client = app.test_client()


def test_hello():
    resp = client.get("/")
    data = resp.text
    assert data == "<p>Hello, World!</p>"
