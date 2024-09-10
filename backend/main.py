from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from jinja2 import Template

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    template = Template(html_template)
    return template.render(result=None)

@app.post("/", response_class=HTMLResponse)
async def convert_number(
    number: str = Form(...),
    base: str = Form(...),
    to_base: str = Form(...)
):
    try:
        number = number.lower()  # Handle case sensitivity for hexadecimal input

        # Validate the input based on the selected base
        if base == "octal" and not all(c in '01234567' for c in number):
            raise ValueError("Invalid octal number")
        if base == "hex" and not all(c in '0123456789abcdef' for c in number):
            raise ValueError("Invalid hexadecimal number")

        # Convert the input number to decimal first
        if base == "decimal":
            decimal_value = int(number)
        elif base == "octal":
            decimal_value = int(number, 8)
        elif base == "hex":
            decimal_value = int(number, 16)
        else:
            raise ValueError("Unsupported base")

        # Convert the decimal value to the desired base
        if to_base == "binary":
            result = bin(decimal_value)[2:]
        elif to_base == "octal":
            result = oct(decimal_value)[2:]
        elif to_base == "decimal":
            result = str(decimal_value)
        elif to_base == "hex":
            result = hex(decimal_value)[2:]
        else:
            raise ValueError("Unsupported target base")

    except ValueError as e:
        result = f"Error: {str(e)}"

    template = Template(html_template)
    return template.render(result=result)

# Simplified HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Base Converter</title>
</head>
<body>
    <h2>Number Base Converter</h2>
    <form method="post">
        <label for="number">Number:</label>
        <input type="text" id="number" name="number" required placeholder="Enter your number"><br>

        <label for="base">Convert From:</label>
        <select id="base" name="base" required>
            <option value="decimal">Decimal</option>
            <option value="octal">Octal</option>
            <option value="hex">Hexadecimal</option>
        </select><br>

        <label for="to_base">Convert To:</label>
        <select id="to_base" name="to_base" required>
            <option value="binary">Binary</option>
            <option value="octal">Octal</option>
            <option value="decimal">Decimal</option>
            <option value="hex">Hexadecimal</option>
        </select><br>

        <input type="submit" value="Convert">
    </form>

    {% if result %}
    <div>
        <h3>Conversion Result:</h3>
        <p>{{ result }}</p>
    </div>
    {% endif %}
</body>
</html>
"""
