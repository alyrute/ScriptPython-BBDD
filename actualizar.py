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
img = Image.open('C:/Users/Alicia/Desktop/CUMPLIENDO SUENOS/S2DAM/TFG/conservas.jpg')

# Convierte la imagen a RGB
img = img.convert("RGB")

# Convierte la imagen a un array de bytes
byte_arr = io.BytesIO()
img.save(byte_arr, format='JPEG')
image_bytes = byte_arr.getvalue()

# Modificar la imagen de la categoría con id = 1
idcategoria = 5  # ID de la categoría que deseas modificar

cur.execute(
     "UPDATE categoria SET nombre = %s, imagen = %s WHERE idcategoria = %s",
    (nuevo_nombre, psycopg2.Binary(image_bytes), id_categoria)
)

conn.commit()

# Cerrar la conexión
cur.close()
conn.close()
