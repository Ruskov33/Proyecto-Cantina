import sqlite3
import sys

def menu():
        print("\nMENU\n")
        print("1. Cargar alumno")
        print("2. Consultar alumnos")
        print("3. Salir")

def elegir():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            return opcion

        except ValueError:
            print("Ingrese un número válido.")

class Alumno:
    def __init__(self, codigo, dni, nombre, apellido, curso, division, turno):
        self.codigo = codigo
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.division = division
        self.turno = turno
        self.activo = True

def cargar_alumno():
    codigo = input("Código: ")
    dni = input("DNI: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    curso = input("Curso: ")
    division = input("División: ")
    turno = input("Turno: ")

    alumno = Alumno(
        codigo,
        dni,
        nombre,
        apellido,
        curso,
        division,
        turno
    )

    print("\nAlumno:")
    print(alumno.nombre)
    print(alumno.apellido)
    print(alumno.curso)
    print(alumno.dni)
    print(alumno.codigo)
    print(alumno.division)
    print(alumno.turno)

    if(input("Confirmar alta? (s/n): ").lower() == "s"):
        conexion = sqlite3.connect("BD_VOUCHER.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ALUMNOS (codigo, dni, nombre, apellido, curso, division, turno, activo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (alumno.codigo, alumno.dni, alumno.nombre, alumno.apellido, alumno.curso, alumno.division, alumno.turno, alumno.activo))
        conexion.commit()
        conexion.close()
        print("Alumno cargado exitosamente.")
    else:
        print("Vuelva a ingresar los datos del alumno.")

def consultar_alumno():
    dni = input("Ingrese el DNI del alumno a consultar: ")
    conexion = sqlite3.connect("BD_VOUCHER_T1.db")  
    cursor = conexion.cursor()
    cursor.execute("SELECT codigo, dni, nombre, apellido, curso, division, turno FROM ALUMNOS WHERE dni = ?", (dni,))
    alumno = cursor.fetchone()

    if alumno:
        print("\nAlumno encontrado:")
        print(f"Código: {alumno[0]}")
        print(f"DNI: {alumno[1]}")
        print(f"Nombre: {alumno[2]}")
        print(f"Apellido: {alumno[3]}")
        print(f"Curso: {alumno[4]}")
        print(f"División: {alumno[5]}")
        print(f"Turno: {alumno[6]}")

        cursor.execute("SELECT id_tipo_voucher, dia_semana FROM ASIGNACION_VOUCHER WHERE id_alumno = (SELECT id_alumno FROM ALUMNOS WHERE dni = ?)", (dni,))
        vouchers = cursor.fetchall()
        if vouchers:
            print("\nVouchers asignados:")
            for voucher in vouchers:
                print(f"Tipo de Voucher: {voucher[0]}, Día de la semana: {voucher[1]}")
        else:
            print("No hay vouchers asignados a este alumno.")
    else:
        print("Alumno no encontrado.")
    conexion.close()

def asignar_voucher():
    dni = input("Ingrese el DNI del alumno al que desea asignar un voucher: ")
    conexion = sqlite3.connect("BD_VOUCHER_T1.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT codigo, dni, nombre, apellido, curso, division, turno FROM ALUMNOS WHERE dni = ?", (dni,))
    alumno = cursor.fetchone()

    if alumno:
        print("\nAlumno a actualizar:")
        print(f"Código: {alumno[0]}")
        print(f"DNI: {alumno[1]}")
        print(f"Nombre: {alumno[2]}")
        print(f"Apellido: {alumno[3]}")
        print(f"Curso: {alumno[4]}")
        print(f"División: {alumno[5]}")
        print(f"Turno: {alumno[6]}")

        tipo_voucher = input("Ingrese el tipo de voucher a asignar: ")
        dia_semana = input("Ingrese el día de la semana para el voucher: ")
        cursor.execute("SELECT id_alumno FROM ALUMNOS WHERE dni = ?", (dni,))
        id_alumno = cursor.fetchone()[0]
        cursor.execute("INSERT INTO ASIGNACION_VOUCHER (id_alumno, id_tipo_voucher, dia_semana) VALUES (?, ?, ?)", (id_alumno, tipo_voucher, dia_semana))
        conexion.commit()
        conexion.close()
        print("Voucher asignado correctamente.")
    else:
        print("Alumno no encontrado.")

def consumir_voucher():
    codigo = input("Ingrese el código del alumno que desea consumir un voucher: ")
    dia_actual = input("Ingrese el día de la semana actual (Lunes, Martes, Miércoles, Jueves, Viernes): ")
    comida = input("Ingrese la comida que desea consumir (Desayuno, Almuerzo, Merienda, Cena): ")
    conexion = sqlite3.connect("BD_VOUCHER_T1.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT tipo_voucher, dia_semana FROM ASIGNACION_VOUCHER WHERE id_alumno = (SELECT id_alumno FROM ALUMNOS WHERE codigo = ?)", (codigo,))
    voucher = cursor.fetchall()
    for v in voucher:
        if(v[0] == comida and v[1] == dia_actual):
            cursor.execute("INSERT INTO CONSUMO_VOUCHER (id_alumno, id_asignacion_voucher, fecha) VALUES ((SELECT id_alumno FROM ALUMNOS WHERE codigo = ?), (SELECT id_asignacion_voucher FROM ASIGNACION_VOUCHER WHERE id_alumno = (SELECT id_alumno FROM ALUMNOS WHERE codigo = ?) AND tipo_voucher = ? AND dia_semana = ?), ?)", (codigo, codigo, comida, dia_actual, dia_actual))
            conexion.commit()
            print("Voucher consumido correctamente.")
    else:
        print("Alumno no encontrado.")
    conexion.close()

while True:

    menu()

    opcion = elegir()

    match opcion:

        case 1:
            cargar_alumno()

        case 2:
            consultar_alumno()

        case 3:
            asignar_voucher()

        case 4:
            consumir_voucher()

        case 5:
            print("UwU")
            sys.exit()

        case _:
              print("Opcion invalida pelele\n")





