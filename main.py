from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Inicio de app'

@app.route("/registro")
def registro():
    return render_template('registro.html')


if __name__ == "__main__":
    app.run(debug=True)