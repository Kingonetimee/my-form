from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods= ['GET', 'POST'])
def login():
    user_name = request.form.get('name')
    user_password = request.form.get('password')
    return render_template("login.html", password = user_password, name = user_name)

if __name__ == "__main__":
    app.run(debug=True)
