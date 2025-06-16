
# 📝 Gestor de Tareas con Flask

Este es un proyecto simple de gestión de tareas creado con **Flask**, que permite a los usuarios:

- Registrarse
- Iniciar sesión
- Crear tareas personales
- Visualizar solo sus propias tareas gracias al sistema de autenticación

---

## 🚀 Tecnologías utilizadas

- [Flask](https://flask.palletsprojects.com/) – Microframework de Python para desarrollo web.
- [SQLite](https://www.sqlite.org/) – Base de datos ligera y fácil de usar.
- [Bootswatch](https://bootswatch.com/) – Temas personalizados para Bootstrap (para los estilos).

---

## 🎯 Funcionalidades

- Registro de usuario con validación y contraseña hasheada.
- Inicio de sesión con autenticación segura.
- Creación de tareas vinculadas al usuario que las crea.
- Cada usuario puede ver solo sus propias tareas.
- Protegido contra acceso no autorizado a rutas privadas.

---

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repo.git
   cd nombre-del-repo
   ```

2. Instala las dependencias:
   ```bash
   pip install flask
   ```

3. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

4. Abre tu navegador en [http://localhost:5000](http://localhost:5000)

---

## 📁 Estructura del proyecto (ejemplo)

```
/mi_proyecto
├── app.py
├── templates/
│   ├── login.html
│   ├── registro.html
│   └── tareas.html
├── static/
│   └── bootswatch/
├── bd.py
├── .gitignore
└── README.md
```

---

## 🔐 Autenticación

El proyecto utiliza contraseñas hasheadas con `werkzeug.security` (`generate_password_hash` y `check_password_hash`). El acceso a las tareas está protegido mediante sesiones, garantizando que cada usuario vea solo sus propias tareas.

---

## 💡 Notas

Este proyecto está en desarrollo. Futuras mejoras pueden incluir:

- Edición y eliminación de tareas
- Marcado de tareas completadas
- Filtro por fecha o estado

---

## 📄 Licencia

Este proyecto es de código abierto. Puedes modificarlo y usarlo para tus propios fines educativos o personales.
