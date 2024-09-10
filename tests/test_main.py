from fastapi.testclient import TestClient
 from backend.main import app # Adjust the path if `main.py` is in a different directory

client = TestClient(app)

def test_convert_decimal_to_binary():
    # Simulating a form POST request to convert decimal number 10 to binary
    response = client.post("/", data={"number": "10", "base": "decimal", "to_base": "binary"})
    assert response.status_code == 200
    assert "1010" in response.text  # Binary representation of 10

def test_convert_octal_to_decimal():
    # Simulating a form POST request to convert octal number 12 (octal) to decimal
    response = client.post("/", data={"number": "12", "base": "octal", "to_base": "decimal"})
    assert response.status_code == 200
    assert "10" in response.text  # Decimal representation of octal 12

def test_convert_hex_to_octal():
    # Simulating a form POST request to convert hexadecimal number 'a' to octal
    response = client.post("/", data={"number": "a", "base": "hex", "to_base": "octal"})
    assert response.status_code == 200
    assert "12" in response.text  # Octal representation of hexadecimal 'a'

def test_invalid_input():
    # Simulating a form POST request with an invalid octal number
    response = client.post("/", data={"number": "89", "base": "octal", "to_base": "decimal"})
    assert response.status_code == 200
    assert "Invalid octal number" in response.text  # Error message for invalid input
