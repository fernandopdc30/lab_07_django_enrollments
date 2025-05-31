# 📘 lab_07_django_enrollments

Este proyecto es una aplicación web desarrollada con Django que permite gestionar inscripciones de productos.

## 🚀 Características principales

* Gestión de inscripciones de estudiantes.
* Interfaz web para crear, leer, actualizar y eliminar registros.
* Uso de Django como framework principal.

## 🗂️ Estructura del repositorio

```
lab_07_django_enrollments/
├── MyDjangoProject/    # Proyecto principal de Django
├── MyWebApps/          # Aplicación Django para inscripciones
├── db.sqlite3          # Base de datos SQLite
├── manage.py           # Script de gestión de Django
└── .gitignore          # Archivos y carpetas ignorados por Git
```

## ⚙️ Requisitos previos

* Python 3.x
* pip (gestor de paquetes de Python)
* Virtualenv (opcional pero recomendado)

## 🛠️ Instalación y ejecución

### 1. **Clonar el repositorio:**

```bash
git clone https://github.com/fernandopdc30/lab_07_django_enrollments.git
cd lab_07_django_enrollments
```

### 2. **Crear y activar un entorno virtual (opcional pero recomendado):**

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

### 3. **Instalar las dependencias:**

```bash
pip install django
```

### 4. **Aplicar migraciones y ejecutar el servidor:**

```bash
python manage.py migrate
python manage.py runserver
```

### 5. **Acceder a la aplicación:**

Abre tu navegador y visita `http://127.0.0.1:8000/`.
