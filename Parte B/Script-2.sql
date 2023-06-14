-- Crear base de datos
CREATE DATABASE ;

-- Usar base de datos
USE Medios;

-- Crear tabla Pais
CREATE TABLE Pais (
  id_pais INT PRIMARY KEY
);

-- Crear tabla Region
CREATE TABLE Region (
  codigo_region INT,
  nombre_region VARCHAR(100),
  id_pais INT,
  PRIMARY KEY (codigo_region),
  FOREIGN KEY (id_pais) REFERENCES Pais(id_pais)
);

-- Crear tabla Comuna
CREATE TABLE Comuna (
  codigo_comuna INT,
  poblacion INT,
  superficie INT,
  nombre_comuna VARCHAR(100),
  codigo_region INT,
  PRIMARY KEY (codigo_comuna),
  FOREIGN KEY (codigo_region) REFERENCES Region(codigo_region)
);

-- Crear tabla Trabajo
CREATE TABLE Trabajo (
  id_trabajo INT PRIMARY KEY,
  hombres_desocupados INT,
  hombres_ocupados INT,
  mujeres_ocupadas INT,
  mujeres_desocupadas INT
);

-- Crear tabla Salud
CREATE TABLE Salud (
  id_salud INT PRIMARY KEY,
  n_farmacias INT,
  n_centros_salud INT
);

-- Crear tabla Indices_educativos
CREATE TABLE Indices_educativos (
  id_indice_educativo INT PRIMARY KEY,
  tipo_establecimiento VARCHAR(100),
  nivel_establecimiento VARCHAR(100),
  promedio_puntaje_simce FLOAT
);

-- Crear tabla Seguridad
CREATE TABLE Seguridad (
  id_seguridad INT PRIMARY KEY,
  n_establecimientos_policiales INT,
  tasa_delictual FLOAT
);

-- Crear tabla Ofrecer
CREATE TABLE Ofrecer (
  id_trabajo INT,
  codigo_comuna INT,
  PRIMARY KEY (id_trabajo, codigo_comuna),
  FOREIGN KEY (id_trabajo) REFERENCES Trabajo(id_trabajo),
  FOREIGN KEY (codigo_comuna) REFERENCES Comuna(codigo_comuna)
);

-- Crear tabla Cuenta_con
CREATE TABLE Cuenta_con (
  id_salud INT,
  codigo_comuna INT,
  PRIMARY KEY (id_salud, codigo_comuna),
  FOREIGN KEY (id_salud) REFERENCES Salud(id_salud),
  FOREIGN KEY (codigo_comuna) REFERENCES Comuna(codigo_comuna)
);

-- Crear tabla Tener
CREATE TABLE Tener (
  id_seguridad INT,
  codigo_comuna INT,
  PRIMARY KEY (id_seguridad, codigo_comuna),
  FOREIGN KEY (id_seguridad) REFERENCES Seguridad(id_seguridad),
  FOREIGN KEY (codigo_comuna) REFERENCES Comuna(codigo_comuna)
);

-- Crear tabla Poseer
CREATE TABLE Poseer (
  id_indice_educativo INT,
  codigo_comuna INT,
  PRIMARY KEY (id_indice_educativo, codigo_comuna),
  FOREIGN KEY (id_indice_educativo) REFERENCES Indices_educativos(id_indice_educativo),
  FOREIGN KEY (codigo_comuna) REFERENCES Comuna(codigo_comuna)
);
