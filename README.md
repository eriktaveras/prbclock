# Employee Management System

Este es un sistema de gestión de empleados construido con Django.

## Descripción

El sistema permite realizar un seguimiento de los empleados y sus registros de tiempo. Los empleados pueden estar asociados con registros de tiempo que contienen información sobre sus horas de trabajo, incluyendo la hora de entrada, la hora de salida y el tiempo de almuerzo.

## Características

- Gestión de empleados: Agregar, editar y eliminar empleados.
- Registro de tiempo: Registrar las horas de trabajo de los empleados.
- Cálculo de horas trabajadas: Calcular las horas trabajadas por semana y la hora de inicio.
- Interfaz de usuario amigable: Utiliza Bootstrap 5.3 para una interfaz moderna y receptiva.

## Requisitos del Sistema

- Python 3.10
- Django 4.2.6
- Otros requisitos específicos (si los hay)

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/prbclock.git
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

1. Accede a la página de inicio en `http://localhost:8000/` para ver la lista de empleados y sus registros de tiempo.

2. Haz clic en un empleado para ver detalles individuales, incluyendo el total de horas trabajadas esta semana y la hora de inicio.

3. Para agregar un nuevo empleado:
   - Accede al panel de administración en `http://localhost:8000/admin/` utilizando las credenciales de superusuario que creaste durante la instalación.
   - Ve a la sección "Employees" y selecciona "Add" para agregar un nuevo empleado. Completa la información requerida y guarda.

4. Para registrar horas de trabajo para un empleado:
   - Accede al panel de administración en `http://localhost:8000/admin/` utilizando las credenciales de superusuario.
   - Ve a la sección "Time Records" y selecciona "Add" para agregar un nuevo registro de tiempo. Asocia el registro con el empleado correspondiente y completa los campos de fecha, hora de entrada, hora de salida y tiempo de almuerzo.

5. Para calcular el total de horas trabajadas esta semana y la hora de inicio de un empleado, accede a su perfil desde la página de inicio y los datos se mostrarán en la parte superior de la página.

Ten en cuenta que este es un proyecto de ejemplo y la funcionalidad real puede variar según las necesidades de tu empresa o proyecto.

¡Disfruta utilizando el sistema de gestión de empleados!


## Mejoras Futuras

- Autenticación y autorización más robustas.
- Adición de gráficos para visualizar los datos.
