import psycopg2
import os
import binascii

def export_images(db_name, user, password, host, port, output_dir):
    # Conectar a la base de datos
    conn = psycopg2.connect(database=db_name, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    # Obtener todas las imágenes
    cursor.execute("SELECT idproducto, imagen FROM producto WHERE idproducto = 13")

    images = cursor.fetchall()

    for id, image_hex in images:
        # Decodificar la cadena hexadecimal en bytes
        image_bytes = binascii.unhexlify(image_hex)

        # Escribir los bytes en el archivo
        with open(os.path.join(output_dir, f"{id}.png"), "wb") as f:
            f.write(image_bytes)

    # Cerrar la conexión
    conn.close()

# Uso de la función
export_images("db_delicias", "user_super", "Bombon2022!", "localhost", "5433", "output_dir")
