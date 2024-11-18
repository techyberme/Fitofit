DROP DATABASE IF EXISTS DB_FITOFITO;
CREATE DATABASE DB_FITOFITO;

USE DB_FITOFITO;
DROP TABLE IF EXISTS EVENTOS;
DROP TABLE IF EXISTS USUARIOS;
DROP TABLE IF EXISTS USUARIOACTIVIDAD;
DROP TABLE IF EXISTS DEPORTES;
DROP TABLE IF EXISTS ACTIVIDADES;
CREATE TABLE EVENTOS ( ID_EVENTO VARCHAR(10) NOT NULL,
		       FECHA DATE,
			HORA TIME,
			PRECIO DECIMAL(5,2),
			LOCALIZACION VARCHAR(100),
			PLAZAS INT(11),
			PRIMARY KEY (ID_EVENTO))
	ENGINE= InnoDB;

CREATE TABLE USUARIOS ( ID_USUARIO VARCHAR(15) NOT NULL,
			NOMBRE_USUARIO VARCHAR(40),
			CORREO VARCHAR(40),
			CONTRASENA VARCHAR(30),			
			FECHA_NAC DATE,
			SEXO CHAR(1) NOT NULL,
			PRIMARY KEY (ID_USUARIO))
	ENGINE = InnoDB;

CREATE TABLE USUARIOACTIVIDAD( ID_USUARIO VARCHAR(15) NOT NULL,
				ID_ACTIVIDAD VARCHAR(10) NOT NULL,
				PRIMARY KEY (ID_USUARIO,ID_ACTIVIDAD),
				FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS(ID_USUARIO) ON DELETE RESTRICT)
	ENGINE= InnoDB;

CREATE TABLE DEPORTES(NOMBRE_DEPORTE VARCHAR(30),
		      TIPO_DEPORTE   VARCHAR(20),
		      EQUIPO CHAR(1) NOT NULL,
			PRIMARY KEY(NOMBRE_DEPORTE))
ENGINE= InnoDB;





CREATE TABLE ACTIVIDADES(ID_ACTIVIDAD VARCHAR(10) NOT NULL,
			NOMBRE_ACTIVIDAD VARCHAR(100),
			TEXTO VARCHAR(140),
			KM FLOAT,
			FC INTEGER,
			KCAL INTEGER,
			DURACION  TIME,
			ID_EVENTO VARCHAR(30) ,
			NOMBRE_DEPORTE VARCHAR(30),
			PRIMARY KEY(ID_ACTIVIDAD),
			FOREIGN KEY(ID_EVENTO) REFERENCES EVENTOS(ID_EVENTO),
			FOREIGN KEY(NOMBRE_DEPORTE) REFERENCES DEPORTES(NOMBRE_DEPORTE))
ENGINE= InnoDB;





 



INSERT INTO EVENTOS (ID_EVENTO, FECHA, HORA, PRECIO, LOCALIZACION, PLAZAS) VALUES 

('EV_001', '2025-02-05', '19:15', 18.03, 'Calle Tetuán, Sevilla', 32), 

('EV_002', '2025-03-10', '21:15', 26.09, 'Calle San Fernando, Sevilla', 61), 

('EV_003', '2025-04-21', '12:30', 36.27, 'Calle San Fernando, Sevilla', 49), 

('EV_004', '2024-11-19', '16:00', 18.17, 'Calle Marques de Larios, Málaga', 56), 

('EV_005', '2025-03-01', '11:45', 98.64, 'Paseo Marítimo, Cádiz', 47), 

('EV_006', '2024-11-23', '17:45', 5.92, 'Calle Colón, Valencia', 86), 

('EV_007', '2025-04-14', '13:45', 73.07, 'Calle Colón, Valencia', 27), 

('EV_008', '2024-12-05', '17:30', 69.22, 'Calle Mayor, Valencia', 76), 

('EV_009', '2025-02-16', '15:15', 58.17, 'Calle Estafeta, Pamplona', 84), 

('EV_010', '2025-03-18', '12:00', 12.65, 'Rambla Nova, Tarragona', 86), 

('EV_011', '2025-03-02', '21:45', 80.87, 'Avenida Diagonal, Barcelona', 69), 

('EV_012', '2024-11-21', '21:00', 63.82, 'Calle Gran Vía, Madrid', 14), 

('EV_013', '2024-12-17', '17:00', 66.70, 'Avenida de la Constitución, Sevilla', 70), 

