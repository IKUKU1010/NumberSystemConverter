from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/convert")
async def convert_number(decimal_number: int = Form(...)):
    binary = bin(decimal_number)[2:]  # Remove '0b'
    octal = oct(decimal_number)[2:]    # Remove '0o'
    hexadecimal = hex(decimal_number)[2:].upper()  # Remove '0x'

    return {
        "binary": binary,
        "octal": octal,
        "hexadecimal": hexadecimal
    }

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <html>
        <head>
            <title>Decimal Converter</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #f0f4f8;
                }
                .container {
                    max-width: 500px;
                    margin: auto;
                    background: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
                label, input, button {
                    display: block;
                    width: 100%;
                    margin-bottom: 10px;
                }
                input {
                    padding: 10px;
                    font-size: 16px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                button {
                    padding: 10px;
                    font-size: 16px;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #0056b3;
                }
                .result {
                    margin-top: 20px;
                }
                .result p {
                    background: #e1f7d5;
                    padding: 10px;
                    border-radius: 4px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Decimal Converter</h1>
                <form id="converter-form">
                    <label for="decimal_number">Enter a Decimal Number:</label>
                    <input type="number" id="decimal_number" name="decimal_number" required>
                    <button type="submit">Convert</button>
                </form>
                <div class="result" id="result-container"></div>
            </div>

            <script>
                document.getElementById('converter-form').addEventListener('submit', async function(event) {
                    event.preventDefault();
                    const decimalNumber = document.getElementById('decimal_number').value;

                    // Fetch conversion results
                    const response = await fetch('/convert', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                        },
                        body: new URLSearchParams({ decimal_number: decimalNumber })
                    });

                    const result = await response.json();

                    // Display results
                    document.getElementById('result-container').innerHTML = `
                        <p><strong>Binary:</strong> ${result.binary}</p>
                        <p><strong>Octal:</strong> ${result.octal}</p>
                        <p><strong>Hexadecimal:</strong> ${result.hexadecimal}</p>
                    `;
                });
            </script>
        </body>
    </html>
    """
    return html_content
