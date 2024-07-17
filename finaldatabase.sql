-- create database gestion_de_centre;
--
-- Table structure for table `appartenir`
--
-- drop database gestion_de_centre;
 DROP TABLE IF EXISTS `service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service` (
  `id_service` int NOT NULL AUTO_INCREMENT,
  `libele_service` varchar(50) NOT NULL,
  `min_seances` int DEFAULT NULL,
  PRIMARY KEY (`id_service`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 DROP TABLE IF EXISTS `professeur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professeur` (
  `id_professeur` int NOT NULL AUTO_INCREMENT,
  `Nom_Prof` varchar(50) NOT NULL,
  `Prenom_Prof` varchar(50) NOT NULL,
  `tel_prof` varchar(20) DEFAULT NULL,
  `email_Prof` varchar(50) NOT NULL,
  `titre` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_professeur`),
  UNIQUE KEY `email_Prof` (`email_Prof`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

 
 DROP TABLE IF EXISTS `groupe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groupe` (
  `id_groupe` int NOT NULL AUTO_INCREMENT,
  `nbr_Clients` int DEFAULT NULL,
  `min_Clients` int DEFAULT '4',
  `max_Clients` int DEFAULT '8',
  `id_cours` int NOT NULL,
  PRIMARY KEY (`id_groupe`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS `semaine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `semaine` (
  `num_semaine` int NOT NULL,
  PRIMARY KEY (`num_semaine`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

 
DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `id_client` int NOT NULL,
  `Nom` varchar(50) NOT NULL,
  `Prenom` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Telephone` varchar(20) DEFAULT NULL,
  `sexe` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_client`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */; 
 

-- Table structure for table `appartenir`
DROP TABLE IF EXISTS `appartenir`;
CREATE TABLE `appartenir` (
  `id_client` int NOT NULL,
  `id_groupe` int NOT NULL,
  PRIMARY KEY (`id_client`, `id_groupe`),
  KEY `id_groupe` (`id_groupe`),
  CONSTRAINT `appartenir_ibfk_1` FOREIGN KEY (`id_client`) REFERENCES `client` (`id_client`) ON DELETE CASCADE,
  CONSTRAINT `appartenir_ibfk_2` FOREIGN KEY (`id_groupe`) REFERENCES `groupe` (`id_groupe`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `client`
--



--
-- Table structure for table `cours`
--

DROP TABLE IF EXISTS `cours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cours` (
  `id_cours` int NOT NULL AUTO_INCREMENT,
  `libele` varchar(50) NOT NULL,
  `niv_scol` varchar(20) DEFAULT NULL,
  `Prix` decimal(10,2) NOT NULL DEFAULT '150.00',
  `id_service` int DEFAULT NULL,
  PRIMARY KEY (`id_cours`),
  KEY `id_service` (`id_service`),
  CONSTRAINT `cours_ibfk_1` FOREIGN KEY (`id_service`) REFERENCES `service` (`id_service`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `feuille_absence`
--



--
-- Table structure for table `groupe`
--


--
-- Table structure for table `inscription`
--

DROP TABLE IF EXISTS `inscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inscription` (
  `nombre_seances` int NOT NULL,
  `Absences_Tolérées` int DEFAULT '1',
  `de_test` tinyint(1) DEFAULT NULL,
  `Prix_test` decimal(10,2) DEFAULT '200.00',
  `id_client` int NOT NULL,
  `id_cours` int NOT NULL,
  `Date_inscription` date NOT NULL,
  PRIMARY KEY (`id_client`,`id_cours`),
  KEY `id_cours` (`id_cours`),
  CONSTRAINT `inscription_ibfk_1` FOREIGN KEY (`id_client`) REFERENCES `client` (`id_client`) ON DELETE CASCADE,
  CONSTRAINT `inscription_ibfk_2` FOREIGN KEY (`id_cours`) REFERENCES `cours` (`id_cours`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `professeur`
--



--
-- Table structure for table `salle`
--

DROP TABLE IF EXISTS `salle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salle` (
  `id_salle` int NOT NULL AUTO_INCREMENT,
  `nom_salle` varchar(50) NOT NULL,
  `type_salle` char(1) NOT NULL DEFAULT 'P',
  PRIMARY KEY (`id_salle`)
) ENGINE=InnoDB AUTO_INCREMENT=568 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `seance`
--

DROP TABLE IF EXISTS `seance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seance` (
  `id_seance` int NOT NULL AUTO_INCREMENT,
  `id_groupe` int DEFAULT NULL,
  `id_salle` int DEFAULT NULL,
  `id_cours` int DEFAULT NULL,
  `id_professeur` int DEFAULT NULL,
  `jour_seance` varchar(20) NOT NULL,
  `heure_seance` varchar(20) NOT NULL,
  PRIMARY KEY (`id_seance`),
  KEY `id_groupe` (`id_groupe`),
  KEY `id_professeur` (`id_professeur`),
  KEY `id_salle` (`id_salle`),
  KEY `id_cours` (`id_cours`),
  CONSTRAINT `seance_ibfk_1` FOREIGN KEY (`id_groupe`) REFERENCES `groupe` (`id_groupe`) ON DELETE CASCADE,
  CONSTRAINT `seance_ibfk_2` FOREIGN KEY (`id_professeur`) REFERENCES `professeur` (`id_professeur`) ON DELETE CASCADE,
  CONSTRAINT `seance_ibfk_3` FOREIGN KEY (`id_salle`) REFERENCES `salle` (`id_salle`) ON DELETE CASCADE,
  CONSTRAINT `seance_ibfk_4` FOREIGN KEY (`id_cours`) REFERENCES `cours` (`id_cours`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
DROP TABLE IF EXISTS `feuille_absence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feuille_absence` (
  `id_client` int NOT NULL,
  `id_seance` int NOT NULL,
  `num_semaine` int NOT NULL,
  `date_feuille` date NOT NULL,
  `est_present` int DEFAULT NULL,
  PRIMARY KEY (`id_client`,`id_seance`,`num_semaine`),
  KEY `id_seance` (`id_seance`),
  KEY `num_semaine` (`num_semaine`),
  CONSTRAINT `feuille_absence_ibfk_1` FOREIGN KEY (`id_client`) REFERENCES `client` (`id_client`) ON DELETE CASCADE,
  CONSTRAINT `feuille_absence_ibfk_2` FOREIGN KEY (`id_seance`) REFERENCES `seance` (`id_seance`) ON DELETE CASCADE,
  CONSTRAINT `feuille_absence_ibfk_3` FOREIGN KEY (`num_semaine`) REFERENCES `semaine` (`num_semaine`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
-- Table structure for table `semaine`
--


--
-- Table structure for table `service`
--


