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
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `Appointment_id` int NOT NULL AUTO_INCREMENT,
  `p_id` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `a_date` date DEFAULT NULL,
  PRIMARY KEY (`Appointment_id`),
  KEY `p_id` (`p_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `patient` (`p_id`),
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES (1,1,2,'2023-08-28'),(2,1,2,'2023-08-28'),(4,1,2,'2023-08-28'),(5,1,2,'2023-08-28'),(15,1,2,'2023-08-28'),(16,1,2,'2023-08-28'),(17,1,2,'2023-08-28'),(18,1,2,'2023-08-28'),(19,1,2,'2023-08-28'),(20,1,2,'2023-08-28'),(21,1,2,'2023-08-28'),(22,1,2,'2023-08-28'),(23,1,2,'2023-08-28'),(24,1,2,'2023-08-28'),(25,1,2,'2023-08-28'),(26,1,3,'2023-08-28'),(27,1,2,'2023-08-28'),(28,1,2,'2023-08-28'),(29,1,2,'2023-08-28'),(30,1,2,'2023-08-28'),(31,1,2,'2023-08-28'),(32,1,2,'2023-08-28'),(33,1,2,'2023-08-28'),(34,1,2,'2023-08-28'),(35,1,2,'2023-08-28'),(36,1,2,'2023-08-28'),(37,3,4,'2023-08-28'),(38,1,2,'2023-08-28'),(39,1,3,'2023-08-28'),(40,3,3,'2023-08-28'),(41,1,2,'2023-08-28'),(42,1,2,'2023-08-29'),(43,1,2,'2023-08-29'),(44,1,2,'2023-08-29'),(45,1,2,'2023-08-29'),(46,1,2,'2023-08-29'),(47,1,2,'2023-08-29'),(48,1,2,'2023-08-29'),(49,1,4,'2023-08-29'),(50,1,4,'2023-08-29'),(51,1,4,'2023-08-29'),(52,1,5,'2023-08-29'),(53,1,5,'2023-08-29'),(54,1,5,'2023-08-29'),(55,1,1,'2023-08-29'),(56,1,1,'2023-08-29'),(57,1,2,'2023-08-29'),(58,1,2,'2023-08-29'),(59,1,2,'2023-08-29'),(60,1,8,'2023-08-29'),(61,3,1,'2023-08-29'),(62,3,2,'2023-08-29'),(63,3,2,'2023-08-29'),(64,1,2,'2023-08-29'),(65,3,2,'2023-08-29'),(66,1,3,'2023-08-29'),(67,2,3,'2023-08-30'),(68,2,2,'2023-08-30'),(69,3,3,'2023-08-30'),(70,3,2,'2023-08-30'),(71,1,2,'2023-08-30'),(72,4,2,'2023-08-30'),(74,1,2,'2023-08-30');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
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
