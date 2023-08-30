CREATE DATABASE  IF NOT EXISTS `hospital` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hospital`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `p_id` int NOT NULL AUTO_INCREMENT,
  `p_name` varchar(40) DEFAULT NULL,
  `p_contact` int DEFAULT NULL,
  `blood_group` varchar(6) DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (1,'akshay',876543191,'B+','M','Pune'),(2,'ajinkya',876043191,'B+','M','Pune'),(3,'jafar',87234491,'AB+','M','Pune'),(4,'Apkesha',87284491,'o+','F','Hyderabad'),(5,'bhawana',78284491,'A+','F','Bhatinda'),(8,'akshay',9845893,'B+','M','Pune'),(9,'akshay',9845893,'B+','M','Pune'),(15,'t',123465,'B+','MALE','Pune'),(16,'akshay',1234,'b+','FEMALE','pune'),(17,'akshay',546213879,'AB+','FEMALE','Pune'),(18,'asfkhj',89,'kj','FEMALE','kjh'),(19,'Omkar',789456231,'B+','MALE','Pune'),(20,'Omkar',78965431,'B+','MALE','Pune'),(21,'omkar',79865413,'B+','MALE','Pune'),(22,'omkar',789654,'B+','FEMALE','Pune'),(23,'akshsh',123,'b+','MALE','s,dh'),(24,'akshay',123,'B+','MALE','pune'),(25,'asdf',2,'B+','FEMALE','dsf'),(26,'akshay',78946321,'M','MALE','Pune'),(27,'12',12,'B+','MALE','PUNE'),(28,'akshay',789465132,'B+','MALE','Pune'),(29,'salijda',987,'B+','MALE','aslkjf'),(30,'ajinkya',78965413,'B+','MALE','Pune'),(31,'asd',98,'AB+','MALE','Pune'),(32,'akshay',98658974,'B+','MALE','Puen');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-30  9:23:01
