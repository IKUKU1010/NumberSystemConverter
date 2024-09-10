from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_convert_number():
    # Test converting decimal number 10 to binary, octal, and hexadecimal
    response = client.post("/convert", data={"decimal_number": 10})
    assert response.status_code == 200
    result = response.json()
    assert result["binary"] == "1010"       # Binary of 10
    assert result["octal"] == "12"          # Octal of 10
    assert result["hexadecimal"] == "A"     # Hexadecimal of 10 (uppercase)

def test_convert_number_zero():
    # Test converting decimal number 0
    response = client.post("/convert", data={"decimal_number": 0})
    assert response.status_code == 200
    result = response.json()
    assert result["binary"] == "0"          # Binary of 0
    assert result["octal"] == "0"           # Octal of 0
    assert result["hexadecimal"] == "0"     # Hexadecimal of 0

def test_invalid_decimal_number():
    # Test for invalid input (empty input or non-integer)
    response = client.post("/convert", data={"decimal_number": "invalid"})
    assert response.status_code == 422      # Unprocessable entity, invalid input
