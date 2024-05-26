import psycopg2
from PIL import Image
import io

# Conectarse a la base de datos
conn = psycopg2.connect(
    dbname="db_delicias",
    user="user_super",
    password="Bombon2022!",
    host="localhost",
    port="5433"
)
cur = conn.cursor()

# Abre la imagen desde tu sistema de archivos
img = Image.open('C:/Users/Alicia/Desktop/CUMPLIENDO SUENOS/S2DAM/TFG/otros.jpg')

# Convierte la imagen a RGB
img = img.convert("RGB")

# Convierte la imagen a un array de bytes
byte_arr = io.BytesIO()
img.save(byte_arr, format='JPEG')
image_bytes = byte_arr.getvalue()

# Nombre de la nueva categoría y su imagen
nombre = "Otros"

# Insertar la nueva categoría en la base de datos
cur.execute(
    "INSERT INTO categoria (nombre, imagen) VALUES (%s, %s)",
    (nombre, psycopg2.Binary(image_bytes))
)

conn.commit()

# Cerrar la conexión
cur.close()
conn.close()

