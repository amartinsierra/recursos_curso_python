CREATE DATABASE  IF NOT EXISTS `academia` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `academia`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: academia
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumnos`
--

DROP TABLE IF EXISTS `alumnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumnos` (
  `idAlumno` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `curso` varchar(45) DEFAULT NULL,
  `nota` double DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idAlumno`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumnos`
--

LOCK TABLES `alumnos` WRITE;
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
INSERT INTO `alumnos` VALUES (1,'prueba','Java',5,'prueba@gmail.com'),(2,'profe','java',6,'profe@gmail.com'),(4,'nuevo','Java',4,'nuev@gmail'),(5,'otro','Java',5,'nn@gmail.com'),(31,'jdbc1','Angular',7,'jdbc@gmail.com'),(35,'hibernate','jpa',8,'dddd'),(39,'jdbc','Java',3,'jdbc@gmail.com'),(42,'jdbc','java',3,'ddd'),(43,'pruebaX','lenguaje X',9,'xxx@gmail.com'),(44,'profe python','bases de datos',5,'profe@gmail.com');
/*!40000 ALTER TABLE `alumnos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-26 13:45:57
CREATE DATABASE  IF NOT EXISTS `formacion` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `formacion`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: formacion
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumnos`
--

DROP TABLE IF EXISTS `alumnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumnos` (
  `usuario` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `edad` int unsigned NOT NULL,
  PRIMARY KEY (`usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumnos`
--

LOCK TABLES `alumnos` WRITE;
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
INSERT INTO `alumnos` VALUES ('aaa','sseeeee','ordenador','ss@dd.es',45),('admin','a','tomates','servlet@gmail.com',22),('admin5','aaaa','dsd','dssd',22),('dd','m37MbuuDq/mt4Q/jiGXfRJm+NWjcxQeuLsO0SYnLAJM=','fdsf','dsfds@gg.es',11),('dfds','ddeeeeee','tomates','ssd@dd.es',22),('diego armando','diego','diego','diego',0),('fd','g','df','g',4),('java','OKCWOmNksJrYZ6qaZsbQCWc8IeGCAVRh2iNuw2GHf3c=','java','java@dd.com',33),('javato','T6GEvvueoevbXxbeTLMz6fk5FLZHd1RtUBcKFUes8U0=','aaa','asas@fff.es',33),('model','model','model','model@gmail',55),('mvcform','mvcform','form','form@gmail.com',22),('noexiste','wq','tomates','mvc@gmail.com',22),('nuevo','nuevo','h','nuevo@gmail.com',22),('nuevo10','nuevo10','nuevo','nuevo@gmail.com',22),('paco','aaa','paco','dsfads',333),('paquito','aaaa','dsdas','asdas',55),('probando','qqqqqqq','probando','probando@gmail.com',23),('prof','UdHmo5isvafhW2h950fn3+lfoTFU3LQKqKs38eKzk6A=','servlet@gmail.com','profe',33),('qa','qaq','ww','qw',34),('qq','qq','qqqqqqqqqq','qq',22),('qqq','qqqqqqqq','sdsad','asdasd@dd.es',45),('test1','test1','test1','test1@gmail.com',99),('ty','rr','rtgre','rte',55),('uno','vw7DaU4SLgZ9mWSjjsfYQVeB30sk9EKtdntGIfuY+MU=','profe','profe@gmail.com',22),('webmvc','webmvc','webmvc','webmvc',333);
/*!40000 ALTER TABLE `alumnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cursos`
--

DROP TABLE IF EXISTS `cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cursos` (
  `idCurso` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `duracion` int unsigned NOT NULL,
  `fechaInicio` date DEFAULT NULL,
  `precio` double DEFAULT NULL,
  PRIMARY KEY (`idCurso`),
  UNIQUE KEY `uk_curso_nombre_fecha` (`nombre`,`fechaInicio`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
INSERT INTO `cursos` VALUES (1,'java 10',100,'2020-08-20',250),(2,'python',50,'2020-10-12',125),(3,'php',25,'2020-10-30',345),(4,'jsf',30,'2020-04-15',100),(5,'ordenador',120,'2020-11-08',2),(6,'angular 9',60,'2020-11-19',170),(7,'javascript',60,'2020-11-26',160),(8,'microservicios spring boot',70,'2020-11-24',390),(9,'servlet',60,'2020-11-17',0),(10,'php7',11,'2020-11-18',0),(11,'ordenador',67,'2020-12-03',0),(12,'jpa',12,'2020-12-03',0),(13,'myjava',45,'2020-12-08',0),(14,'Kubernates',60,'2021-02-11',0),(15,'dockers completo',70,'2020-12-20',0),(16,'Spring',50,'2021-05-17',0),(17,'kafka',70,'2021-06-30',0),(18,'ww',23,'2021-05-14',0);
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matriculas`
--

