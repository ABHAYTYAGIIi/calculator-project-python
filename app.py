from flask import Flask, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        operation = request.form["operation"]

        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)

    return f"""
    <h1>Python Calculator</h1>

    <form method="POST">
        <input name="a" placeholder="First number">

        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>

        <input name="b" placeholder="Second number">

        <button type="submit">Calculate</button>
    </form>

    <h2>Result: {result}</h2>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
