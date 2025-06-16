import os
from dotenv import load_dotenv
from flask import Flask,render_template,request,redirect,url_for,flash,session
from werkzeug.security import check_password_hash
from database import (crear_data_base,insertar_usuario,buscar_username,
                      buscar_username_password,buscar_tareas_por_user_id,
                      agregar_tarea)

#Cargar variable de entorno
load_dotenv()

#Crear base de datos
crear_data_base()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/tareas', methods=["GET", "POST"])
def tareas():
    tareas = []
    user_id = session['user_id']
    user_name = session['username']

    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    #Agregar a la base de datos
    if request.method == "POST":
        titulo = request.form['titulo'].strip()
        descripcion = request.form['descripcion'].strip()
        print(f"T:{titulo}, des:{descripcion} y el id:{user_id}")
        
        agregar_tarea(titulo,descripcion,user_id)
    
    #Buscar las tareas del usuario
    tareas = buscar_tareas_por_user_id(user_id)
    print(tareas)
    
    return render_template('tareas.html',user_name=user_name,tareas=tareas)

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

@app.route('/login',methods=["GET","POST"])
def login():
    errores = []
    if request.method == "POST":
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if not username or not password:
            errores.append("Debe ingresar usuario y contraseña")
            return render_template('login.html', errores=errores)

        user = buscar_username_password(username)

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('tareas'))
        else:
            errores.append("Usuario o contraseña incorrectos")
            return render_template('login.html', errores=errores)
        

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)