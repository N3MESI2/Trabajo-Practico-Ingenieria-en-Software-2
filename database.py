import sqlite3
import os

DB_NAME = "parkapp.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            rol TEXT NOT NULL CHECK(rol IN ('conductor', 'socio')),
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # ¡ATENCIÓN! Agregamos zona, precio, img y descripcion a la tabla cocheras
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cocheras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_socio INTEGER NOT NULL,
            nombre_comercial TEXT NOT NULL,
            cuit TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT,
            capacidad INTEGER,
            horario TEXT,
            direccion TEXT NOT NULL,
            zona TEXT NOT NULL,
            precio INTEGER NOT NULL,
            img TEXT NOT NULL,
            descripcion TEXT,
            FOREIGN KEY(id_socio) REFERENCES usuarios(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_conductor INTEGER,
            id_cochera INTEGER NOT NULL,
            lugar TEXT NOT NULL,
            patente TEXT NOT NULL,
            llegada TEXT NOT NULL,
            precio INTEGER NOT NULL,
            metodo_pago TEXT NOT NULL,
            fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(id_conductor) REFERENCES usuarios(id),
            FOREIGN KEY(id_cochera) REFERENCES cocheras(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Base de datos inicializada correctamente.")

def poblar_datos_iniciales():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("INSERT OR IGNORE INTO usuarios (id, nombre, rol) VALUES (1, 'Admin Inicial', 'socio')")

    # Lista ampliada: 5 cocheras, distintas zonas, precios y fotos únicas
    cocheras_iniciales = [
        (1, 'Cochera Mitre', '20-12345678-9', 'mitre@mail.com', 'Av. Mitre 2371', 'Centro', 1500, 'https://images.unsplash.com/photo-1590674899484-d5640e854abe?q=80&w=400&auto=format&fit=crop', 'Excelente ubicación. Amplio estacionamiento techado y seguro cerca del casco céntrico.'),
        (1, 'Estac. La Cochera', '20-87654321-9', 'lacochera@mail.com', 'Entre Ríos 2023', 'Centro', 1800, 'https://images.unsplash.com/photo-1573348722427-f1d6819fdf98?q=80&w=400&auto=format&fit=crop', 'Ideal para hacer trámites. Abierto de Lunes a Viernes de 7:00 a 20:00hs.'),
        (1, 'Estacionamiento Colón', '20-11223344-9', 'colon@mail.com', 'Colón 2350', 'Centro', 2000, 'https://images.unsplash.com/photo-1604061986761-d9d0cc41b0d1?q=80&w=400&auto=format&fit=crop', 'Estacionamiento privado muy bien valorado, con espacios para todo tipo de vehículos.'),
        (1, 'Cochera Costanera', '20-55667788-9', 'costa@mail.com', 'Av. Costanera Sur', 'Costanera', 2500, 'https://images.unsplash.com/photo-1506521781263-d8422e82f27a?q=80&w=400&auto=format&fit=crop', 'A pasos del río y zona de bares. Vigilancia 24hs y cámaras de seguridad.'),
        (1, 'Garaje Villa Sarita', '20-99887766-9', 'sarita@mail.com', 'Ivanowski 1230', 'Villa Sarita', 1200, 'https://images.unsplash.com/photo-1470224114660-3f6686c562eb?q=80&w=400&auto=format&fit=crop', 'Estacionamiento económico y tranquilo en el corazón del barrio Villa Sarita.')
    ]

    for cochera in cocheras_iniciales:
        cursor.execute('''
            INSERT OR IGNORE INTO cocheras (id_socio, nombre_comercial, cuit, email, direccion, zona, precio, img, descripcion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', cochera)

    conn.commit()
    conn.close()
    print("Datos iniciales cargados en la base de datos.")

if __name__ == "__main__":
    init_db()
    poblar_datos_iniciales()