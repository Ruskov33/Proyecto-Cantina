CREATE TABLE ALUMNOS (
  id_alumno INTEGER PRIMARY KEY,
  cod TEXT NOT NULL UNIQUE,
  dni TEXT NOT NULL UNIQUE,
  nombre TEXT NOT NULL,
  apellido TEXT NOT NULL,
  curso TEXT NOT NULL,
  division TEXT NOT NULL,
  turno TEXT NOT NULL, 
  activo INTEGER DEFAULT 1
);
CREATE TABLE COMIDA_VOUCHERS (
  id_comida INTEGER PRIMARY KEY,
  nombre_comida TEXT NOT NULL
);
CREATE TABLE DIA_VOUCHERS (
  id_dia INTEGER PRIMARY KEY,
  nombre_dia TEXT NOT NULL
);
CREATE TABLE ASIGNACION_VOUCHERS (
  id_asignacion INTEGER PRIMARY KEY,
  id_alumno INTEGER NOT NULL, 
  id_comida INTEGER NOT NULL, 
  id_dia INTEGER NOT NULL,
  FOREIGN KEY (id_alumno) REFERENCES ALUMNOS (id_alumno),
  FOREIGN KEY (id_comida) REFERENCES COMIDA_VOUCHERS (id_comida),
  FOREIGN KEY (id_dia) REFERENCES DIA_VOUCHERS (id_dia),
  CONSTRAINT uq_asignacion_unica UNIQUE (id_alumno, id_comida, id_dia) 
);
CREATE TABLE CONSUMO_VOUCHERS (
  id_consumo INTEGER PRIMARY KEY, 
  id_asignacion INTEGER NOT NULL, 
  fecha TEXT NOT NULL, 
  hora_consumo TEXT DEFAULT CURRENT_TIMESTAMP, 
  FOREIGN KEY (id_asignacion) REFERENCES ASIGNACION_VOUCHERS (id_asignacion),
  CONSTRAINT uq_consumo_unico_por_dia UNIQUE (id_asignacion, fecha)
);  