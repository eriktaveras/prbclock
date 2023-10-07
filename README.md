# Employee Time Record App

## Descripción

Una aplicación web de registro de tiempo para empleados temporales. Desarrollada con Django y Bootstrap 5.3, esta aplicación permite a los administradores registrar las horas de trabajo, tiempo de almuerzo, y más.

## Características

- Registro de entrada, salida y tiempo de almuerzo.
- Tabla de resumen semanal organizada por días laborables.
- Exportación e impresión de reportes de horas trabajadas.
- Interfaz administrativa de Django para gestionar empleados.

## Instalación

### Requisitos

- Python 3.x
- Django 3.x

### Pasos

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/employee-time-record-app.git
    ```

2. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Aplicar las migraciones:
    ```bash
    python manage.py migrate
    ```

4. Iniciar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso

1. Acceder al admin de Django para añadir, modificar o eliminar empleados y registros.
2. Acceder a la página principal para ver el resumen de registros de tiempo.

## Tecnologías Utilizadas

- Backend: Django
- Frontend: Bootstrap 5.3, Moment.js
- Base de Datos: SQLite (puede cambiarse)

## Mejoras Futuras

- Autenticación y autorización más robustas.
- Adición de gráficos para visualizar los datos.
