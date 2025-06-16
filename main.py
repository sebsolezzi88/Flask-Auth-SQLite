import os
from dotenv import load_dotenv
from flask import Flask,render_template,request,redirect,url_for,flash
from database import (crear_data_base,insertar_usuario,buscar_username)

#Cargar variable de entorno
load_dotenv()

#Crear base de datos
crear_data_base()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return 'Inicio de app'

@app.route("/registro", methods=["GET", "POST"])
def registro():
    errores = []
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        passwordr = request.form['passwordr']

        # Revisar si los passwords coinciden
        if password != passwordr:
            errores.append("Los passwords no coinciden")
            return render_template("registro.html", errores=errores)

        # Revisar si el usuario ya existe
        user = buscar_username(username)
        if user:
            errores.append("El nombre de usuario ya está registrado")
            return render_template("registro.html", errores=errores)
        
        #Si el username es menos de 6 caracteres
        if len(username) < 6:
            errores.append("El nombre de usuario debe tener al meno 6 caracteres")
            return render_template("registro.html", errores=errores)

        # Insertar usuario
        insertar_usuario(username, password)
        flash("Tu cuenta fue creada con éxito. Ahora puedes iniciar sesión.")
        return redirect(url_for('login'))

    return render_template('registro.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)