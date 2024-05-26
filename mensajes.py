import psycopg2
from datetime import datetime

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname="db_delicias",
    user="user_super",
    password="Bombon2022!",
    host="localhost",
    port="5433"
)
cursor = conn.cursor()


# Datos de prueba
mensajes = [
    (1, 2, 'Hola, ¿cómo estás?', datetime.now().date(), False),
    (2, 1, 'Estoy bien, gracias. ¿Y tú?', datetime.now().date(), False)
]

# Insertar mensajes de prueba
cursor.executemany('''
INSERT INTO mensaje (senderid, receiverid, texto, fecha, leido) 
VALUES (%s, %s, %s, %s, %s)
''', mensajes)

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Mensajes insertados exitosamente.")
