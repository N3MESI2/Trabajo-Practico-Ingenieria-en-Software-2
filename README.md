# PARKAPP POSADAS - SISTEMA DE GESTION DE ESTACIONAMIENTOS

## 1. DESCRIPCION GENERAL
ParkApp es una aplicacion diseñada para optimizar la busqueda y reserva de espacios de estacionamiento en la ciudad de Posadas, Misiones. El sistema permite a los conductores localizar cocheras disponibles, seleccionar planes de estadia y obtener tickets digitales con codigos QR para el ingreso y egreso ágil.

## 2. FUNCIONALIDADES PRINCIPALES

**Para Usuarios Conductores:**
- Visualizacion de estacionamientos disponibles con fotos, precios y valoraciones.
- Busqueda dinamica por nombre o zona (ej: Centro, Villa Sarita).
- Filtro por tipo de vehiculo (Auto, Moto, Camioneta, Scooter).
- Mapa de disponibilidad visual para seleccion de piso y lugar especifico.
- Calculadora de tarifas segun plan de permanencia (Por Hora, Medio Dia, Dia Completo).
- Registro de patente y seleccion de hora de llegada (inmediata o personalizada).
- Generacion de Ticket Digital con QR identificador.
- Historial de reservas activas.
- Interfaz adaptable a Modo Oscuro y Modo Claro.

**Para Socios Propietarios:**
- Interfaz exclusiva de registro comercial.
- Formulario de asociacion con CUIT, capacidad operativa, horarios y vinculacion geografica con Google Maps.

## 3. ESPECIFICACIONES TECNICAS
- **Lenguaje de programacion:** Python 3.x
- **Framework de interfaz:** Flet (basado en Flutter)
- **Base de Datos:** SQLite3 (Motor relacional local)
- **Gestion de estado:** Diccionarios de estado global en memoria.

---

##  4. GUÍA DE ONBOARDING PARA DESARROLLADORES
Si te estás sumando al equipo de desarrollo, leé esta sección detenidamente antes de empezar a programar. Aquí explicamos la arquitectura y cómo configurar tu entorno local.

### A. Arquitectura de Archivos
El proyecto sigue una arquitectura básica de separación de responsabilidades en 3 archivos fundamentales:
*   `app.py`: **Frontend.** Contiene toda la interfaz visual construida con Flet. Aquí se definen los controles, tarjetas, navegación y el manejo del tema visual. No debe contener consultas directas a la base de datos.
*   `backend.py`: **Backend/Cerebro.** Centraliza la lógica de negocio y las consultas SQL. Recibe peticiones del frontend (ej: "registrar cochera") y se comunica con SQLite.
*   `database.py`: **Script de Inicialización.** Se ejecuta por única vez para crear el archivo `parkapp.db` y estructurar las tablas (`usuarios`, `cocheras`, `reservas`).

### B. Configuración del Entorno Local (Importante)
Para evitar conflictos de versiones y asegurar que la interfaz se renderice correctamente, es obligatorio aislar el proyecto utilizando un entorno virtual y una versión específica de Flet.

**Paso a paso para instalar:**
1. Clonar este repositorio en tu computadora.
2. Abrir la terminal en la raíz del proyecto y crear el entorno virtual:
   `python -m venv .venv`
3. Activar el entorno virtual:
   - En Windows (PowerShell/CMD): `.\.venv\Scripts\activate`
   - En entornos tipo Bash (Git Bash/MSYS2): `.\.venv\bin\activate`
4. Instalar la versión exacta del framework:
   `pip install flet==0.28.3`
5. Crear la base de datos local:
   `python database.py`
6. Levantar la aplicación:
   `python app.py`

### C. Manejo del Estado y UI
El proyecto no utiliza un sistema tradicional de ruteo por URLs. En su lugar, usamos un **Renderizado Condicional de Vistas**.
*   **Estado Global:** Existe un diccionario llamado `estado_app` en `app.py` que almacena la sesión actual (`id_usuario`, `pantalla_actual`, etc.).
*   **Navegación:** Cada pantalla es una función (`mostrar_principal()`, `mostrar_login()`). Para cambiar de pantalla, la función hace un `page.controls.clear()`, construye la nueva vista y termina con `page.add()`.
*   **Refresco Visual:** Regla de oro en Flet. Siempre que cambies el valor de una variable que el usuario deba ver en pantalla (un texto, un color, un error), debes ejecutar `page.update()` para forzar el repintado de la interfaz.

### D. Flujo de Trabajo para Nuevas Funcionalidades
Si necesitás programar una función nueva, seguí este orden:
1. Diseñá el componente visual en la función correspondiente de `app.py`.
2. Escribí la consulta SQL o la lógica de procesamiento en `backend.py`.
3. Conectá el evento `on_click` o `on_change` de tu componente en el frontend llamando a la función que creaste en el backend.

---

## 5. NOTA OPERATIVA: TICKET QR
El codigo QR generado al finalizar una reserva funciona como el identificador transaccional único. El usuario debe exhibir este código en la barrera física de la cochera tanto al ingresar como al salir. Si la permanencia excede el tiempo prepagado en la app, el sistema de barrera calculará el saldo deudor restante para ser abonado in situ.
