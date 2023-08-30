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
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `doctor_id` int NOT NULL AUTO_INCREMENT,
  `d_name` varchar(40) DEFAULT NULL,
  `d_gender` varchar(10) DEFAULT NULL,
  `d_age` int DEFAULT NULL,
  `d_contact` varchar(20) DEFAULT NULL,
  `d_exp` int DEFAULT NULL,
  `d_charge` int DEFAULT NULL,
  `qualification` varchar(30) DEFAULT NULL,
  `specialties_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (1,'max ','M',37,'8967564534',10,500,'MBBS','GENERAL'),(2,'lewis ','M',47,'8967564534',20,1000,'MBBS, MS(cardio)','Cardiologist'),(3,'vettel ','M',45,'8237564534',20,1000,'MBBS, MS(ortho)','Orthologist'),(4,'anushka ','F',27,'8967564534',2,500,'MBBS, MS(cardio)','Cardiologist'),(5,'Essa bela','F',30,'8237564534',20,500,'MBBS, MS(ortho)','Orthologist'),(6,'akshay','M',20,NULL,NULL,NULL,NULL,NULL),(7,'ajinkya','M',21,NULL,NULL,NULL,NULL,NULL),(8,'ajinkya','M',21,NULL,NULL,NULL,NULL,NULL),(21,'arjun','M',36,'8529637413',12,1234,'MBBS,MS','Cardiologist'),(22,'karan','M',37,'6541378915',34,1423,'MBBS,MS','Orthologist'),(23,'akshay','M',20,'312654',0,100,'MBBS','GENERAL'),(24,'akshay','M',12,'21365497',12,1234,'MBBS MS','GENERAL'),(25,'akshay','123',12,'M',22,123,'MBBS','GENERAL');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
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
