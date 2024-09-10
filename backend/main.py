from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Template

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number System Converter</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        <h1>Number System Converter</h1>
        <form action="/" method="post">
            <input type="text" name="number" placeholder="Enter number" required>
            <select name="base" required>
                <option value="decimal">Decimal</option>
                <option value="binary">Binary</option>
                <option value="octal">Octal</option>
                <option value="hex">Hexadecimal</option>
            </select>
            <select name="to_base" required>
                <option value="binary">Binary</option>
                <option value="octal">Octal</option>
                <option value="hex">Hexadecimal</option>
                <option value="decimal">Decimal</option>
            </select>
            <button type="submit">Convert</button>
            <button type="reset" class="reset-button">Reset</button>
        </form>
        {% if result %}
        <div class="output">
            <p class="{{ 'error' if 'Error' in result else '' }}">{{ result }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_form():
    template = Template(html_template)
    return template.render(result=None)

@app.post("/", response_class=HTMLResponse)
async def convert_number(request: Request, number: str = Form(...), base: str = Form(...), to_base: str = Form(...)):
    try:
        if base == "decimal":
            num = int(number)
        elif base == "binary":
            num = int(number, 2)
        elif base == "octal":
            if any(c not in '01234567' for c in number):
                raise ValueError("Invalid octal number")
            num = int(number, 8)
        elif base == "hex":
            num = int(number, 16)
        else:
            raise ValueError("Invalid base")

        if to_base == "decimal":
            result = f"Decimal: {num}"
        elif to_base == "binary":
            result = f"Binary: {bin(num)[2:]}"
        elif to_base == "octal":
            result = f"Octal: {oct(num)[2:]}"
        elif to_base == "hex":
            result = f"Hexadecimal: {hex(num)[2:]}"
        else:
            raise ValueError("Invalid target base")
    except ValueError as e:
        result = f"Error: {str(e)}"

    template = Template(html_template)
    return template.render(result=result)
