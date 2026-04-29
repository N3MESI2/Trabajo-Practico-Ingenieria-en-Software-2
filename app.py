import flet as ft
import random
import time
import urllib.parse 

def main(page: ft.Page):
    page.title = "ParkApp - Posadas"
    page.window_width = 400
    page.window_height = 800
    page.theme_mode = "light"
    page.padding = 0
    page.bgcolor = "#fcfcfc"
    page.scroll = "auto" 

    estado_app = {
        "nombre_usuario": "",
        "vehiculo_actual": "Auto",
        "reservas": [],
        "pantalla_actual": "login"
    }

    def crear_link_maps(nombre, direccion):
        busqueda = f"{nombre} {direccion} Posadas Misiones"
        busqueda_codificada = urllib.parse.quote(busqueda)
        return f"https://www.google.com/maps/search/?api=1&query=?q={busqueda_codificada}"

    base_estacionamientos = [
        {
            "id": 1, 
            "img": "https://images.unsplash.com/photo-1590674899484-d5640e854abe?q=80&w=400&auto=format&fit=crop", 
            "nombre": "Cochera Mitre", 
            "direccion": "Av. Bartolomé Mitre 2371", 
            "zona": "Centro", 
            "precio": 1500, 
            "estrellas": 5.0, 
            "descripcion": "Excelente ubicación. Amplio estacionamiento techado y seguro cerca del casco céntrico.", 
            "url_mapa": crear_link_maps("Cochera Mitre", "Av. Bartolomé Mitre 2371")
        },
        {
            "id": 2, 
            "img": "https://images.unsplash.com/photo-1573348722427-f1d6819fdf98?q=80&w=400&auto=format&fit=crop", 
            "nombre": "Estac. La Cochera", 
            "direccion": "Entre Ríos 2023", 
            "zona": "Centro", 
            "precio": 1800, 
            "estrellas": 4.1, 
            "descripcion": "Ideal para hacer trámites. Abierto de Lunes a Viernes de 7:00 a 20:00hs.", 
            "url_mapa": crear_link_maps("Estacionamiento La Cochera", "Entre Ríos 2023")
        },
        {
            "id": 3, 
            "img": "https://images.unsplash.com/photo-1604061986761-d9d0cc41b0d1?q=80&w=400&auto=format&fit=crop", 
            "nombre": "Estacionamiento Colón", 
            "direccion": "Colón 2350", 
            "zona": "Centro", 
            "precio": 2000, 
            "estrellas": 5.0, 
            "descripcion": "Estacionamiento privado muy bien valorado, con espacios para todo tipo de vehículos.", 
            "url_mapa": crear_link_maps("Estacionamiento Colon", "Colón 2350")
        },
        {
            "id": 4, 
            "img": "https://images.unsplash.com/photo-1470224114660-3f6686c562eb?q=80&w=400&auto=format&fit=crop", 
            "nombre": "Cocheras San Martín", 
            "direccion": "San Martín y San Luis", 
            "zona": "Centro", 
            "precio": 1800, 
            "estrellas": 4.6, 
            "descripcion": "Atención personalizada, con vigilancia mediante cámaras. Abierto hasta las 22:00hs.", 
            "url_mapa": crear_link_maps("Estacionamiento San Martín", "San Martín y San Luis")
        },
        {
            "id": 5, 
            "img": "https://images.unsplash.com/photo-1506521781263-d8422e82f27a?q=80&w=400&auto=format&fit=crop", 
            "nombre": "Al PaSo Cochera", 
            "direccion": "Bolívar 1640", 
            "zona": "Centro", 
            "precio": 1600, 
            "estrellas": 4.7, 
            "descripcion": "Estacionamiento y Maxikiosco 24hs. Súper práctico para dejar el auto en cualquier momento del día.", 
            "url_mapa": crear_link_maps("Al PaSo Estacionamiento y Maxikiosco", "Bolívar 1640")
        }
    ]

    multiplicadores = {
        "Auto": 1.0, 
        "Moto": 0.5, 
        "Camioneta": 1.5, 
        "Scooter": 0.3
    }

    # ==========================================
    # FUNCIONES GLOBALES (TEMA OSCURO)
    # ==========================================
    def alternar_tema(e):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
            page.bgcolor = "#121212"
        else:
            page.theme_mode = "light"
            page.bgcolor = "#fcfcfc"
        
        page.update()
        
        if estado_app["pantalla_actual"] == "principal":
            mostrar_principal()
        elif estado_app["pantalla_actual"] == "reservas":
            mostrar_reservas()

    # ==========================================
    # PANTALLA 1: INICIO DE SESIÓN
    # ==========================================
    def mostrar_login():
        estado_app["pantalla_actual"] = "login"
        page.controls.clear() 
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center" 

        def intentar_ingresar(e=None):
            nombre = nombre_input.value.strip()
            if nombre == "":
                nombre_input.error_text = "Obligatorio"
                page.update()
            else:
                estado_app["nombre_usuario"] = nombre
                mostrar_principal()

        nombre_input = ft.TextField(
            label="Ingresá tu nombre", 
            width=300, 
            border_radius=10,
            border_color="#1a5e3a", 
            cursor_color="#1a5e3a", 
            prefix_icon="person",
            on_submit=intentar_ingresar 
        )

        boton_ingresar = ft.ElevatedButton(
            content=ft.Text("Buscar Estacionamiento", size=16, weight="bold", color="white"),
            bgcolor="#2a7d4f", 
            width=300, 
            height=50, 
            on_click=intentar_ingresar
        )

        enlace_socio = ft.TextButton(
            text="¿Tenés una cochera? Asociá tu local acá",
            icon="storefront",
            icon_color="grey",
            style=ft.ButtonStyle(
                color="grey", 
                text_style=ft.TextStyle(size=13, weight="bold")
            ),
            on_click=lambda e: mostrar_registro_socio()
        )

        page.add(
            ft.Container(
                padding=20,
                content=ft.Column(
                    horizontal_alignment="center", 
                    spacing=20,
                    controls=[
                        ft.Icon("local_parking", color="#1a5e3a", size=80),
                        ft.Text("Bienvenido a ParkApp", size=24, weight="bold", color="#333333" if page.theme_mode=="light" else "white"),
                        ft.Container(height=10),
                        nombre_input,
                        boton_ingresar,
                        ft.Container(height=30), 
                        enlace_socio 
                    ]
                )
            )
        )
        page.update()

    # ==========================================
    # PANTALLA EXCLUSIVA: REGISTRO DE SOCIOS
    # ==========================================
    def mostrar_registro_socio():
        estado_app["pantalla_actual"] = "registro"
        page.controls.clear()
        page.vertical_alignment = "start"
        color_texto = "#333333" if page.theme_mode == "light" else "white"

        header_socio = ft.Container(
            bgcolor="#1a5e3a", 
            padding=ft.padding.only(left=10, right=20, top=40, bottom=20),
            border_radius=ft.border_radius.only(bottom_left=30, bottom_right=30),
            content=ft.Row(
                controls=[
                    ft.IconButton(icon="arrow_back", icon_color="white", on_click=lambda e: mostrar_login()),
                    ft.Text("Panel de Propietario", size=20, weight="bold", color="white")
                ]
            )
        )

        input_nombre = ft.TextField(label="Nombre Comercial", prefix_icon="storefront", border_color="#1a5e3a")
        input_cuit = ft.TextField(label="CUIT / CUIL", prefix_icon="badge", keyboard_type="number", border_color="#1a5e3a")
        input_email = ft.TextField(label="Correo Electrónico", prefix_icon="email", border_color="#1a5e3a")
        input_telefono = ft.TextField(label="Teléfono de Contacto", prefix_text="+54 ", prefix_icon="phone", keyboard_type="number", border_color="#1a5e3a")
        input_capacidad = ft.TextField(label="Capacidad (Ej: 40 vehículos)", prefix_icon="grid_on", keyboard_type="number", border_color="#1a5e3a")
        
        input_horario = ft.Dropdown(
            label="Horario de Atención", 
            border_color="#1a5e3a",
            options=[
                ft.dropdown.Option("24 Horas"), 
                ft.dropdown.Option("Horario Comercial (08:00 - 20:00)"), 
                ft.dropdown.Option("Nocturno (20:00 - 06:00)")
            ]
        )

        input_dir = ft.TextField(label="Dirección exacta", prefix_icon="location_on", border_color="#1a5e3a", expand=True) 
        btn_mapa = ft.IconButton(
            icon="map", 
            icon_color="white", 
            bgcolor="#2a7d4f", 
            icon_size=24, 
            on_click=lambda e: page.launch_url("https://www.google.com/maps/@-27.3662,-55.8967,16z")
        )

        fila_direccion = ft.Column(
            spacing=2, 
            controls=[
                ft.Row(
                    spacing=10, 
                    controls=[
                        input_dir, 
                        btn_mapa
                    ]
                ), 
                ft.Text("Tocá el botón verde para buscar tu local en el mapa", size=12, color="grey", italic=True)
            ]
        )
        
        formulario = ft.Column(
            spacing=15,
            controls=[
                ft.Text("Ingresá los datos de tu empresa:", size=16, weight="bold", color=color_texto),
                input_nombre, 
                input_cuit, 
                input_email, 
                input_telefono, 
                fila_direccion, 
                ft.Text("Detalles operativos:", size=16, weight="bold", color=color_texto),
                input_capacidad, 
                input_horario
            ]
        )

        cargando = ft.Column(
            visible=False, 
            horizontal_alignment="center", 
            spacing=15, 
            controls=[
                ft.ProgressRing(color="#1a5e3a"), 
                ft.Text("Enviando solicitud a ParkApp...", size=16, weight="bold", color=color_texto)
            ]
        )

        exito = ft.Column(
            visible=False, 
            horizontal_alignment="center", 
            spacing=10,
            controls=[
                ft.Container(
                    bgcolor="#4caf50", 
                    padding=20, 
                    border_radius=10, 
                    width=float("inf"), 
                    content=ft.Column(
                        horizontal_alignment="center", 
                        controls=[
                            ft.Icon("verified", color="white", size=50), 
                            ft.Text("¡Solicitud Recibida!", size=20, weight="bold", color="white"), 
                            ft.Text("Nuestro equipo validará tus datos. Te contactaremos por email para confirmarte si la cochera fue aprobada.", size=14, color="white", text_align="center")
                        ]
                    )
                ),
                ft.TextButton(
                    content=ft.Text("Volver al inicio", color="grey", weight="bold"), 
                    on_click=lambda e: mostrar_login()
                )
            ]
        )

        boton_enviar = ft.ElevatedButton(
            "Enviar Solicitud de Asociación", 
            bgcolor="#2a7d4f", 
            color="white", 
            height=55, 
            width=float("inf"), 
            on_click=lambda e: procesar_solicitud()
        )

        def procesar_solicitud():
            if not input_nombre.value or not input_dir.value or not input_email.value:
                input_nombre.error_text = "Obligatorio" if not input_nombre.value else None
                input_dir.error_text = "Obligatorio" if not input_dir.value else None
                input_email.error_text = "Obligatorio" if not input_email.value else None
                page.update()
                return 

            formulario.visible = False
            boton_enviar.visible = False
            cargando.visible = True
            page.update()
            
            time.sleep(2) 
            
            cargando.visible = False
            exito.visible = True
            page.update()

        page.add(
            header_socio, 
            ft.Container(
                padding=20, 
                content=ft.Column(
                    spacing=20, 
                    horizontal_alignment="center", 
                    controls=[
                        formulario, 
                        boton_enviar, 
                        cargando, 
                        exito
                    ]
                )
            )
        )
        page.update()


    # ==========================================
    # PANTALLA: HISTORIAL DE RESERVAS
    # ==========================================
    def mostrar_reservas():
        estado_app["pantalla_actual"] = "reservas"
        page.controls.clear()
        page.vertical_alignment = "start"

        header_reservas = ft.Container(
            bgcolor="#1a5e3a", 
            padding=ft.padding.only(left=10, right=20, top=40, bottom=20),
            border_radius=ft.border_radius.only(bottom_left=30, bottom_right=30),
            content=ft.Row(
                controls=[
                    ft.IconButton(icon="arrow_back", icon_color="white", on_click=lambda e: mostrar_principal()),
                    ft.Text("Mis Reservas Activas", size=20, weight="bold", color="white")
                ]
            )
        )

        lista_ui = ft.Column(spacing=15)

        if len(estado_app["reservas"]) == 0:
            lista_ui.controls.append(
                ft.Container(
                    padding=40, 
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        horizontal_alignment="center", 
                        controls=[
                            ft.Icon("receipt_long", size=60, color="grey"),
                            ft.Text("No tenés reservas aún.", color="grey", size=16)
                        ]
                    )
                )
            )
        else:
            for res in reversed(estado_app["reservas"]): 
                lista_ui.controls.append(
                    ft.Container(
                        bgcolor="#e8f5e9" if page.theme_mode == "light" else "#1b3320",
                        padding=15, 
                        border_radius=15, 
                        border=ft.border.all(1, "#4caf50"),
                        content=ft.Column(
                            spacing=5, 
                            controls=[
                                ft.Row(
                                    alignment="spaceBetween", 
                                    controls=[
                                        ft.Text(res["local"], weight="bold", size=16, color="#1a5e3a" if page.theme_mode == "light" else "white"),
                                        ft.Container(
                                            bgcolor="#4caf50", 
                                            padding=5, 
                                            border_radius=5, 
                                            content=ft.Text(res["lugar"], color="white", weight="bold")
                                        )
                                    ]
                                ),
                                ft.Text(f"Llegada: {res['llegada']}", size=13, color="grey"),
                                ft.Text(f"Patente: {res['patente'].upper()}", size=13, color="grey"),
                                ft.Divider(color="#cccccc"),
                                ft.Row(
                                    alignment="spaceBetween", 
                                    controls=[
                                        ft.Text(f"Pagado con {res['metodo']}", size=12, italic=True, color="grey"),
                                        ft.Text(f"${res['precio']}", weight="bold", size=16, color="#1a5e3a" if page.theme_mode == "light" else "#a5d6a7")
                                    ]
                                )
                            ]
                        )
                    )
                )

        page.add(
            header_reservas, 
            ft.Container(
                padding=20, 
                content=lista_ui
            )
        )
        page.update()

    # ==========================================
    # PANTALLA 3: DETALLE, MAPA, PLANES, TICKET Y PAGO
    # ==========================================
    def mostrar_detalle(estacionamiento, precio_calculado):
        estado_app["pantalla_actual"] = "detalle"
        page.controls.clear()
        page.vertical_alignment = "start"
        color_fondo_tarjeta = "white" if page.theme_mode == "light" else "#1e1e1e"
        color_texto = "black" if page.theme_mode == "light" else "white"
        color_verde = "#1a5e3a" if page.theme_mode == "light" else "#a5d6a7"

        estado_detalle = {
            "lugar_seleccionado": None,
            "ui_lugares": {},
            "plan": "Por Hora",
            "precio_final": precio_calculado
        }

        texto_precio = ft.Text(
            f"${estado_detalle['precio_final']}", 
            size=28, 
            weight="bold", 
            color=color_verde
        )
        
        texto_total_efectivo = ft.Text(
            f"Total a pagar en local: ${estado_detalle['precio_final']}", 
            weight="bold", 
            size=16, 
            color=color_texto
        )

        header_detalle = ft.Container(
            bgcolor="#1a5e3a", 
            padding=ft.padding.only(left=10, right=20, top=40, bottom=20),
            content=ft.Row(
                controls=[
                    ft.IconButton(icon="arrow_back", icon_color="white", on_click=lambda e: mostrar_principal()), 
                    ft.Text("Detalle del Lugar", size=20, weight="bold", color="white")
                ]
            )
        )

        imagen_grande = ft.Image(src=estacionamiento["img"], width=400, height=200, fit="cover")

        texto_error_lugar = ft.Text("Por favor, seleccioná un lugar en el mapa.", color="red", size=12, visible=False, weight="bold")
        texto_error_datos = ft.Text("Falta completar la patente.", color="red", size=12, visible=False, weight="bold")
        
        def seleccionar_lugar(e):
            id_lugar = e.control.data
            if estado_detalle["lugar_seleccionado"] is not None:
                lugar_anterior = estado_detalle["lugar_seleccionado"]
                estado_detalle["ui_lugares"][lugar_anterior].bgcolor = "#a5d6a7" 
            
            estado_detalle["lugar_seleccionado"] = id_lugar
            e.control.bgcolor = "#1a5e3a" 
            texto_error_lugar.visible = False
            page.update()

        def generar_lugar(id_lugar):
            libre = random.choice([True, False]) 
            if libre:
                btn_lugar = ft.Container(
                    content=ft.Text(id_lugar, size=10, weight="bold", color="black"), 
                    bgcolor="#a5d6a7", 
                    width=35, 
                    height=25, 
                    border_radius=5, 
                    border=ft.border.all(1, "#4caf50"), 
                    alignment=ft.alignment.center, 
                    data=id_lugar, 
                    on_click=seleccionar_lugar, 
                    ink=True
                )
                estado_detalle["ui_lugares"][id_lugar] = btn_lugar
                return btn_lugar
            else:
                return ft.Container(
                    content=ft.Icon("directions_car", color="grey", size=22), 
                    width=35, 
                    height=25, 
                    alignment=ft.alignment.center
                )

        def generar_columna_autos(prefijo, inicio): 
            return ft.Column(
                spacing=5, 
                controls=[generar_lugar(f"{prefijo}{inicio + i}") for i in range(4)]
            )

        mapa_cocheras = ft.Container(
            padding=15, 
            bgcolor=color_fondo_tarjeta, 
            border_radius=15, 
            border=ft.border.all(1, "#e0e0e0"), 
            shadow=ft.BoxShadow(blur_radius=10, color="#eeeeee" if page.theme_mode=="light" else "transparent"), 
            width=360, 
            content=ft.Column(
                horizontal_alignment="center", 
                spacing=10,
                controls=[
                    ft.Text("Seleccioná tu lugar (Cuadros Verdes)", size=14, weight="bold", color=color_texto), 
                    ft.Row(
                        alignment="center", 
                        spacing=20, 
                        controls=[
                            ft.Column(
                                horizontal_alignment="center", 
                                spacing=8, 
                                controls=[
                                    ft.Container(
                                        bgcolor="#a5d6a7", 
                                        padding=ft.padding.only(left=8, right=8, top=2, bottom=2), 
                                        border_radius=5, 
                                        content=ft.Text("Planta baja", size=10, color="black", weight="bold")
                                    ), 
                                    ft.Row(
                                        spacing=15, 
                                        controls=[
                                            generar_columna_autos("A", 1), 
                                            generar_columna_autos("A", 5)
                                        ]
                                    )
                                ]
                            ),
                            ft.Container(width=1, height=140, bgcolor="#cccccc"),
                            ft.Column(
                                horizontal_alignment="center", 
                                spacing=8, 
                                controls=[
                                    ft.Container(
                                        bgcolor="#a5d6a7", 
                                        padding=ft.padding.only(left=8, right=8, top=2, bottom=2), 
                                        border_radius=5, 
                                        content=ft.Text("Primer Piso", size=10, color="black", weight="bold")
                                    ), 
                                    ft.Row(
                                        spacing=15, 
                                        controls=[
                                            generar_columna_autos("B", 1), 
                                            generar_columna_autos("B", 5)
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        )

        def actualizar_precio(e):
            plan_elegido = opciones_plan.value
            estado_detalle["plan"] = plan_elegido
            
            if plan_elegido == "Por Hora": 
                estado_detalle["precio_final"] = precio_calculado
            elif plan_elegido == "Medio Día (12hs)": 
                estado_detalle["precio_final"] = precio_calculado * 10
            elif plan_elegido == "Día Completo (24hs)": 
                estado_detalle["precio_final"] = precio_calculado * 18
            
            texto_precio.value = f"${estado_detalle['precio_final']}"
            texto_total_efectivo.value = f"Total a pagar en local: ${estado_detalle['precio_final']}"
            monto_input.value = ""
            error_efectivo.visible = False
            page.update()

        opciones_plan = ft.Dropdown(
            label="Tipo de estadía", 
            value="Por Hora", 
            border_color="#1a5e3a",
            options=[
                ft.dropdown.Option("Por Hora"), 
                ft.dropdown.Option("Medio Día (12hs)"), 
                ft.dropdown.Option("Día Completo (24hs)")
            ],
            on_change=actualizar_precio
        )

        input_patente = ft.TextField(
            label="Patente (Ej: AC123XX)", 
            border_color="#1a5e3a", 
            width=160
        )
        
        # --- SELECTOR DE HORA TIPO ALARMA ---
        estado_tiempo = {"hora": 12, "minuto": 0}

        txt_hora = ft.Text("12", size=24, weight="bold", color=color_verde)
        txt_minuto = ft.Text("00", size=24, weight="bold", color=color_verde)

        def sumar_hora(e):
            estado_tiempo["hora"] = (estado_tiempo["hora"] + 1) % 24
            txt_hora.value = f"{estado_tiempo['hora']:02d}"
            page.update()

        def restar_hora(e):
            estado_tiempo["hora"] = (estado_tiempo["hora"] - 1) % 24
            txt_hora.value = f"{estado_tiempo['hora']:02d}"
            page.update()

        def sumar_minuto(e):
            estado_tiempo["minuto"] = (estado_tiempo["minuto"] + 5) % 60
            txt_minuto.value = f"{estado_tiempo['minuto']:02d}"
            page.update()

        def restar_minuto(e):
            estado_tiempo["minuto"] = (estado_tiempo["minuto"] - 5) % 60
            txt_minuto.value = f"{estado_tiempo['minuto']:02d}"
            page.update()

        selector_hora_container = ft.Container(
            visible=False,
            width=180, 
            height=75,
            padding=ft.padding.only(left=10, right=10),
            border_radius=10,
            border=ft.border.all(1, "#1a5e3a"),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER, 
                spacing=10,
                controls=[
                    ft.Icon("access_time", color=color_verde, size=24), # CORRECCIÓN DEL ICONO ACÁ
                    ft.Column(
                        horizontal_alignment="center", 
                        alignment=ft.MainAxisAlignment.CENTER, 
                        spacing=0,
                        controls=[
                            ft.IconButton(icon="keyboard_arrow_up", on_click=sumar_hora, icon_color=color_verde, padding=0, height=20, icon_size=20),
                            txt_hora,
                            ft.IconButton(icon="keyboard_arrow_down", on_click=restar_hora, icon_color=color_verde, padding=0, height=20, icon_size=20)
                        ]
                    ),
                    ft.Text(":", size=20, weight="bold", color=color_verde),
                    ft.Column(
                        horizontal_alignment="center", 
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            ft.IconButton(icon="keyboard_arrow_up", on_click=sumar_minuto, icon_color=color_verde, padding=0, height=20, icon_size=20),
                            txt_minuto,
                            ft.IconButton(icon="keyboard_arrow_down", on_click=restar_minuto, icon_color=color_verde, padding=0, height=20, icon_size=20)
                        ]
                    )
                ]
            )
        )

        def mostrar_input_personalizado(e):
            if input_llegada.value == "Hora personalizada...":
                selector_hora_container.visible = True
            else:
                selector_hora_container.visible = False
            page.update()

        input_llegada = ft.Dropdown(
            label="¿Cuándo llegás?", 
            value="Ahora mismo (Lo antes posible)", 
            border_color="#1a5e3a", 
            width=190,
            options=[
                ft.dropdown.Option("Ahora mismo (Lo antes posible)"), 
                ft.dropdown.Option("En 30 minutos"), 
                ft.dropdown.Option("En 1 hora"), 
                ft.dropdown.Option("Mañana a la mañana"),
                ft.dropdown.Option("Hora personalizada...") 
            ],
            on_change=mostrar_input_personalizado
        )
        # -------------------------------------------

        texto_lugar_exito = ft.Text("Lugar reservado: --", size=16, weight="bold", color="white")
        texto_vuelto_exito = ft.Text("", size=14, color="white", visible=False, weight="bold")

        txt_ticket_lugar = ft.Text("Lugar: --", color="black")
        txt_ticket_patente = ft.Text("Patente: --", color="black")
        txt_ticket_llegada = ft.Text("Llegada: --", color="black")
        txt_ticket_pago = ft.Text("Pagado: --", weight="bold", color="#1a5e3a")

        ticket_digital = ft.Container(
            visible=False, 
            bgcolor="white", 
            border=ft.border.all(2, "#1a5e3a"), 
            border_radius=10, 
            padding=20, 
            width=float("inf"),
            content=ft.Column(
                horizontal_alignment="center", 
                spacing=5,
                controls=[
                    ft.Text("TICKET DE RESERVA", weight="bold", size=18, color="#1a5e3a"),
                    ft.Icon("qr_code_2", size=100, color="black"),
                    ft.Text(estacionamiento["nombre"], weight="bold", color="black"),
                    txt_ticket_lugar,
                    txt_ticket_patente,
                    txt_ticket_llegada,
                    ft.Divider(color="grey"),
                    txt_ticket_pago,
                    ft.Container(height=5),
                    ft.Text("Escaneá este QR al entrar y salir. El tiempo excedente se abona en la barrera.", size=10, color="grey", text_align="center")
                ]
            )
        )

        boton_reserva = ft.ElevatedButton(
            content=ft.Row(
                alignment="center", 
                controls=[
                    ft.Icon("local_parking", color="white"), 
                    ft.Text("Confirmar Reserva", color="white", size=18, weight="bold")
                ]
            ),
            bgcolor="#1a5e3a", 
            height=60, 
            width=float("inf"), 
            on_click=lambda e: iniciar_reserva()
        )

        menu_pagos = ft.Column(
            visible=False, 
            spacing=10,
            controls=[
                ft.Text("Seleccioná tu método de pago:", weight="bold", size=16, color=color_texto),
                ft.ElevatedButton(
                    content=ft.Row([ft.Icon("credit_card", color="#1a5e3a"), ft.Text("Tarjeta Débito/Crédito", color="black")]), 
                    bgcolor="#f5f5f5", 
                    width=float("inf"), 
                    height=50, 
                    on_click=lambda e: procesar_pago("Tarjeta")
                ),
                ft.ElevatedButton(
                    content=ft.Row([ft.Icon("qr_code_scanner", color="#1a5e3a"), ft.Text("MercadoPago / Transferencia", color="black")]), 
                    bgcolor="#f5f5f5", 
                    width=float("inf"), 
                    height=50, 
                    on_click=lambda e: procesar_pago("Transferencia")
                ),
                ft.ElevatedButton(
                    content=ft.Row([ft.Icon("payments", color="#1a5e3a"), ft.Text("Efectivo en el Local", color="black")]), 
                    bgcolor="#f5f5f5", 
                    width=float("inf"), 
                    height=50, 
                    on_click=lambda e: procesar_pago("Efectivo")
                ),
                ft.TextButton(
                    content=ft.Text("Volver atrás", color="grey", weight="bold"), 
                    on_click=lambda e: cancelar_pago()
                )
            ]
        )

        def confirmar_efectivo(e=None):
            try: 
                monto_ingresado = int(monto_input.value.strip())
            except ValueError:
                error_efectivo.value = "Por favor, ingresá un número válido."
                error_efectivo.visible = True
                page.update()
                return

            if monto_ingresado < estado_detalle["precio_final"]:
                error_efectivo.value = f"Monto insuficiente. Faltan ${estado_detalle['precio_final'] - monto_ingresado}"
                error_efectivo.visible = True
                page.update()
            else:
                vuelto = monto_ingresado - estado_detalle["precio_final"]
                error_efectivo.visible = False
                ingreso_efectivo.visible = False
                
                if vuelto > 0: 
                    texto_vuelto_exito.value = f"Tu vuelto en la caja será de: ${vuelto}"
                else: 
                    texto_vuelto_exito.value = "Pago exacto (Sin vuelto)."
                
                texto_vuelto_exito.visible = True
                
                texto_validando.value = "Registrando reserva para pago en local..."
                cargando_pago.visible = True
                page.update()
                
                time.sleep(1.5) 
                
                finalizar_reserva("Efectivo")

        monto_input = ft.TextField(
            label="¿Con cuánto vas a pagar?", 
            prefix_text="$ ", 
            keyboard_type="number", 
            border_color="#1a5e3a", 
            cursor_color="#1a5e3a", 
            width=float("inf"), 
            on_submit=confirmar_efectivo
        )
        
        error_efectivo = ft.Text("", color="red", visible=False, size=12, weight="bold")

        ingreso_efectivo = ft.Column(
            visible=False, 
            spacing=10,
            controls=[
                texto_total_efectivo, 
                monto_input, 
                error_efectivo,
                ft.Row(
                    alignment="spaceBetween", 
                    controls=[
                        ft.TextButton(content=ft.Text("Cambiar método", color="grey", weight="bold"), on_click=lambda e: cancelar_efectivo()), 
                        ft.ElevatedButton("Confirmar Pago", bgcolor="#1a5e3a", color="white", on_click=confirmar_efectivo)
                    ]
                )
            ]
        )

        texto_validando = ft.Text("Validando pago...", size=16, weight="bold", color=color_texto)
        
        cargando_pago = ft.Column(
            visible=False, 
            horizontal_alignment="center", 
            spacing=15, 
            controls=[
                ft.ProgressRing(color="#1a5e3a"), 
                texto_validando, 
                ft.Text("Por favor, no cierres la aplicación.", size=12, color="grey")
            ]
        )

        mensaje_exito = ft.Column(
            visible=False, 
            horizontal_alignment="center", 
            spacing=10,
            controls=[
                ticket_digital, 
                ft.Container(
                    bgcolor="#4caf50", 
                    padding=15, 
                    border_radius=10, 
                    width=float("inf"), 
                    content=ft.Column(
                        horizontal_alignment="center", 
                        controls=[
                            ft.Icon("check_circle", color="white", size=40), 
                            ft.Text("¡Reserva Confirmada!", size=18, weight="bold", color="white"), 
                            texto_vuelto_exito, 
                            ft.Text("Presentá el ticket en la barrera.", size=14, color="white", text_align="center")
                        ]
                    )
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        alignment="center", 
                        controls=[
                            ft.Icon("map", color="#1a5e3a"), 
                            ft.Text("¿Necesita guía de cómo llegar?", color="#1a5e3a", weight="bold")
                        ]
                    ), 
                    bgcolor="white", 
                    height=50, 
                    width=float("inf"), 
                    on_click=lambda e: page.launch_url(estacionamiento["url_mapa"])
                )
            ]
        )

        def iniciar_reserva():
            if estado_detalle["lugar_seleccionado"] is None:
                texto_error_lugar.visible = True
                page.update()
                return
            if input_patente.value.strip() == "":
                texto_error_datos.value = "Falta completar la patente."
                texto_error_datos.visible = True
                page.update()
                return

            texto_error_lugar.visible = False
            texto_error_datos.visible = False
            texto_vuelto_exito.visible = False 
            
            opciones_plan.disabled = True
            input_patente.disabled = True
            input_llegada.disabled = True
            selector_hora_container.disabled = True 
            
            boton_reserva.visible = False
            menu_pagos.visible = True
            page.update()

        def cancelar_pago():
            menu_pagos.visible = False
            boton_reserva.visible = True
            opciones_plan.disabled = False
            input_patente.disabled = False
            input_llegada.disabled = False
            selector_hora_container.disabled = False
            page.update()

        def cancelar_efectivo():
            ingreso_efectivo.visible = False
            error_efectivo.visible = False
            monto_input.value = ""
            menu_pagos.visible = True
            page.update()

        def procesar_pago(metodo):
            if metodo == "Efectivo":
                menu_pagos.visible = False
                ingreso_efectivo.visible = True
                page.update()
            else:
                texto_validando.value = f"Validando pago con {metodo}..."
                menu_pagos.visible = False
                cargando_pago.visible = True
                page.update()
                
                time.sleep(2) 
                
                finalizar_reserva(metodo)

        def finalizar_reserva(metodo):
            cargando_pago.visible = False
            mensaje_exito.visible = True
            
            if input_llegada.value == "Hora personalizada...":
                hora_final = f"{txt_hora.value}:{txt_minuto.value} hs"
            else:
                hora_final = input_llegada.value

            txt_ticket_lugar.value = f"Lugar: {estado_detalle['lugar_seleccionado']}"
            txt_ticket_patente.value = f"Patente: {input_patente.value.upper()}"
            txt_ticket_llegada.value = f"Llegada: {hora_final}"
            txt_ticket_pago.value = f"Abonado: ${estado_detalle['precio_final']} ({metodo})"
            
            ticket_digital.visible = True

            nueva_reserva = {
                "local": estacionamiento["nombre"],
                "lugar": estado_detalle["lugar_seleccionado"],
                "patente": input_patente.value.upper(),
                "llegada": hora_final,
                "precio": estado_detalle['precio_final'],
                "metodo": metodo
            }
            estado_app["reservas"].append(nueva_reserva)
            
            page.update()

        info_container = ft.Container(
            padding=20, 
            bgcolor=color_fondo_tarjeta, 
            border_radius=ft.border_radius.only(top_left=30, top_right=30), 
            margin=ft.margin.only(top=-30),
            content=ft.Column(
                spacing=15, 
                horizontal_alignment="center", 
                controls=[
                    ft.Row(
                        alignment="spaceBetween", 
                        controls=[
                            ft.Container(
                                width=220, 
                                content=ft.Text(estacionamiento["nombre"], size=20, weight="bold", color=color_texto)
                            ), 
                            ft.Row(
                                spacing=5, 
                                controls=[
                                    ft.Icon("star", color="#e6a800", size=20), 
                                    ft.Text(str(estacionamiento["estrellas"]), size=16, weight="bold", color=color_texto)
                                ]
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon("location_on", color="grey", size=14), 
                            ft.Text(f'{estacionamiento["direccion"]} - {estacionamiento["zona"]}', size=14, color="grey")
                        ]
                    ),
                    ft.Text(estacionamiento["descripcion"], size=13, color="grey"),
                    
                    mapa_cocheras,
                    texto_error_lugar,

                    ft.Divider(color="#eeeeee" if page.theme_mode=="light" else "grey"),
                    
                    opciones_plan, 
                    
                    ft.Row(
                        alignment="spaceBetween", 
                        controls=[
                            input_patente, 
                            input_llegada
                        ]
                    ),
                    selector_hora_container, 
                    texto_error_datos,

                    ft.Row(
                        alignment="spaceBetween",
                        controls=[
                            ft.Column(
                                spacing=2, 
                                controls=[
                                    ft.Text("Tarifa a pagar", size=14, color="grey"), 
                                    ft.Text(f'Vehículo: {estado_app["vehiculo_actual"]}', size=12, weight="bold", color="#1a5e3a" if page.theme_mode=="light" else "#a5d6a7")
                                ]
                            ),
                            texto_precio 
                        ]
                    ),
                    ft.Container(height=5),
                    
                    boton_reserva,
                    menu_pagos,
                    ingreso_efectivo, 
                    cargando_pago,
                    mensaje_exito 
                ]
            )
        )

        page.add(header_detalle, imagen_grande, info_container)
        page.update()

    # ==========================================
    # PANTALLA 2: LISTA DE ESTACIONAMIENTOS
    # ==========================================
    def mostrar_principal():
        estado_app["pantalla_actual"] = "principal"
        page.controls.clear() 
        page.vertical_alignment = "start"
        color_texto = "#333333" if page.theme_mode == "light" else "white"

        botones_ui = {}     

        def renderizar_lista(e=None):
            lista_estacionamientos.content.controls.clear()
            termino_busqueda = search_input.value.lower() if search_input.value else ""
            mult = multiplicadores[estado_app["vehiculo_actual"]]

            for est in base_estacionamientos:
                if termino_busqueda in est["nombre"].lower() or termino_busqueda in est["zona"].lower():
                    precio_calculado = int(est["precio"] * mult)
                    lista_estacionamientos.content.controls.append(crear_tarjeta_estacionamiento(est, precio_calculado))
            page.update()

        def cambiar_vehiculo(e):
            estado_app["vehiculo_actual"] = e.control.data
            for nombre, controles in botones_ui.items():
                es_seleccionado = (nombre == estado_app["vehiculo_actual"])
                controles["container"].bgcolor = "#2a7d4f" if es_seleccionado else ("white" if page.theme_mode=="light" else "#1e1e1e")
                controles["icono"].color = "white" if es_seleccionado else "grey"
                controles["container"].shadow = None if es_seleccionado else ft.BoxShadow(blur_radius=10, color="#eeeeee" if page.theme_mode=="light" else "transparent")
                controles["texto"].weight = "bold" if es_seleccionado else "normal"
            renderizar_lista()

        header = ft.Container(
            bgcolor="#1a5e3a", 
            padding=ft.padding.only(left=20, right=20, top=40, bottom=30),
            border_radius=ft.border_radius.only(bottom_left=30, bottom_right=30),
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment="spaceBetween",
                        controls=[
                            ft.Row(
                                spacing=10, 
                                controls=[
                                    ft.CircleAvatar(radius=20, background_image_src="https://i.pravatar.cc/150?img=11"),
                                    ft.Text(f'Buenos Días, {estado_app["nombre_usuario"]}', color="white", size=14, weight="w500")
                                ]
                            ),
                            ft.Row(
                                spacing=0, 
                                controls=[
                                    ft.IconButton(icon="receipt_long", icon_color="white", tooltip="Mis Reservas", on_click=lambda e: mostrar_reservas()),
                                    ft.IconButton(icon="dark_mode" if page.theme_mode=="light" else "light_mode", icon_color="white", tooltip="Modo Oscuro", on_click=alternar_tema),
                                    ft.IconButton(icon="logout", icon_color="white", tooltip="Cerrar Sesión", on_click=lambda e: mostrar_login())
                                ]
                            )
                        ]
                    ),
                    ft.Container(height=15),
                    ft.Text("Elija el mejor lugar\npara estacionar.", size=28, weight="bold", color="white")
                ]
            )
        )

        search_input = ft.TextField(
            hint_text="Buscar zona (ej: Centro)", 
            prefix_icon="search", 
            border_radius=15, 
            bgcolor="white" if page.theme_mode=="light" else "#1e1e1e", 
            border_color="transparent", 
            filled=True, 
            height=50, 
            text_size=14, 
            on_change=renderizar_lista
        )
        
        search_bar = ft.Container(
            padding=ft.padding.only(left=20, right=20, top=10), 
            content=ft.Container(
                content=search_input, 
                shadow=ft.BoxShadow(blur_radius=15, color="#e0e0e0" if page.theme_mode=="light" else "transparent")
            )
        )

        def crear_boton_vehiculo(icono, texto):
            seleccionado = (texto == estado_app["vehiculo_actual"])
            bg_color = "#2a7d4f" if seleccionado else ("white" if page.theme_mode=="light" else "#1e1e1e")
            icon_color = "white" if seleccionado else "grey"
            text_weight = "bold" if seleccionado else "normal"
            
            icono_ctrl = ft.Icon(icono, color=icon_color, size=30)
            texto_ctrl = ft.Text(texto, size=12, weight=text_weight, color=color_texto)
            
            container_ctrl = ft.Container(
                content=icono_ctrl, 
                bgcolor=bg_color, 
                width=70, 
                height=70, 
                border_radius=15, 
                alignment=ft.alignment.center,
                shadow=ft.BoxShadow(blur_radius=10, color="#eeeeee" if page.theme_mode=="light" else "transparent") if not seleccionado else None,
                data=texto, 
                on_click=cambiar_vehiculo, 
                ink=True 
            )
            
            botones_ui[texto] = {"container": container_ctrl, "icono": icono_ctrl, "texto": texto_ctrl}
            
            return ft.Column(
                horizontal_alignment="center", 
                spacing=5, 
                controls=[container_ctrl, texto_ctrl]
            )

        categorias = ft.Container(
            padding=ft.padding.only(left=20, right=20, top=15),
            content=ft.Row(
                alignment="spaceBetween",
                controls=[
                    crear_boton_vehiculo("directions_car", "Auto"),
                    crear_boton_vehiculo("two_wheeler", "Moto"),
                    crear_boton_vehiculo("airport_shuttle", "Camioneta"),
                    crear_boton_vehiculo("electric_scooter", "Scooter"),
                ]
            )
        )

        titulo_lista = ft.Container(
            padding=ft.padding.only(left=20, right=20, top=20, bottom=5), 
            content=ft.Row(
                alignment="spaceBetween", 
                controls=[
                    ft.Text("Estacionamientos Disponibles:", size=18, weight="bold", color=color_texto), 
                    ft.Icon("more_horiz", color="grey")
                ]
            )
        )

        def crear_tarjeta_estacionamiento(estacionamiento, precio_calculado):
            return ft.Container(
                bgcolor="#e8f5e9" if page.theme_mode=="light" else "#1b3320", 
                border_radius=20, 
                padding=10, 
                ink=True,
                on_click=lambda e: mostrar_detalle(estacionamiento, precio_calculado), 
                content=ft.Row(
                    spacing=15,
                    controls=[
                        ft.Image(src=estacionamiento["img"], width=110, height=85, border_radius=15, fit="cover"),
                        ft.Column(
                            spacing=4,
                            controls=[
                                ft.Text(estacionamiento["nombre"], size=13, weight="bold", color=color_texto),
                                ft.Row(
                                    spacing=3, 
                                    controls=[
                                        ft.Icon("location_on", size=12, color="grey"), 
                                        ft.Text(f'{estacionamiento["direccion"]} ({estacionamiento["zona"]})', size=11, color="grey")
                                    ]
                                ),
                                ft.Row(
                                    spacing=3, 
                                    controls=[
                                        ft.Icon("star", size=14, color="#e6a800"), 
                                        ft.Text(str(estacionamiento["estrellas"]), size=12, weight="bold", color="grey")
                                    ]
                                ),
                                ft.Text(f"${precio_calculado}/H", size=14, weight="bold", color="#1a5e3a" if page.theme_mode=="light" else "#a5d6a7") 
                            ]
                        )
                    ]
                )
            )

        lista_estacionamientos = ft.Container(
            padding=ft.padding.only(left=20, right=20, bottom=20), 
            content=ft.Column(spacing=15, controls=[])
        )

        page.add(header, search_bar, categorias, titulo_lista, lista_estacionamientos)
        renderizar_lista()

    mostrar_login()

ft.app(target=main)