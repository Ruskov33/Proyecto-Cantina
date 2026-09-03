import sqlite3
import sys

def menu():
        print("\nMENU\n")
        print("1.  Cargar alumno")
        print("2.  Consultar alumnos")
        print("3. Salir")

def elegir():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            return opcion

        except ValueError:
            print("Ingrese un número válido.")

class Alumno:
    def __init__(self, codigo, dni, apellido, curso, division, turno):
        self.codigo = codigo
        self.dni = dni
        self.apellido = apellido
        self.curso = curso
        self.division = division
        self.turno = turno
        self.activo = True

def cargar_alumno():
    while True:
        codigo = input("Código: ")
        dni = input("DNI: ")
        apellido = input("Apellido: ")
        curso = input("Curso: ")
        division = input("División: ")
        turno = input("Turno: ")

        alumno = Alumno(
            codigo,
            dni,
            apellido,
            curso,
            division,
            turno
        )

        print("\nAlumno:")
        print(alumno.apellido)
        print(alumno.curso)
        print(alumno.dni)
        print(alumno.codigo)
        print(alumno.division)
        print(alumno.turno)

        if(input("Confirmar alta? (s/n): ").lower() == "s"):
            conexion = sqlite3.connect("BD_VOUCHER_T1.db")
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO ALUMNOS (codigo, dni, apellido, curso, division, turno, activo) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (alumno.codigo, alumno.dni, alumno.apellido, alumno.curso, alumno.division, alumno.turno, alumno.activo))
            conexion.commit()
            conexion.close()
            print("Alumno cargado exitosamente.")
            break
        else:
            print("Vuelva a ingresar los datos del alumno.")

def consultar_alumno():
    dni = input("Ingrese el DNI del alumno a consultar: ")
    conexion = sqlite3.connect("BD_VOUCHER_T1.db")  
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ALUMNOS WHERE dni = ?", (dni,))
    alumno = cursor.fetchone()
    conexion.close()

    if alumno:
        print("\nAlumno encontrado:")
        print(f"Código: {alumno[0]}")
        print(f"DNI: {alumno[1]}")
        print(f"Apellido: {alumno[2]}")
        print(f"Curso: {alumno[3]}")
        print(f"División: {alumno[4]}")
        print(f"Turno: {alumno[5]}")
    else:
        print("Alumno no encontrado.")

while True:

    menu()

    opcion = elegir()

    match opcion:

        case 1:
            cargar_alumno()
            break;

        case 2:
            consultar_alumno()
            break;

        case 3:
            print("UwU")
            sys.exit()

        case _:
              print("Opcion invalida pelele\n")






