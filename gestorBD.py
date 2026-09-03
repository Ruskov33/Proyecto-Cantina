import sqlite3

conexion = sqlite3.connect("BD_VOUCHER_T1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM TIPO_VOUCHER")

resultados = cursor.fetchall()

import sqlite3

conexion = sqlite3.connect("BD_VOUCHER_T1.db")

cursor = conexion.cursor()

comidas = [
    ("Desayuno",),
    ("Almuerzo",),
    ("Merienda",),
    ("Cena",)
]

cursor.executemany("""
    INSERT INTO TIPO_VOUCHER (Nombre_comida)
    VALUES (?)
""", comidas)

conexion.commit()

print("Comidas cargadas correctamente")

conexion.close()