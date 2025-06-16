import os
from dotenv import load_dotenv
from flask import Flask,render_template,request,redirect,url_for,flash,session
from werkzeug.security import check_password_hash
from database import (crear_data_base,insertar_usuario,buscar_username,
                      buscar_username_password,buscar_tareas_por_user_id,
                      agregar_tarea,obtener_tarea_por_id,borrar_tarea_db, actualizar_tarea_db)

#Cargar variable de entorno
load_dotenv()

#Crear base de datos
crear_data_base()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/tareas', methods=["GET", "POST"])
def tareas():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    tareas = []
    user_id = session['user_id']
    user_name = session['username']

    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    #Agregar a la base de datos
    if request.method == "POST":
        titulo = request.form['titulo'].strip()
        descripcion = request.form['descripcion'].strip()
        
        agregar_tarea(titulo,descripcion,user_id)
    
    #Buscar las tareas del usuario
    tareas = buscar_tareas_por_user_id(user_id)
    print(tareas)
    
    return render_template('tareas.html',logged_in=True,user_name=user_name,tareas=tareas)

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
    if 'user_id' in session: # Si ya está logueado, redirige a tareas
        return redirect(url_for('tareas'))
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

#Borrar tarea
@app.route('/borrar/<int:id>',methods=["POST"])
def borrar_tarea(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))


    usuario_id = session['user_id']

    # Obtener la tarea de la base de datos
    tarea = obtener_tarea_por_id(id)

    # Verifica que la tarea pertenece al usuario
    if tarea and tarea['user_id'] == usuario_id:
        borrar_tarea_db(id)
        flash('Tarea borrada correctamente')
    else:
        flash('No tienes permiso para borrar esta tarea')

    return redirect(url_for('tareas'))


#Actualizar tarea
@app.route('/actualizar/<int:id>',methods=["GET","POST"])
def actulizar_tarea(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    user_name = session['username']

    # Obtener la tarea de la base de datos
    tarea = obtener_tarea_por_id(id)

    if tarea is None: # Si la tarea no se encontró en la base de datos
        flash('La tarea especificada no existe.', 'danger') # Mensaje para el usuario
        return redirect(url_for('tareas'))

    #Comprar si la tarea a actulizar corresponde al mismo usuario
    if(tarea["user_id"] != user_id):
        flash('No tienes permiso para borrar esta tarea')
        return redirect(url_for('tareas'))

    if request.method == 'POST':
        titulo = request.form['titulo'].strip()
        descripcion = request.form['descripcion'].strip()
        actualizar_tarea_db(titulo,descripcion,id)

        flash('Tarea actulizada')
        return redirect('/tareas')
    
    
    

    return render_template('actualizar.html',logged_in=True,tarea=tarea,user_name=user_name)


#Cerrar sesion
@app.route('/logout')
def cerrar_sesion():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)