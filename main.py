from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/login', methods=['post'])
def receive_data():
    username = request.form["username"]
    password = request.form["password"]
    return render_template("login.html", username=username, password=password)


@app.route('/contact-info', methods=['post'])
def contact_info():
    # username = request.form["username"]
    # password = request.form["password"]
    return "<h1>Data Transfer Successful</h1>"


if __name__ == "__main__":
    app.run(debug=True)
