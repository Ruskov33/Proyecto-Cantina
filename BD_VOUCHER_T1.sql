
--Datos basicos de alumnos
CREATE TABLE ALUMNOS (
  id_alumno INTEGER PRIMARY KEY,
  Codigo TEXT NOT NULL UNIQUE,
  DNI TEXT NOT NULL UNIQUE,
  Apellido TEXT NOT NULL,
  Curso TEXT NOT NULL,
  Division TEXT NOT NULL,
  Turno TEXT NOT NULL, 
  Activo INTEGER DEFAULT 1 -- Para no tener que eliminar un registro entero en caso de darse de baja temporalmente
);

-- Usamos para definir y referenciar el nombre de la comida, pueden modificarse. En principio serian solo 4
CREATE TABLE TIPO_VOUCHER (
  id_tipo_voucher INTEGER PRIMARY KEY,
  Nombre_comida TEXT NOT NULL
);

-- Tabla de asignacion para cada alumna
CREATE TABLE ASIGNACION_VOUCHER (
  id_asignacion INTEGER PRIMARY KEY,
  id_alumno INTEGER NOT NULL, -- FK
  id_tipo_vaucher INTEGER NOT NULL, -- FK
  dia_semana INTEGER NOT NULL,

  -- Referencias
  FOREIGN KEY (id_alumno) REFERENCES ALUMNOS (id_alumno),
  FOREIGN KEY (id_tipo_voucher) REFERENCES TIPO_VOUCHER (id_tipo_voucher),
  -- No permite que haya un alumno con exactamente el mismo voucher asgiando
  CONSTRAINT uq_asignacion_unica UNIQUE (id_alumno, id_tipo_voucher, dia_semana) 
);

-- Tabla de chequeos
CREATE TABLE CONSUMO_VOUCHERS (
  id_consumo INTEGER PRIMARY KEY, 
  id_alumno INTEGER NOT NULL, -- FK
  id_tipo_voucher INTEGER NOT NULL, -- FK
  fecha TEXT NOT NULL, -- Para chequiar
  hora_consumo TEXT DEFAULT CURRENT_TIMESTAMP, -- Hora actual para registrar el consumo
    
  -- Referencias a tablas foraneas
  FOREIGN KEY (id_alumno) REFERENCES ALUMNOS(id_alumno),
  FOREIGN KEY (id_tipo_voucher) REFERENCES TiPO_VOUCHER(id_tipo_voucher),
    
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
