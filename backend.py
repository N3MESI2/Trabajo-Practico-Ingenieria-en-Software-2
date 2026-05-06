import sqlite3

DB_NAME = "parkapp.db"

def obtener_todas_las_cocheras():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre_comercial, direccion, zona, precio, img, descripcion FROM cocheras")
    filas = cursor.fetchall()
    conn.close()
    return filas

def buscar_cocheras(termino):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre_comercial, direccion, zona, precio, img, descripcion 
        FROM cocheras 
        WHERE nombre_comercial LIKE ? OR zona LIKE ?
    """, (f'%{termino}%', f'%{termino}%'))
    filas = cursor.fetchall()
    conn.close()
    return filas

def obtener_o_crear_usuario(nombre):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE nombre = ?", (nombre,))
    usuario = cursor.fetchone()
    if usuario:
        user_id = usuario[0]
    else:
        cursor.execute("INSERT INTO usuarios (nombre, rol) VALUES (?, 'conductor')", (nombre,))
        conn.commit()
        user_id = cursor.lastrowid
    conn.close()
    return user_id

def guardar_reserva(user_id, cochera_id, lugar, patente, llegada, precio, metodo):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservas (id_conductor, id_cochera, lugar, patente, llegada, precio, metodo_pago)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, cochera_id, lugar, patente, llegada, precio, metodo))
    conn.commit()
    conn.close()

def obtener_reservas_usuario(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT c.nombre_comercial, r.lugar, r.llegada, r.patente, r.precio, r.metodo_pago
        FROM reservas r
        JOIN cocheras c ON r.id_cochera = c.id
        WHERE r.id_conductor = ?
        ORDER BY r.id DESC
    ''', (user_id,))
    filas = cursor.fetchall()
    conn.close()
    return filas

def guardar_nueva_cochera(socio_id, nombre, cuit, email, tel, cap, hor, dir, zona, precio, img, desc):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cocheras (id_socio, nombre_comercial, cuit, email, telefono, capacidad, horario, direccion, zona, precio, img, descripcion)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (socio_id, nombre, cuit, email, tel, cap, hor, dir, zona, precio, img, desc))
    conn.commit()
    conn.close()