('EV_014', '2025-05-09', '13:15', 45.71, 'Paseo de Gracia, Barcelona', 76), 

('EV_015', '2025-04-07', '16:15', 43.65, 'Calle Alfonso I, Zaragoza', 28), 

('EV_016', '2025-02-04', '20:45', 82.17, 'Gran Vía, Granada', 11), 

('EV_017', '2025-04-30', '13:15', 36.64, 'Paseo de Gracia, Barcelona', 14), 

('EV_018', '2025-03-04', '17:00', 7.55, 'Paseo Marítimo, Cádiz', 40), 

('EV_019', '2024-11-26', '21:45', 74.39, 'Calle Marques de Larios, Málaga', 47), 

('EV_020', '2025-04-12', '18:15', 51.67, 'Calle Alfonso I, Zaragoza', 19), 

('EV_021', '2023-05-13', '08:15', 80.00, 'Paseo de la Independencia, Zaragoza', 300), 

('EV_022', '2024-05-19', '10:15', 75.60, 'Paseo de la Castellana, Madrid', 250),

('EV_023', '2025-06-23, '11:15', 68.60, 'Paseo de Gracia, Barcelona', 290); 
	

INSERT INTO USUARIOS (ID_USUARIO, NOMBRE_USUARIO, CORREO, CONTRASENA, FECHA_NAC, SEXO) VALUES 

('id_usuario_1', 'Ricardo Torres', 'ricardo@hotmail.com', 'hFxN^@E@IS', '1965-11-29', 'M'), 

('id_usuario_2', 'Laura Navarro', 'laura@gmail.com', 'ssFN5TAMUf', '1970-11-28', 'F'), 

('id_usuario_3', 'Juan Rodríguez', 'juan@outlook.com', '(Qpo3JxSs%', '2005-11-19', 'M'), 

('id_usuario_4', 'Luis García', 'luis@yahoo.com', 'lnIUrYw(F)', '1994-11-22', 'M'), 

('id_usuario_5', 'Raúl Ruiz', 'raúl@outlook.com', 'vZx9OcG)fX', '1981-11-25', 'M'), 

('id_usuario_6', 'Andrés Torres', 'andrés@outlook.com', 'xm@a2gxkq7', '1995-11-22', 'M'), 

('id_usuario_7', 'Elena López', 'elena@gmail.com', 'MV*3%LPAOS', '1975-11-27', 'F'), 

('id_usuario_8', 'Sara Pérez', 'sara@hotmail.com', 'Tm8#YOjq!f', '1966-11-29', 'F'), 

('id_usuario_9', 'María Ramírez', 'maría@gmail.com', 'ZFJEZ(abeV', '1964-11-29', 'F'), 

('id_usuario_10', 'Sofía Alonso', 'sofía@outlook.com', 'ZgneA4(h4T', '2000-11-20', 'F'), 

('id_usuario_11', 'Paula García', 'paula@outlook.com', 'MSdksj)86E', '1977-11-26', 'F'), 

('id_usuario_12', 'Alberto Rodríguez', 'alberto@hotmail.com', '0kEyb)iOVa', '1999-11-21', 'M'), 

('id_usuario_13', 'Cristina Sánchez', 'cristina@hotmail.com', '3QA7D2m!vo', '1989-11-23', 'F'), 

('id_usuario_14', 'Marta Hernández', 'marta@hotmail.com', '&)IyFTKB0z', '2006-11-19', 'F'), 

('id_usuario_15', 'Clara Romero', 'clara@yahoo.com', 'VM8j4b9T*x', '2005-11-19', 'F'), 

('id_usuario_16', 'Eva Moreno', 'eva@hotmail.com', '&F^j)3khF(', '1969-11-28', 'F'), 

('id_usuario_17', 'Luis López', 'luis@yahoo.com', 'Ha3zdX0OPn', '1971-11-28', 'M'), 

('id_usuario_18', 'Raúl Gutiérrez', 'raúl@hotmail.com', '7@fAvbdzwT', '2003-11-20', 'M'), 

('id_usuario_19', 'Clara Gutiérrez', 'clara@outlook.com', 'pygF*2v&jB', '1972-11-27', 'F'), 

('id_usuario_20', 'Ricardo Navarro', 'ricardo@hotmail.com', 'Ct2tRvQ3R)', '1991-11-23', 'M'), 

('id_usuario_21', 'Clara Martínez', 'clara@hotmail.com', 'v^x0vpz@no', '1972-11-27', 'F'), 

('id_usuario_22', 'Eva González', 'eva@hotmail.com', 'hDrDHkBxfB', '1991-11-23', 'F'), 

('id_usuario_23', 'Alberto Fernández', 'alberto@outlook.com', 'Fx%7MWl%tR', '1981-11-25', 'M'), 

('id_usuario_24', 'Cristina Torres', 'cristina@yahoo.com', 'K)iQbF5pCD', '1966-11-29', 'F'), 

('id_usuario_25', 'Alberto Fernández', 'alberto@yahoo.com', 'i61OpAT&gw', '1990-11-23', 'M'), 

('id_usuario_26', 'Alberto Gutiérrez', 'alberto@hotmail.com', 'nX7bw&s^jJ', '1974-11-27', 'M'), 

('id_usuario_27', 'Andrés Ruiz', 'andrés@outlook.com', 'K&dyBBPQ6)', '2002-11-20', 'M'), 

('id_usuario_28', 'Pablo Torres', 'pablo@yahoo.com', '!QyUgvxl&M', '2006-11-19', 'M'), 

('id_usuario_29', 'María Rodríguez', 'maría@gmail.com', 'QgthZuFX(t', '1966-11-29', 'F'), 

('id_usuario_30', 'Sara Fernández', 'sara@yahoo.com', 'tMx)Uu(T9I', '1978-11-26', 'F'); 


INSERT INTO DEPORTES (NOMBRE_DEPORTE, TIPO_DEPORTE, EQUIPO) VALUES 

	('Fútbol', 'clásicos', 'S'), 

	('Surf', 'acuáticos', 'N'), 

	('Escalada', 'extremos', 'N'), 

	('Baloncesto', 'clásicos', 'S'), 

	('Natación', 'acuáticos', 'N'), 

	('Rugby', 'clásicos', 'S'), 

	('Kitesurf', 'acuáticos', 'N'), 

	('Parapente', 'extremos', 'N'), 

	('Voleibol', 'clásicos', 'S'), 

	('Buceo', 'acuáticos', 'N'), 
	('Carrera', 'clásicos', 'N'),
	('Gym', 'clásicos', 'N'), 
	('Yoga', 'clásicos', 'N'),
	('Ping Pong','clásicos','N');

INSERT INTO ACTIVIDADES(ID_ACTIVIDAD, NOMBRE_ACTIVIDAD, TEXTO, KM, FC, KCAL, DURACION, ID_EVENTO, NOMBRE_DEPORTE) VALUES 

('id_act1', 'Carrera 5K', 'Una carrera divertida de 5 kilómetros', 5, 150, 350, '00:30:00', 'EV_001', 'Carrera'), 

('id_act2', 'Natación Libre', 'Sesión de natación libre', 2, 120, 200, '00:45:00', 'EV_002', 'Natación'), 

('id_act3', 'Clase de Yoga', 'Clase de yoga para relajarse', NULL, 80, 150, '01:00:00', 'EV_003', 'Yoga'), 

('id_act4', 'Fútbol Amistoso', 'Partido de fútbol amistoso', NULL, 140, 500, '01:30:00', 'EV_004', 'Fútbol'), 

('id_act5', 'Voleibol Playa', 'Partido de voleibol en la playa', NULL, 130, 400, '01:00:00', 'EV_005', 'Voleibol'), 

('id_act6', 'Rugby Infantil', 'Partido para niños', NULL, 110, 300, '00:40:00', 'EV_006', 'Rugby'), 

('id_act7', 'Escalada', 'Sesión de escalada en roca', NULL, 160, 450, '02:00:00', 'EV_007', 'Escalada'), 

('id_act8', 'Ping Pong', 'Torneo de ping pong', NULL, 100, 100, '00:30:00', 'EV_008', 'Ping Pong'), 

('id_act9', 'Maratón', 'Maratón completo en la ciudad', 42.2, 170, 3000, '04:00:00', 'EV_009', 'Carrera'), 

('id_act10', 'Kitesurf', 'Curso de kitesurf para principiantes', NULL, 140, 600, '01:20:00', 'EV_010', 'Kitesurf'),
	('id_act11', 'Maratón', 'Maratón completo en la ciudad', 42, 160, 2500, '04:23:01', 'EV_011', 'Atletismo'), 

('id_act12, 'Maratón', 'Maratón completo en la ciudad', 42, 175, 2200, '03:34:18', 'EV_012', 'Atletismo'), 

('id_act13, 'Maratón', 'Maratón Zaragoza', 42, 175, 2200, '03:34:18', 'EV_021', 'Atletismo'), 

('id_act14, 'Maratón', 'Maratón completo en Zaragoza', 42, 175, 2200, '03:34:18', 'EV_021', 'Atletismo'), 

('id_act15, 'Maratón', 'Maratón con amigos Madrid', 42, 175, 2200, '03:34:18', 'EV_022', 'Atletismo'), 

('id_act16, 'Maratón', 'Maratón  de Barcelona', 42, 175, 2200, '03:34:18', 'EV_023', 'Atletismo'), 

('id_act17', 'Partido Futbol Amistoso', 'Partido amistoso de fútbol con amigos', 0, 145, 700, '01:30:00', NULL, 'Futbol'),  

('id_act18', 'Entrenamiento Futbol', 'Sesión de entrenamiento técnico y táctico', 0, 135, 500, '01:00:00', NULL, 'Futbol'), 

 ('id_act19', 'Torneo Futbol 5', 'Participación en torneo de fútbol 5 vs 5', 0, 150, 600, '00:50:00', NULL, 'Futbol'), 

('id_act20', 'Surf Libre', 'Surf libre en olas medianas', 0, 120, 400, '00:45:00', NULL, 'Surf'),  

('id_act21', 'Entrenamiento Surf', 'Práctica de maniobras y equilibrio', 0, 110, 350, '01:00:00', NULL, 'Surf'),  

('id_act22', 'Competencia Surf', 'Participación en competencia local', 0, 130, 500, '01:15:00', NULL, 'Surf'), 

('id_act23', 'Escalada en Roca', 'Escalada al aire libre en roca natural', 0, 130, 600, '02:00:00', NULL, 'Escalada'),  

('id_act24', 'Boulder en Rocódromo', 'Práctica de boulder en rocódromo', 0, 140, 450, '01:30:00', NULL, 'Escalada'),  

('id_act25', 'Escalada en Vía Larga', 'Ascenso de varias rutas en vía larga', 0, 120, 700, '03:00:00', NULL, 'Escalada'), 

('id_act26', 'Partido Baloncesto Amistoso', 'Partido amistoso con compañeros de equipo', 0, 130, 550, '01:00:00', NULL, 'Baloncesto'), 

 ('id_act27', 'Entrenamiento Baloncesto', 'Práctica de tiros y jugadas tácticas', 0, 125, 400, '00:45:00', NULL, 'Baloncesto'),  

('id_act28', 'Torneo Baloncesto', 'Participación en torneo local', 0, 140, 700, '01:30:00', NULL, 'Baloncesto'), 

('id_act29', 'Entrenamiento Natación', 'Sesión de entrenamiento de resistencia en piscina', 0, 125, 400, '00:45:00', NULL, 'Natación'),  

('id_act30', 'Natación Libre', 'Natación recreativa en piscina olímpica', 0, 110, 350, '00:30:00', NULL, 'Natación'), 

 ('id_act31', 'Competencia Natación', 'Participación en competencia de estilo libre', 0, 135, 600, '01:00:00', NULL, 'Natación'), 

('id_act32', 'Partido Rugby Amistoso', 'Partido amistoso de rugby con el equipo', 0, 150, 800, '01:20:00', NULL, 'Rugby'), 

('id_act33', 'Entrenamiento Rugby', 'Entrenamiento de fuerza y tácticas de juego', 0, 140, 600, '01:00:00', NULL, 'Rugby'), 

('id_act34', 'Torneo Rugby', 'Participación en torneo regional de rugby', 0, 160, 900, '01:30:00', NULL, 'Rugby'), 

('id_act35', 'Kitesurf en Playa', 'Práctica de kitesurf en condiciones de viento moderado', 0, 130, 500, '01:00:00', NULL, 'Kitesurf'), 

('id_act36', 'Competencia Kitesurf', 'Participación en competencia de freestyle', 0, 140, 700, '01:30:00', NULL, 'Kitesurf'), 

('id_act37', 'Entrenamiento Kitesurf', 'Sesión de entrenamiento de maniobras avanzadas', 0, 120, 450, '00:50:00', NULL, 'Kitesurf'),

('id_act38', 'Vuelo de Parapente en Montaña', 'Vuelo sobre un paisaje montañoso con vistas panorámicas', 0, 90, 250, '01:00:00', NULL, 'Parapente'), 
 

('id_act39', 'Entrenamiento de Parapente', 'Práctica de control y maniobras en parapente', 0, 85, 200, '00:45:00', NULL, 'Parapente'), 
 

('id_act40', 'Competencia de Parapente', 'Participación en una competencia de vuelo de distancia', 0, 100, 300, '02:30:00', NULL, 'Parapente'),

 

('id_act41', 'Partido de Volleyball', 'Juego recreativo de volleyball en la playa', 0, 120, 350, '01:15:00', NULL, 'Volley'),  

('id_act42', 'Entrenamiento de Volleyball', 'Práctica de recepción, saque y bloqueo', 0, 110, 300, '01:00:00', NULL, 'Volley'), 

('id_act43', 'Torneo de Volleyball', 'Competencia en un torneo local de volleyball', 0, 130, 400, '02:00:00', NULL, 'Volley'),

('id_act44', 'Buceo en Arrecife', 'Exploración de arrecifes de coral', 0, 100, 300, '01:20:00', NULL, 'Buceo'),  

('id_act45', 'Buceo Nocturno', 'Inmersión nocturna con observación de fauna marina', 0, 95, 280, '01:00:00', NULL, 'Buceo'),  

('id_act46', 'Práctica de Buceo', 'Sesión de entrenamiento en aguas abiertas', 0, 105, 320, '01:30:00', NULL, 'Buceo'); 

 

INSERT INTO USUARIOACTIVIDAD (ID_USUARIO, ID_ACTIVIDAD) VALUES 

('id_usuario_1', 'id_act2'), 

('id_usuario_1', 'id_act3'), 

('id_usuario_2', 'id_act4'), 

('id_usuario_2', 'id_act5'), 

('id_usuario_3', 'id_act1'), 

('id_usuario_3', 'id_act6'), 

('id_usuario_4', 'id_act7'), 

('id_usuario_4', 'id_act8'), 

('id_usuario_5', 'id_act9'), 

('id_usuario_5', 'id_act10'), 

('id_usuario_6', 'id_act2'), 

('id_usuario_6', 'id_act4'), 

('id_usuario_7', 'id_act5'), 

('id_usuario_7', 'id_act7'), 

('id_usuario_8', 'id_act1'), 

('id_usuario_8', 'id_act3'), 

('id_usuario_9', 'id_act8'), 

('id_usuario_9', 'id_act9'), 

('id_usuario_10', 'id_act6'), 

('id_usuario_10', 'id_act10'),
 
('id_usuario_1', 'id_act13'), 

('id_usuario_2', 'id_act13'), 

('id_usuario_3', 'id_act14'), 

('id_usuario_4', 'id_act15'), 

('id_usuario_5', 'id_act15'), 

('id_usuario_6', 'id_act15'), 

('id_usuario_7', 'id_act16'), 

('id_usuario_8', 'id_act16'), 

('id_usuario_1', 'id_act19'), 

('id_usuario_1', 'id_act17'), 

('id_usuario_1', 'id_act18'), 

('id_usuario_2’, 'id_act20'), 

('id_usuario_2’, 'id_act21'), 

('id_usuario_2’, 'id_act22'), 

('id_usuario_3’, 'id_act23'), 

('id_usuario_3’, 'id_act24'), 

('id_usuario_3’, 'id_act25'), 

('id_usuario_4’, 'id_act26'), 

('id_usuario_4’, 'id_act27'), 

('id_usuario_4’, 'id_act28'), 

('id_usuario_5’, 'id_act29'), 

('id_usuario_5’, 'id_act30'), 

('id_usuario_5’, 'id_act31'), 

('id_usuario_6’, 'id_act32'), 

('id_usuario_6’, 'id_act33'), 

('id_usuario_6’, 'id_act34'), 

('id_usuario_7', 'id_act35'), 

('id_usuario_7', 'id_act36'), 

('id_usuario_7', 'id_act37'), 

('id_usuario_8', 'id_act38'), 

('id_usuario_8', 'id_act39'), 

('id_usuario_8', 'id_act40'), 

('id_usuario_9', 'id_act41'), 

('id_usuario_9', 'id_act42'), 

('id_usuario_9', 'id_act43'), 

('id_usuario_10', 'id_act44'), 

('id_usuario_10', 'id_act45'), 

('id_usuario_10', 'id_act46'), 

('id_usuario_8', 'id_act13');



##Falta tabla eventos usuario



















			
			
