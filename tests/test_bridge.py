from fastapi.testclient import TestClient

from bridge.main import app
from blockchain.ton_integration import AuroraTONConnector


client = TestClient(app)


def test_root_reports_bridge_service():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "Aurora Omni-Kernel Bridge"


def test_validate_id_rejects_malformed_address():
    response = client.post("/validate-id", json={"wallet_address": "not-a-ton-address"})
    assert response.status_code == 403


def test_connector_marks_demo_format_as_simulated_valid():
    connector = AuroraTONConnector()
    result = connector.validate_aurora_id("UQ" + "A" * 42)
    assert result["status"] == "VALID"
    assert result["tier"] == "SOVEREIGN"
    assert len(result["aurora_id"]) == 16


def test_kernel_status_is_explicitly_demo_metadata():
    response = client.get("/kernel/status")
    assert response.status_code == 200
    assert response.json()["kernel_type"] == "Omni-Kernel"
