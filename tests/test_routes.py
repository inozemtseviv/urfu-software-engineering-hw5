import os
import pytest
from fastapi.testclient import TestClient

from app.services.local_summarizer_service import LocalSummarizerService
from app.services.remote_summarizer_service import RemoteSummarizerService


@pytest.fixture(autouse=True)
def mock_init(monkeypatch):
    def mock_init(*args, **kwargs):
        return

    monkeypatch.setattr(LocalSummarizerService, "__init__", mock_init)
    monkeypatch.setattr(RemoteSummarizerService, "__init__", mock_init)


@pytest.fixture(autouse=True)
def mock_summarize(monkeypatch):
    def mock_summarize(*args, **kwargs):
        return "Test text"

    monkeypatch.setattr(LocalSummarizerService, "summarize", mock_summarize)
    monkeypatch.setattr(RemoteSummarizerService, "summarize", mock_summarize)


def test_get_home():
    from main import app
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"text": "Привет!"}


def test_post_summarize_local():
    os.environ["SUMMARIZER_TYPE"] = "local"
    from main import app
    client = TestClient(app)

    text = "Test text"
    response = client.post("/summarize", json={"text": text})
    assert response.status_code == 200
    assert "text" in response.json()


def test_post_summarize_remote():
    os.environ["SUMMARIZER_TYPE"] = "remote"
    from main import app
    client = TestClient(app)

    text = "Test text"
    response = client.post("/summarize", json={"text": text})
    assert response.status_code == 200
    assert "text" in response.json()
