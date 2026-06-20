"""Tests for health endpoint."""

import pytest
from fastapi.testclient import TestClient

from runtm_api import __version__
from runtm_api.main import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


def test_health_returns_200(client):
    """Health endpoint should return 200."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_status(client):
    """Health endpoint should return status."""
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_home_returns_json_status(client):
    """Root endpoint should return an API-style JSON status."""
    response = client.get("/")
    data = response.json()

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert data["service"] == "runtm-api"
    assert data["status"] == "healthy"
    assert data["version"] == __version__
    assert "timestamp" in data
    assert data["health_url"] == "/health"
    assert data["docs_url"] == "/docs"