DROP TABLE IF EXISTS `matriculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matriculas` (
  `usuario` varchar(45) NOT NULL,
  `idCurso` int unsigned NOT NULL,
  `nota` double NOT NULL DEFAULT '0',
  PRIMARY KEY (`usuario`,`idCurso`),
  KEY `FKhr6mvvff63pmqimncbh95juay` (`idCurso`),
  CONSTRAINT `FKhr6mvvff63pmqimncbh95juay` FOREIGN KEY (`idCurso`) REFERENCES `cursos` (`idCurso`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matriculas`
--

LOCK TABLES `matriculas` WRITE;
/*!40000 ALTER TABLE `matriculas` DISABLE KEYS */;
INSERT INTO `matriculas` VALUES ('aaa',1,0),('aaa',4,0),('aaa',17,0),('admin',1,0),('admin',2,0),('admin',6,3),('admin',14,0),('dd',17,0),('dfds',1,0),('diego armando',2,0),('diego armando',13,7),('model',1,0),('model',3,0),('model',4,0),('model',7,0),('paco',1,0),('paco',2,8),('probando',1,7),('prof',17,5),('test1',1,0),('uno',1,5),('uno',7,3),('uno',17,0),('webmvc',1,4),('webmvc',2,7),('webmvc',5,8),('webmvc',6,0),('webmvc',9,5),('webmvc',12,3),('webmvc',13,9);
/*!40000 ALTER TABLE `matriculas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preguntas`
--

DROP TABLE IF EXISTS `preguntas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `preguntas` (
  `idPregunta` int unsigned NOT NULL AUTO_INCREMENT,
  `idCurso` int unsigned NOT NULL,
  `enunciado` varchar(200) NOT NULL,
  PRIMARY KEY (`idPregunta`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preguntas`
--

LOCK TABLES `preguntas` WRITE;
/*!40000 ALTER TABLE `preguntas` DISABLE KEYS */;
INSERT INTO `preguntas` VALUES (1,1,'¿Cuantos bytes ocupa el tipo int?'),(2,1,'¿Cual es una palabra reservada de Java?');
/*!40000 ALTER TABLE `preguntas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `respuestas`
--

DROP TABLE IF EXISTS `respuestas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `respuestas` (
  `idRespuesta` int unsigned NOT NULL AUTO_INCREMENT,
  `idPregunta` int unsigned NOT NULL,
  `texto` varchar(150) NOT NULL,
  `correcta` tinyint(1) NOT NULL,
  PRIMARY KEY (`idRespuesta`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `respuestas`
--

LOCK TABLES `respuestas` WRITE;
/*!40000 ALTER TABLE `respuestas` DISABLE KEYS */;
INSERT INTO `respuestas` VALUES (1,1,'2',0),(2,1,'4',1),(3,1,'3',0),(4,1,'8',0),(5,2,'red',0),(6,2,'main',0),(7,2,'scanner',0),(8,2,'import',1);
/*!40000 ALTER TABLE `respuestas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-26 13:45:57
CREATE DATABASE  IF NOT EXISTS `centralpedidos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `centralpedidos`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: centralpedidos
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `idPedido` int NOT NULL AUTO_INCREMENT,
  `tienda` int NOT NULL,
  `producto` varchar(45) DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`idPedido`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
INSERT INTO `pedidos` VALUES (15,2,'balón',15,'2021-02-15'),(16,1,'pan',20,'2021-02-20'),(17,3,'cerveza',34,'2021-02-13'),(18,3,'impresora',180,'2021-03-03'),(19,1,'ordenador',730,'2021-02-19'),(20,2,'leche',6,'2021-02-25'),(21,1,'silla',130,'2021-03-01'),(22,3,'cuadernos',8,'2021-02-26'),(23,4,'vino',10,'2021-03-01'),(24,4,'lapiz',2,'2021-03-04'),(25,1,'ratón',15,'2021-02-14'),(26,2,'pan',5,'2021-04-06'),(27,2,'pan',6,'2021-06-15'),(31,1,'caramelos',9,'2021-08-20'),(32,2,'vino',10,'2021-03-01'),(33,3,'lapiz',2,'2021-03-04'),(34,3,'pelota',5,'2021-04-06'),(35,1,'pan',3,'2021-11-19'),(36,2,'vino',2,'2021-11-08'),(37,2,'pan',5,'2021-11-05');
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tiendas`
--

DROP TABLE IF EXISTS `tiendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tiendas` (
  `idTienda` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `responsable` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idTienda`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tiendas`
--

LOCK TABLES `tiendas` WRITE;
/*!40000 ALTER TABLE `tiendas` DISABLE KEYS */;
INSERT INTO `tiendas` VALUES (1,'tienda1','Madrid','A Perez'),(2,'tienda2','Valencia','J Martín'),(3,'tienda3','Sevilla','M Murillo'),(4,'tienda4','Sevilla','L Álvarez');
/*!40000 ALTER TABLE `tiendas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-26 13:45:57
CREATE DATABASE  IF NOT EXISTS `alumnoscursos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `alumnoscursos`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: alumnoscursos
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumnos`
--

DROP TABLE IF EXISTS `alumnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumnos` (
  `idAlumno` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `curso` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `nota` double DEFAULT NULL,
  PRIMARY KEY (`idAlumno`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumnos`
--

LOCK TABLES `alumnos` WRITE;
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
INSERT INTO `alumnos` VALUES (3,'a3','Python','a3@gmail.com',5.5),(4,'a4','Angular','a4@gmail.com',4.5),(11,'wewe','Java','ttttt@gmail.com',7.4),(12,'keyc','Java','keyc@gmail.com',9),(13,'keycsds','Java','keyssc@gmail.com',9),(14,'keyddddcsds','Java','kedddyssc@gmail.com',9),(15,'zzkeayfc','Java','aakeayf@gmail.com',9),(16,'jwt','Java','jwt@gmail.com',9),(18,'kafka','Python','kaafka@gmail.com',7.4),(19,'wert','Kafka','wert@gmail.com',7.4),(20,'gty','Kafka','gty@gmail.com',6),(29,'z4','Angular','z4@gmail.com',2.4),(30,'mayya1','Java','maya1@gmail.com',7.4),(35,'postman','Java','postity@gmail.com',10),(38,'apache','Kafka','apache@gmail.com',9),(81,'remote','HTML','remote@gmail.com',6),(82,'ffggggg','Java','awasd@gmail.com',8),(85,'este es nuevo','Java','keyc@gmail.com',9),(92,'aws3','Python','a3@gmail.com',5.5),(105,'new','Java','newjava@gmail.com',9),(106,'seguro','Python','seguro@gmail.com',10),(107,'estudiante x','JavaEE','x@gmail.com',9),(109,'alumno sin codigo','Java','sincodigo@gmail.com',8.5),(110,'otro sin codigo','Python','nocode@gmail.com',8.5),(111,'p1','a','bb',4),(112,'otro','Java','maya1@gmail.es',8),(113,'ffff','Python','a3@gmaildddcom',5.5),(114,'otro','Java34','mayadfsfsd1@gmail.es',8),(115,'otro','Javaeee34','mayadfsfewqd1@gmail.es',8),(116,'curso java noviembre','Java','nov@gmail.com',8);
/*!40000 ALTER TABLE `alumnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ediciones`
--

DROP TABLE IF EXISTS `ediciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ediciones` (
  `codigoCurso` int NOT NULL,
  `dia` int NOT NULL,
  `totalAlumnos` int DEFAULT NULL,
  `horario` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`codigoCurso`,`dia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ediciones`
--

LOCK TABLES `ediciones` WRITE;
/*!40000 ALTER TABLE `ediciones` DISABLE KEYS */;
INSERT INTO `ediciones` VALUES (5,23,15,'mañana'),(6,23,14,'tarde'),(11,30,18,'mañana');
/*!40000 ALTER TABLE `ediciones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-26 13:45:57
CREATE DATABASE  IF NOT EXISTS `bancabd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bancabd`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bancabd
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `dni` int unsigned NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `telefono` int unsigned NOT NULL,
  PRIMARY KEY (`dni`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1111,'Pepito','c/marte',1111),(2222,'Alicia','c/ jupiter',2222),(3333,'Marta','c/venus',3333),(7777,'Gustavo','bbbb',1111),(9898,'Irene','aaaa',1111),(11117777,'Luis','bbbb',1111);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuentas`
--

DROP TABLE IF EXISTS `cuentas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuentas` (
  `numeroCuenta` int unsigned NOT NULL,
  `saldo` double NOT NULL,
  `tipocuenta` varchar(45) NOT NULL,
  PRIMARY KEY (`numeroCuenta`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuentas`
--

LOCK TABLES `cuentas` WRITE;
/*!40000 ALTER TABLE `cuentas` DISABLE KEYS */;
INSERT INTO `cuentas` VALUES (1000,113020,'recibos'),(1234,570,'prueba2'),(2000,11400,'ahorro'),(3000,670,'recibos'),(4000,880,'ahorro'),(5000,6700,'recibos'),(9000,50000,'ahorro');
/*!40000 ALTER TABLE `cuentas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movimientos`
--

DROP TABLE IF EXISTS `movimientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movimientos` (
  `idMovimiento` int unsigned NOT NULL AUTO_INCREMENT,
  `idCuenta` int unsigned NOT NULL,
  `fecha` date DEFAULT NULL,
  `cantidad` double NOT NULL,
  `operacion` varchar(45) NOT NULL,
  PRIMARY KEY (`idMovimiento`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimientos`
--

LOCK TABLES `movimientos` WRITE;
/*!40000 ALTER TABLE `movimientos` DISABLE KEYS */;
INSERT INTO `movimientos` VALUES (25,1000,'2019-03-31',200,'extracción'),(26,1000,'2019-03-31',600,'ingreso'),(27,2000,'2019-03-31',300,'extracción'),(28,1000,'2019-03-31',400,'ingreso'),(29,2000,'2019-03-31',2100,'ingreso'),(30,1000,'2019-03-31',135,'ingreso'),(31,1000,'2019-03-31',200,'extracción'),(32,1000,'2019-03-31',1100,'ingreso'),(33,1000,'2019-03-31',500,'extracción'),(34,1000,'2019-03-31',105,'ingreso'),(35,1000,'2019-04-04',123,'ingreso'),(36,1000,'2019-04-04',34,'extracción'),(37,1000,'2019-04-04',11,'extracción'),(38,1000,'2019-04-04',11,'extracción'),(39,1000,'2019-06-26',300,'extracción'),(40,1000,'2019-06-27',50000,'extracción'),(41,2000,'2019-06-27',50100,'ingreso'),(42,1000,'2019-06-27',3000,'extracción'),(43,2000,'2019-06-27',3100,'ingreso'),(44,1000,'2019-06-27',2000,'extracción'),(45,2000,'2019-06-27',2100,'ingreso'),(46,1000,'2019-06-27',2000,'extracción'),(47,2000,'2019-06-27',2100,'ingreso'),(48,1000,'2019-06-27',1111,'extracción'),(49,1000,'2019-10-25',556,'ingreso'),(50,1000,'2019-12-17',2100,'ingreso'),(51,1000,'2019-12-20',20000,'extracción'),(52,1000,'2019-12-20',1100,'ingreso'),(53,1000,'2020-08-20',400,'extracción'),(54,1000,'2020-09-06',3100,'ingreso'),(55,1000,'2020-09-07',1500,'extracción'),(56,1000,'2020-09-09',4100,'ingreso'),(57,1000,'2020-11-30',10100,'ingreso'),(58,2000,'2020-11-30',5100,'ingreso'),(59,1000,'2020-11-30',5000,'extracción'),(60,1000,'2021-04-08',4000,'Extracción'),(61,1000,'2021-12-09',4100,'ingreso'),(62,1000,'2021-12-09',200,'extracción'),(63,1234,'2021-12-09',600,'ingreso'),(64,1000,'2021-12-09',500,'extracción'),(65,2000,'2022-03-22',600,'ingreso'),(66,2000,'2022-03-22',4000,'extracción'),(67,2000,'2022-03-22',600,'extracción'),(68,1000,'2022-03-22',700,'ingreso'),(69,2000,'2022-03-22',3100,'ingreso'),(70,1000,'2022-10-21',1500,'ingreso'),(71,2000,'2022-10-24',2500,'extracción'),(72,1000,'2026-09-02',23,'extracción'),(73,1000,'2026-09-02',50,'extracción'),(74,1000,'2026-09-15',45,'ingreso'),(75,1000,'2026-09-15',25,'ingreso'),(76,1000,'2026-09-15',50,'ingreso'),(77,1000,'2026-09-15',50000,'ingreso'),(78,1000,'2026-09-15',10000,'ingreso'),(79,1000,'2026-09-15',10000,'ingreso');
/*!40000 ALTER TABLE `movimientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sucursales`
--

DROP TABLE IF EXISTS `sucursales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sucursales` (
  `nombre` varchar(50) NOT NULL,
  `codigoPostal` int NOT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `numeroEmpleados` int DEFAULT NULL,
  PRIMARY KEY (`nombre`,`codigoPostal`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sucursales`
--

LOCK TABLES `sucursales` WRITE;
/*!40000 ALTER TABLE `sucursales` DISABLE KEYS */;
/*!40000 ALTER TABLE `sucursales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `titulares`
--

DROP TABLE IF EXISTS `titulares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `titulares` (
  `idCuenta` int unsigned NOT NULL,
  `idCliente` int unsigned NOT NULL,
  PRIMARY KEY (`idCuenta`,`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `titulares`
--

LOCK TABLES `titulares` WRITE;
/*!40000 ALTER TABLE `titulares` DISABLE KEYS */;
INSERT INTO `titulares` VALUES (1000,1111),(1000,3333),(1000,7777),(1000,11117777),(1234,1111),(1234,3333),(2000,3333),(3000,2222),(4000,1111),(4000,2222),(5000,2222),(5000,9898),(9000,1111),(9000,2222);
/*!40000 ALTER TABLE `titulares` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-26 13:45:58
CREATE DATABASE  IF NOT EXISTS `libros` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `libros`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: libros
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `idCliente` int unsigned NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `telefono` int unsigned NOT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'test1','test1','test1@gmail.com',22222),(2,'test2','test2','test2@gmail.com',3333),(3,'test3','test3','afas',444),(4,'profe','profe','sadasd',234),(5,'ere','ff','aseea',23),(7,'fulano','mipassword','dfsfs@.es',343434),(8,'usuario_ejemplo','password_ejemplo','email@email.com',33333),(9,'miuser','mipass1','faddfs',3434),(14,'persiste','persiste','ddd',34),(16,'pepito','grillo','jajajaj',777777),(17,'mvc1','mvc1','sadas',1111),(18,'p1','p1','wwww',1111),(50,'mitienda','mitienda','mitienda@gmail.com',555),(51,'a','a','ajms66@gmail.com',333),(52,'asdas','q','servlet@gmail.com',333);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libros`
--

DROP TABLE IF EXISTS `libros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libros` (
  `isbn` int unsigned NOT NULL,
  `titulo` varchar(200) NOT NULL,
  `autor` varchar(45) DEFAULT NULL,
  `precio` double NOT NULL,
  `paginas` int unsigned DEFAULT NULL,
  `idTema` int unsigned NOT NULL,
  PRIMARY KEY (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros`
--

LOCK TABLES `libros` WRITE;
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
INSERT INTO `libros` VALUES (888,'Java 8','Gomez',26.62,300,1),(900,'Java 11','hilton',41.14,300,1),(987,'docker','sa',23,245,7),(6723,'Windows 20103','pears',19,170,2),(8767,'word','roberts',14,123,4),(9009,'excel','anónimo',27,300,4),(9999,'administración linux','angel lopez',30,370,2),(11123,'spring security','l2',24.2,0,1),(13667,'Machine Learning','Nelson',31,370,3),(26003,'docker','dfs',44,343,5),(27883,'Hadoop','Bryan',30,260,3),(30303,'Microservices','otro',54.45,600,1),(34215,'cisco','Martín',30,450,6),(40004,'diseño de página Web','alumnos',15,0,5),(43944,'programación python','engels',33.88,240,1),(60006,'JQuery','curso de Java',45,0,5),(70990,'docker','sa',66.55,22,1),(78011,'Java 15','Martín',36.3,450,1),(78080,'Angular xx',NULL,0,0,1),(93345,'Angular','pears',24,345,5),(123345,'Java 19','AA',26.62,300,1),(54654654,'fe','few',44,0,5);
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temas`
--

DROP TABLE IF EXISTS `temas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temas` (
  `idTema` int unsigned NOT NULL AUTO_INCREMENT,
  `tema` varchar(45) NOT NULL,
  PRIMARY KEY (`idTema`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temas`
--

LOCK TABLES `temas` WRITE;
/*!40000 ALTER TABLE `temas` DISABLE KEYS */;
INSERT INTO `temas` VALUES (1,'programación'),(2,'sistemas operativos'),(3,'big data'),(4,'ofimatica'),(5,'web'),(6,'redes'),(7,'devops'),(20,'r');
/*!40000 ALTER TABLE `temas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `idVenta` int unsigned NOT NULL AUTO_INCREMENT,
  `idCliente` int unsigned NOT NULL,
  `idLibro` int unsigned NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`idVenta`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (1,1,9999,'2010-09-01 11:49:21'),(2,1,11123,'2011-09-01 11:49:21'),(3,1,11123,'2012-09-01 11:49:21'),(4,1,11123,'2012-09-02 12:38:23'),(5,1,9999,'2012-09-02 12:38:23'),(6,1,8767,'2013-02-16 00:00:00'),(7,2,11123,'2015-02-16 00:00:00'),(8,1,9999,'2015-02-16 00:00:00'),(10,1,9999,'2016-06-05 00:00:00'),(11,1,900,'2018-08-13 11:29:10'),(12,1,43944,'2018-08-13 11:29:10'),(13,1,13667,'2021-11-17 12:29:00'),(14,1,78011,'2021-11-18 09:38:47'),(15,1,900,'2021-11-29 11:05:20'),(16,1,9999,'2021-11-29 11:05:20'),(17,1,27883,'2021-11-29 11:05:20'),(18,1,13667,'2022-03-07 12:22:45'),(19,1,27883,'2022-03-07 12:22:45'),(20,1,26003,'2022-03-07 12:44:13'),(21,1,27883,'2022-03-07 12:45:23'),(22,1,900,'2022-03-17 09:45:43'),(23,1,70990,'2022-03-17 09:45:43'),(24,1,888,'2022-03-22 12:02:47'),(25,1,888,'2022-03-22 12:02:47'),(26,1,27883,'2022-03-22 12:02:47'),(27,1,27883,'2022-03-22 12:02:47'),(28,1,78011,'2022-03-22 12:03:44'),(29,1,27883,'2022-03-28 10:04:45'),(30,1,43944,'2022-03-30 10:42:15'),(31,1,888,'2022-03-30 10:42:15');
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-26 13:45:58
