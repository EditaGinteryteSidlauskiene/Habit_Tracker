-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: habit_tracker
-- ------------------------------------------------------
-- Server version	9.3.0

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
-- Table structure for table `habit_completions`
--

DROP TABLE IF EXISTS `habit_completions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `habit_completions` (
  `id` varchar(36) NOT NULL,
  `completed_on` datetime NOT NULL,
  `habit_id` varchar(36) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `habit_id` (`habit_id`),
  CONSTRAINT `habit_id` FOREIGN KEY (`habit_id`) REFERENCES `habits` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habit_completions`
--

LOCK TABLES `habit_completions` WRITE;
/*!40000 ALTER TABLE `habit_completions` DISABLE KEYS */;
INSERT INTO `habit_completions` VALUES ('0e6f0c1d-b3b2-4f49-b5f5-65e3ef61b4d3','2025-03-20 11:30:44','d06bebf9-ee21-40be-82cd-f3d7ed0eb48d'),('1b832204-539d-48b0-8aa2-8b03ce3d324f','2025-07-03 07:00:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('2ac988c2-feb3-4a0a-880f-22fdff41d4e9','2025-07-06 08:00:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('2cf65bc6-7990-4f71-8dfc-885e39db1e6b','2025-07-14 18:10:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('2d90eb77-29cb-4a00-9ae5-b46ae0c129f9','2025-06-29 18:30:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('30db50f1-b2aa-4b52-8d1e-62e186cccb86','2025-06-20 19:45:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('36f255db-f3a0-4e2c-86ea-1d82639535d2','2025-06-20 07:45:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('3bbcc683-b195-4d27-9aa6-7bcac3e4cf33','2025-06-02 02:45:12','7d6b0b72-cf6c-43e1-b17d-495cd54a3ece'),('3e5f6b45-8707-447e-8ed4-8d96c967377a','2025-06-27 19:05:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('3f50e916-6b14-490c-8856-ec80d4a3e4df','2025-07-07 07:30:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('52cfa87b-6de3-4e62-9f86-663674b85ec9','2025-07-12 19:45:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('5dfc3b39-8828-412c-b34a-7a7d63fa739e','2025-07-06 19:20:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('6173e139-85e5-4cf1-9a35-ecf6a92d93a2','2025-06-24 08:30:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('6dfd9c1e-1b94-42a2-9c42-bf3b7f5cf90d','2025-06-09 18:45:45','7d6b0b72-cf6c-43e1-b17d-495cd54a3ece'),('6e15b450-e34a-4378-94c7-d8b6d59e2e6b','2025-07-16 19:32:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('71383f85-08cd-41b3-bb77-0b137e623f7a','2025-06-17 18:10:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('74f22f41-04a7-4b87-bdbf-4cfc5df7dbe2','2025-06-28 09:15:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('8e68a801-d6a1-49ad-8774-41eb4faeec9c','2025-06-14 13:47:55','d06bebf9-ee21-40be-82cd-f3d7ed0eb48d'),('94a6c1b7-e6a2-4c5e-b52e-2f72920e4121','2025-07-08 18:00:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('a686382c-b8a4-43d2-b10d-5fa67e2dfaa0','2025-07-14 10:17:01','ffda7c39-8c94-478f-9e74-39a86c4d6fdb'),('a7e85e4e-71e3-4e01-a53d-11f764bba92d','2025-07-04 07:15:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('ab3a4522-cdcb-49b5-ae4e-135b6a894f55','2025-07-13 20:05:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('ad8ec85b-f1b2-4f7c-b167-bf84a99fdc12','2025-06-22 15:48:46','7d6b0b72-cf6c-43e1-b17d-495cd54a3ece'),('b748d38e-2a3d-4f8f-8a6f-3e877b582bf5','2025-07-06 14:15:22','7d6b0b72-cf6c-43e1-b17d-495cd54a3ece'),('b7b15244-f3e7-41c7-a25e-fc9d98a470de','2025-07-15 20:50:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('b8a1db72-9f70-4b2c-b63d-44f4d10d8074','2025-07-09 17:30:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('c5fd1f5d-c9d7-4070-a95f-df5f5cf72d68','2025-06-23 20:15:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('c8e6f8b1-91c2-43e2-8cb3-2d4e15a3c1c9','2025-07-10 01:00:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('d59a9616-1b10-48eb-9d7e-3cf4b6c44f2b','2025-07-14 13:33:14','7d6b0b72-cf6c-43e1-b17d-495cd54a3ece'),('dc32f844-3658-49cf-a5ec-33d65e1dc498','2025-07-09 21:00:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('de39d47a-3fe6-4b3c-84fc-798b45ddcf25','2025-07-10 17:00:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('e24acdab-9d61-4656-bab6-4726db1d607c','2025-05-20 13:47:11','d06bebf9-ee21-40be-82cd-f3d7ed0eb48d'),('e7a1d14f-2f14-4de5-a58a-1dc2c43813e5','2025-07-11 05:30:00','5e8de8d5-3136-44e3-8158-972a127bb839'),('e7a38f53-8b2e-4d7a-8e09-4f9c47d4ad40','2025-07-01 15:44:11','7d6b0b72-cf6c-43e1-b17d-495cd54a3ece'),('ef14a2aa-15a5-4d8d-b0d3-c77c0c62aa66','2025-04-30 13:48:22','d06bebf9-ee21-40be-82cd-f3d7ed0eb48d'),('f0c3b74d-3d61-44c3-8b08-8db9ed1b88d7','2025-07-13 12:15:12','5e8de8d5-3136-44e3-8158-972a127bb839'),('f9a7ff77-bacc-4b76-89f4-1f2790b6d020','2025-07-02 20:40:00','e164b60a-511d-4fad-9841-5136726a1a4e'),('fbcb7c86-8f3c-499c-91b1-9c2eb7c76e5d','2025-07-14 13:13:13','5e8de8d5-3136-44e3-8158-972a127bb839');
/*!40000 ALTER TABLE `habit_completions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `habits`
--

DROP TABLE IF EXISTS `habits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `habits` (
  `id` varchar(36) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(500) NOT NULL,
  `periodicity` varchar(50) NOT NULL,
  `creation_date` datetime NOT NULL,
  `user_id` varchar(36) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habits`
--

LOCK TABLES `habits` WRITE;
/*!40000 ALTER TABLE `habits` DISABLE KEYS */;
INSERT INTO `habits` VALUES ('5e8de8d5-3136-44e3-8158-972a127bb839','Jogging','Jog for 30 min','DAILY','2025-06-20 07:00:00','3bbe0fe5-5964-4c0f-aee3-fe85057c9877'),('7d6b0b72-cf6c-43e1-b17d-495cd54a3ece','Laundry','Do laundry','WEEKLY','2025-06-01 12:00:00','b6b47614-afcb-454e-9a3a-a9f815e91568'),('878b72db-ec14-4409-849c-88bc45f1ee82','Brush teeth','twice a day','DAILY','2025-07-10 00:00:00','b6b47614-afcb-454e-9a3a-a9f815e91568'),('be06e0a1-d1e6-47b6-b357-ef50e8bc7d80','Grass','Mowe grass','WEEKLY','2025-07-10 00:00:00','d0697617-54c3-4237-9ad2-ddc93ef02079'),('d06bebf9-ee21-40be-82cd-f3d7ed0eb48d','Trash container','Take out trash container','MONTHLY','2025-07-10 00:00:00','d0697617-54c3-4237-9ad2-ddc93ef02079'),('e164b60a-511d-4fad-9841-5136726a1a4e','Drink water','8 glasses a day','DAILY','2025-06-17 12:00:00','3bbe0fe5-5964-4c0f-aee3-fe85057c9877'),('ef14a2aa-15a5-4d8d-b0d3-c77c0c62aa67','Bills','Pay bills','MONTHLY','2025-07-10 00:00:00','9b5d301d-ec61-402e-9543-d68f86b9c41d'),('ffda7c39-8c94-478f-9e74-39a86c4d6fdb','Change sheets','Change sheets','WEEKLY','2025-07-10 00:00:00','9b5d301d-ec61-402e-9543-d68f86b9c41d');
/*!40000 ALTER TABLE `habits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(36) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('3bbe0fe5-5964-4c0f-aee3-fe85057c9877','William','william@gmail.com','william'),('3f55da35-fe6e-4fee-a7ed-20601f764ad5','Oliver','oliver@gmail.com','oliver'),('9b5d301d-ec61-402e-9543-d68f86b9c41d','Martha','martha@gmail.com','martha'),('b6b47614-afcb-454e-9a3a-a9f815e91568','Joana','joana@gmail.com','joana'),('d0697617-54c3-4237-9ad2-ddc93ef02079','Mark','mark@gmail.com','mark');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-16 15:22:38
