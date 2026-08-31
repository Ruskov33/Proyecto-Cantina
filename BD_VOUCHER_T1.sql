
DROP DATABASE if EXISTS VOUCHER;

CREATE DATABASE VOUCHER;

USE VOUCHER;
--Datos basicos de alumnos
CREATE TABLE ALUMNOS (
  id_alumno INT AUTO_INCREMENT PRIMARY KEY,
  Codigo CHAR(3) NOT NULL UNIQUE,
  DNI VARCHAR(10) NOT NULL UNIQUE,
  Nombre VARCHAR(100) NOT NULL,
  Apellido VARCHAR(100) NOT NULL,
  Curso CHAR(2) NOT NULL,
  Division CHAR(2) NOT NULL,
  Turno VARCHAR(10) NOT NULL, 
  Activo BOOLEAN DEFAULT TRUE -- Para no tener que eliminar un registro entero en caso de darse de baja temporalmente
);

-- Usamos para definir y referenciar el nombre de la comida, pueden modificarse. En principio serian solo 4
CREATE TABLE TIPO_VOUCHER (
  id_tipo_voucher INT AUTO_INCREMENT PRIMARY KEY,
  Nombre_comida VARCHAR(50) NOT NULL
);

-- Tabla de asignacion para cada alumna
CREATE TABLE ASIGNACION_VOUCHER (
  id_asignacion INT AUTO_INCREMENT PRIMARY KEY,
  id_alumno INT, -- FK
  id_tipo_vaucher INT, -- FK
  dia_semana INT NOT NULL,

  -- Referencias
  FOREIGN KEY (id_alumno) REFERENCES ALUMNOS (id_alumno),
  FOREIGN KEY (id_tipo_vaucher) REFERENCES TIPO_VOUCHER (id_tipo_voucher),
  -- No permite que haya un alumno con exactamente el mismo voucher asgiando
  CONSTRAINT uq_asignacion_unica UNIQUE (id_alumno, id_tipo_voucher, dia_semana) 
);

-- Tabla de chequeos
CREATE TABLE Consumo_Vouchers (
  id_consumo INT AUTO_INCREMENT PRIMARY KEY, 
  id_alumno INT NOT NULL, -- FK
  id_tipo_voucher INT NOT NULL, -- FK
  fecha DATE NOT NULL, -- Para chequiar
  hora_consumo TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Hora actual para registrar el consumo
    
  -- Referencias a tablas foraneas
  FOREIGN KEY (id_alumno) REFERENCES Alumnos(id_alumno),
  FOREIGN KEY (id_tipo_voucher) REFERENCES Tipos_Voucher(id_tipo_voucher),
    
  -- No permite acumular consumos con los tres campos indenticos
   CONSTRAINT uq_consumo_unico_por_dia UNIQUE (id_alumno, id_tipo_voucher, fecha)
);

/*
  Funcionamiento basico:

  INICIALIZACIÓN OBLIGATORIA
  1. Se cargan los tipos de comida en tipo_voucher 

  ALUMNOS
  2. Se cargan por separado en la tabla ALUMNOS todos los datos basicos
  de cada alumno.

  ALUMNOS - VOUCHER

  3. Se asigna sus voucher correspondientes a cada alumno en ASIGNACION_VOUCHER,
  se establece la comida y el dia (1-5). Se crea un registro por cada comida cada dia que se desee.
  

  PSEUDOCIGO DE LA LOGICA DE CONSUMO

  ALUMNO = BuscarAlumnoPorCodigo(codigo_ingresado)

  SI ALUMNO no existe O ALUMNO.activo == False ENTONCES
      MostrarPantallaRoja("Alumno no válido")
      Terminar Proceso
  FIN SI

  DIA_HOY = ObtenerDiaSemanaActual() -- (1 al 7)
  FECHA_HOY = ObtenerFechaActual()   -- (AAAA-MM-DD)
  COMIDA_SELECCIONADA = ObtenerIdComida() -- (1, 2, 3 o 4)

  -- Paso 2: Validar si tiene el permiso configurado
  TIENE_PERMISO = ConsultarAsignacion(ALUMNO.id, COMIDA_SELECCIONADA, DIA_HOY)

  SI TIENE_PERMISO == Falso ENTONCES
      MostrarPantallaRoja("No tienes este voucher asignado para hoy")
      Terminar Proceso
  FIN SI

  -- Paso 3: Intentar registrar el consumo (El candado final)
  EXITO_REGISTRO = IntentarInsertarConsumo(ALUMNO.id, COMIDA_SELECCIONADA, FECHA_HOY)

  SI EXITO_REGISTRO == Falso ENTONCES
      MostrarPantallaRoja("Acceso Denegado: Ya consumiste esta comida hoy")
  SINO
      MostrarPantallaVerde("Acceso Permitido. ¡Buen provecho!")
      AbrirPuerta()
  FIN SI
 */
