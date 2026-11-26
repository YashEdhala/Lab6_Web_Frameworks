
from flask import Flask, render_template, request

app = Flask(__name__)


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Dynamic greeting route
@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)


# Form submission route
@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name", "").strip()

    if not name:
        return "Please enter your name.", 400

    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
