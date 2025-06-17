# 📝 Gestor de Tareas con Flask

Este es un proyecto simple de gestión de tareas personales desarrollado con **Flask**. Permite a los usuarios:

- Registrarse
- Iniciar sesión
- Crear tareas personales
- Visualizar únicamente sus propias tareas gracias al sistema de autenticación

---

## 🚀 Tecnologías utilizadas

- [Flask](https://flask.palletsprojects.com/) – Microframework de Python para desarrollo web.
- [SQLite](https://www.sqlite.org/) – Base de datos ligera y fácil de integrar.
- [Bootswatch](https://bootswatch.com/) – Temas personalizados para Bootstrap (estilizado rápido y atractivo).

---

## 🎯 Funcionalidades

- Registro de usuario con validación y contraseñas hasheadas.
- Inicio de sesión con autenticación segura.
- Creación de tareas vinculadas a cada usuario.
- Visualización exclusiva de tareas propias.
- Rutas protegidas contra accesos no autorizados.

---

## ⚙️ Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/sebsolezzi88/Flask-Auth-SQLite
   cd Flask-Auth-SQLite
   ```

2. Instala las dependencias:

   ```bash
   pip install flask
   ```

3. Ejecuta la aplicación:

   ```bash
   python main.py
   ```

4. Abre tu navegador y visita: [http://localhost:5000](http://localhost:5000)

---

## 📁 Estructura del proyecto

```bash
/Flask-Auth-SQLite
├── main.py
├── database.py
├── static/
│   └── bootstrap.css
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── registro.html
│   ├── tareas.html
│   ├── actualizar.html
│   └── about.html
├── .gitignore
└── README.md
```

> ✅ Nota: Asegúrate de que los nombres de archivos y rutas sean consistentes. Por ejemplo, se corrigieron nombres como `actulizar.html` a `actualizar.html`, y la plantilla `base.html` debe estar bien referenciada.

---

## 🔐 Autenticación

Este proyecto utiliza el módulo `werkzeug.security` para hashear contraseñas mediante `generate_password_hash` y verificar su validez con `check_password_hash`.  
Las sesiones se usan para proteger rutas privadas, asegurando que cada usuario solo pueda acceder a su información.

---
