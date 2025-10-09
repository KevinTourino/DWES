/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.3-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mysitedb
-- ------------------------------------------------------
-- Server version	11.8.3-MariaDB-0+deb13u1 from Debian

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `tComentarios`
--

DROP TABLE IF EXISTS `tComentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `tComentarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comentario` varchar(2000) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `juego_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `juego_id` (`juego_id`),
  CONSTRAINT `tComentarios_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `tUsuarios` (`id`),
  CONSTRAINT `tComentarios_ibfk_2` FOREIGN KEY (`juego_id`) REFERENCES `tJuegos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tComentarios`
--

LOCK TABLES `tComentarios` WRITE;
/*!40000 ALTER TABLE `tComentarios` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `tComentarios` VALUES
(1,'Me encanta la libertad que ofrece este juego.',1,1),
(2,'La historia y los gráficos son impresionantes.',2,2),
(3,'Esperaba más optimización, pero la ambientación es brutal.',3,3),
(4,'Perfecto para jugar con amigos y crear mundos.',4,4),
(5,'La campaña es muy emocionante y divertida.',5,5);
/*!40000 ALTER TABLE `tComentarios` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `tJuegos`
--

DROP TABLE IF EXISTS `tJuegos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `tJuegos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `url_imagen` varchar(200) DEFAULT NULL,
  `plataforma` varchar(50) DEFAULT NULL,
  `año_lanzamiento` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tJuegos`
--

LOCK TABLES `tJuegos` WRITE;
/*!40000 ALTER TABLE `tJuegos` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `tJuegos` VALUES
(1,'The Legend of Zelda: Breath of the Wild','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSx0VFhbdcnUsce7j8y9uA11ayD_rx4d3XtA&s','Nintendo Switch',2017),
(2,'God of War','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvnQlTKA6OAG476zE1kLja_hzPoS0uxdyONA&s','PS4',2018),
(3,'Cyberpunk 2077','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLTzQrZkmLPDeFyNS3R2-G0rIkB-nRsZ0I8Q&s','PC',2020),
(4,'Minecraft','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcxBqMSPuVAvVHyReAw63NoX2v-BRer5vYjw&s','Multiplataforma',2011),
(5,'Halo Infinite','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuc8nxOdB56vhc9IUau3JlM-Z1GV1JJNErKw&s','Xbox Series X',2021);
/*!40000 ALTER TABLE `tJuegos` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `tUsuarios`
--

DROP TABLE IF EXISTS `tUsuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `tUsuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `contraseña` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tUsuarios`
--

LOCK TABLES `tUsuarios` WRITE;
/*!40000 ALTER TABLE `tUsuarios` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `tUsuarios` VALUES
(1,'Carlos','García Pérez','carlos.garcia@example.com','pass123'),
(2,'Laura','Martínez López','laura.martinez@example.com','pass456'),
(3,'Javier','Rodríguez Gómez','javier.rodriguez@example.com','pass789'),
(4,'Ana','Fernández Díaz','ana.fernandez@example.com','pass321'),
(5,'Miguel','Sánchez Ruiz','miguel.sanchez@example.com','pass654');
/*!40000 ALTER TABLE `tUsuarios` ENABLE KEYS */;
UNLOCK TABLES;
commit;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-10-09 11:34:39
