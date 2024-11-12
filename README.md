# Instrucciones para el proyecto Django

## Paso a paso para ejecutar un proyecto de Django con TensorFlow, Keras y NumPy

### Requisitos previos

- **Python 3.8 o superior** instalado
  - Asegúrate de tener Python y pip instalados en tu sistema.
  - Para verificar si Python está instalado, ejecuta en la terminal:
    ```bash
    python --version  o python3 --version
    ```
- **pip** (gestor de paquetes de Python)
  - Para verificar si pip está instalado, ejecuta en la terminal:
    ```bash
    pip --version  o pip3 --version
    ```
- **Gestor de entornos virtuales** (recomendado: virtualenv)

> 💡 Si no tienes Python instalado, descárgalo desde [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## Paso 1: Crear un entorno virtual

1. Abre la terminal.
2. Navega al directorio raíz de tu proyecto.
3. Crea un entorno virtual ejecutando:

   - **Linux y macOS**:

     ```bash
     python3 -m venv venv
     ```

   - **Windows**:
     ```bash
     python -m venv venv
     ```

4. Activa el entorno virtual:

   - **Linux y macOS**:

     ```bash
     source venv/bin/activate
     ```

   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

---

## Paso 2: Instalar Django y dependencias

Con el entorno virtual activado, instala las dependencias de tu proyecto Django:

- **Linux y macOS**:

  ```bash
  pip3 install django tensorflow keras numpy
  ```

- **Windows**
  ```bash
  pip install django tensorflow keras numpy
  ```

## Paso 3: Ejecutar el servidor de desarrollo

Inicia el servidor de desarrollo de Django:

- **Linux y macOS**:

  ```bash
  python3 manage.py runserver
  ```

- **Windows**
  ```bash
  python manage.py runserver
  ```

Ahora puedes acceder a tu proyecto Django en [http://localhost:8000](http://localhost:8000])
