from fastapi.testclient import TestClient
from unittest.mock import patch

from app.services.base_summarizer_service import BaseSummarizerService


class FakeLocalSummarizerService(BaseSummarizerService):
    def summarize(self, text):
        return text


class FakeRemoteSummarizerService(BaseSummarizerService):
    def summarize(self, text):
        return text


def test_get_home():
    from main import app

    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"text": "Привет!"}


def test_post_summarize_local():
    with patch('app.services.local_summarizer_service.LocalSummarizerService', new=FakeLocalSummarizerService):
        from main import app

        client = TestClient(app)
        text = "Test text"
        response = client.post("/summarize", json={"text": text})
        assert response.status_code == 200
        assert "text" in response.json()


def test_post_summarize_remote():
    with patch('app.services.remote_summarizer_service.RemoteSummarizerService', new=FakeRemoteSummarizerService):
        from main import app

        client = TestClient(app)
        text = "Test text"
        response = client.post("/summarize", json={"text": text})
        print(response.json())
        assert response.status_code == 200
        assert "text" in response.json()
