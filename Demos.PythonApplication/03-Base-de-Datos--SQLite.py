import sqlite3
conn = sqlite3.connect('demo.db')

c = conn.cursor()

# Crear table
c.execute("CREATE TABLE alumnos (id, nombre, apellidos, curso, notas)")

# Insert una fila de datos
c.execute("INSERT INTO alumnos VALUES ('A00', 'Borja', 'Cabeza', '1A', '')")

# Insertar varias filas de datos
alumnos = [('B40', 'Ana', 'Trujillo', '1A', ''),
           ('Z02', 'Jimena', 'Sanz', '2A', '')]
c.executemany('INSERT INTO alumnos VALUES (?,?,?,?,?)', alumnos)

# Guardar los cambios (commit) 
conn.commit()

# También podemos cerrar la conexión si hemos terminado con ella.
# Solo asegúrese de que se hayan realizado cambios o se perderán.
conn.close()
