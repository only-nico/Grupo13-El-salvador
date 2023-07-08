-- Crear base de datos
CREATE DATABASE Medios;
-- Usar base de datos
USE Medios;
-- Crear tabla Medios_de_Comunicacion
CREATE TABLE Medios_de_Comunicacion (
  id_medio INT PRIMARY KEY,
  ubicacion VARCHAR(100),
  año_fundacion INT,
  cobertura VARCHAR(100),
  fundador VARCHAR(100)
);

-- Crear tabla Redes_Sociales
CREATE TABLE Redes_Sociales (
  nombre_red_social VARCHAR(100),
  nombre_usuario VARCHAR(100),
  seguidores INT,
  ultima_actualizacion DATE,
  id_medio INT,
  PRIMARY KEY (nombre_red_social, nombre_usuario),
  FOREIGN KEY (id_medio) REFERENCES Medios_de_Comunicacion(id_medio)
);

-- Crear tabla Sitios_web
CREATE TABLE Sitios_web (
  id_sitioweb INT PRIMARY KEY,
  url VARCHAR(500),
  id_medio INT,
  FOREIGN KEY (id_medio) REFERENCES Medios_de_Comunicacion(id_medio)
);

-- Crear tabla Categorias
CREATE TABLE Categorias (
  url_categoria VARCHAR(100),
  id_categoria INT PRIMARY KEY,
  nombre_categoria VARCHAR(100),
  xpath_categoria VARCHAR(500),
  id_sitioweb INT,
  FOREIGN KEY (id_sitioweb) REFERENCES Sitios_web(id_sitioweb)
);

-- Crear tabla Noticia
CREATE TABLE Noticia (
  id_noticia INT PRIMARY KEY,
  url_noticia VARCHAR(500),
  xpath_fecha VARCHAR(500),
  xpath_titulo VARCHAR(500),
  xpath_contenido VARCHAR(500),
  id_sitioweb INT,
  FOREIGN KEY (id_sitioweb) REFERENCES Sitios_web(id_sitioweb)
);
