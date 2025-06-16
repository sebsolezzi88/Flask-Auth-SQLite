from flask import Flask,render_template,request
from database import (crear_data_base)


crear_data_base()
app = Flask(__name__)


@app.route('/')
def index():
    return 'Inicio de app'

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        print(request.form['username'])
        print(request.form['password'])
        print(request.form['passwordr'])

        return 'diste post'
    else:
        return render_template('registro.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)