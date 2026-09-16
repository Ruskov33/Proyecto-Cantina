import sqlite3
import sys

def menu():
        print("\nMENU\n")
        print("1. Cargar alumno")
        print("2. Consultar alumnos")
        print("3. Asignar voucher")
        print("4. Consumir voucher")
        print("5. Salir")

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
    conexion = sqlite3.connect("BD_VOUCHER.db")  
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

        cursor.execute("SELECT id_comida, id_dia FROM ASIGNACION_VOUCHER WHERE id_alumno = (SELECT id_alumno FROM ALUMNOS WHERE dni = ?)", (dni,))
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
    conexion = sqlite3.connect("BD_VOUCHER.db")
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

        id_comida = input("Ingrese la comida a asignar (1: Desayuno, 2: Almuerzo, 3: Merienda, 4: Cena): ")
        id_dia = input("Ingrese el día de la semana para el voucher (1-5): ")
        cursor.execute("SELECT id_alumno FROM ALUMNOS WHERE dni = ?", (dni,))
        id_alumno = cursor.fetchone()[0]
        cursor.execute("INSERT INTO ASIGNACION_VOUCHER (id_alumno, id_comida, id_dia) VALUES (?, ?, ?)", (id_alumno, id_comida, id_dia))
        conexion.commit()
        conexion.close()
        print("Voucher asignado correctamente.")
    else:
        print("Alumno no encontrado.")

def consumir_voucher():
    cod = input("Ingrese el código del alumno que desea consumir un voucher: ")
    id_dia = input("Ingrese el día de la semana actual (1-5): ")
    id_comida = input("Ingrese la comida que desea consumir (1: Desayuno, 2: Almuerzo, 3: Merienda, 4: Cena): ")
    fecha = input("Ingrese la fecha de hoy: ")

    conexion = sqlite3.connect("BD_VOUCHER.db")
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id_asignacion FROM ASIGNACION_VOUCHERS "
        "WHERE id_alumno = (SELECT id_alumno FROM ALUMNOS WHERE cod = ?) "
        "AND id_comida = ? AND id_dia = ?",
        (cod, id_comida, id_dia)
    )

    voucher = cursor.fetchone()

    if voucher:
        id_asignacion = voucher[0]

        cursor.execute(
            "INSERT INTO CONSUMO_VOUCHERS (id_asignacion, fecha) VALUES (?, ?)",
            (id_asignacion, fecha)
        )

        conexion.commit()
        print("Voucher consumido correctamente.")

    else:
        print("No se encontró un voucher asignado para ese alumno, día y comida.")
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





