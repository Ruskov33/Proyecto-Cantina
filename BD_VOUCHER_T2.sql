CREATE TABLE ALUMNOS (
  id_alumno INTEGER PRIMARY KEY,
  Codigo TEXT NOT NULL UNIQUE,
  DNI TEXT NOT NULL UNIQUE,
  Nombre TEXT NOT NULL,
  Apellido TEXT NOT NULL,
  Curso TEXT NOT NULL,
  Division TEXT NOT NULL,
  Turno TEXT NOT NULL, 
  Activo INTEGER DEFAULT 1
);
CREATE TABLE TIPO_VOUCHER (
  id_tipo_voucher INTEGER PRIMARY KEY,
  Nombre_comida TEXT NOT NULL
);
CREATE TABLE ASIGNACION_VOUCHER (
  id_asignacion INTEGER PRIMARY KEY,
  id_alumno INTEGER NOT NULL, 
  id_tipo_voucher INTEGER NOT NULL, 
  dia_semana INTEGER NOT NULL,
  FOREIGN KEY (id_alumno) REFERENCES ALUMNOS (id_alumno),
  FOREIGN KEY (id_tipo_voucher) REFERENCES TIPO_VOUCHER (id_tipo_voucher),
  CONSTRAINT uq_asignacion_unica UNIQUE (id_alumno, id_tipo_voucher, dia_semana) 
);
CREATE TABLE CONSUMO_VOUCHERS (
  id_consumo INTEGER PRIMARY KEY, 
  id_alumno INTEGER NOT NULL,
  id_tipo_voucher INTEGER NOT NULL, 
  fecha TEXT NOT NULL, 
  hora_consumo TEXT DEFAULT CURRENT_TIMESTAMP, 
  FOREIGN KEY (id_alumno) REFERENCES ALUMNOS(id_alumno),
  FOREIGN KEY (id_tipo_voucher) REFERENCES TiPO_VOUCHER(id_tipo_voucher),
  CONSTRAINT uq_consumo_unico_por_dia UNIQUE (id_alumno, id_tipo_voucher, fecha)
);