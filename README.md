# PARKAPP POSADAS - SISTEMA DE GESTION DE ESTACIONAMIENTOS

DESCRIPCION
ParkApp es una aplicacion diseñada para optimizar la busqueda y reserva de espacios de estacionamiento en la ciudad de Posadas, Misiones. El sistema permite a los conductores localizar cocheras disponibles, seleccionar planes de estadia y obtener tickets digitales con codigos QR para el ingreso y egreso.

FUNCIONALIDADES PARA EL USUARIO
- Visualizacion de estacionamientos disponibles con fotos, precios y valoraciones.
- Busqueda dinamica por nombre o zona (Centro, etc.).
- Filtro por tipo de vehiculo (Auto, Moto, Camioneta, Scooter).
- Mapa de disponibilidad en tiempo real con seleccion de piso y lugar especifico.
- Calculadora de tarifas segun plan de permanencia (Por Hora, Medio Dia, Dia Completo).
- Registro de patente y seleccion de hora de llegada (incluye opcion de llegada inmediata y selector de hora personalizado).
- Generacion de Ticket Digital con QR identificador.
- Historial de reservas activas para el usuario.
- Soporte para Modo Oscuro y Modo Claro.

FUNCIONALIDADES PARA SOCIOS
- Interfaz de registro para propietarios de cocheras.
- Formulario de solicitud de asociacion incluyendo CUIT, capacidad, horarios y ubicacion geografica vinculada a Google Maps.

ESPECIFICACIONES TECNICAS
- Lenguaje de programacion: Python 3.x
- Framework de interfaz: Flet (basado en Flutter)
- Gestion de estado: Diccionarios de estado global para persistencia de datos durante la sesion.
- Integracion externa: Enlaces dinamicos a Google Maps para navegacion GPS.

INSTALACION Y EJECUCION
1. Asegurese de tener instalado Python y el administrador de paquetes pip.
2. Instalar la libreria necesaria:
   pip install flet
3. Ejecutar el archivo principal:
   python app.py

NOTAS SOBRE EL TICKET QR
El codigo QR generado al finalizar la reserva sirve como identificador unico. Debe ser escaneado tanto al ingresar como al salir del establecimiento. En caso de exceder el tiempo prepagado, el sistema calculara la diferencia a abonar en la barrera de salida.
