from app.main import app
from fastapi.testclient import TestClient
import respx
from httpx import Response

client = TestClient(app)

@respx.mock
def test_get_ai_models():
    respx.get("http://localhost:11434/api/tags").mock(
        return_value=Response(200, json={
            "models": [
                {
                    "name": "llama3.2:3b-instruct-q4_K_M",
                    "model": "llama3.2:3b-instruct-q4_K_M",
                    "modified_at": "2025-09-29T12:16:03.912177-07:00",
                    "size": 2019393189,
                    "digest": "a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72",
                    "details": {
                        "parent_model": "",
                        "format": "gguf",
                        "family": "llama",
                        "families": [
                            "llama"
                        ],
                        "parameter_size": "3.2B",
                        "quantization_level": "Q4_K_M"
                    }
                }
            ]})
    )

    response = client.get("/api/models")

    assert response.status_code == 200
    data = response.json()
    assert data["data"]["models"][0]["name"] == "llama3.2:3b-instruct-q4_K_M"