CREATE DATABASE IF NOT EXISTS `test`;
USE `test`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(32) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES (0,'admin@example.com','admin','Admin'),(1,'user1@example.com','user1','User1'),(2,'user2@example.com','user2','User2'),(3,'user3@example.com','user3','User3'),(4,'user4@example.com','user4','User4'),(5,'user5@example.com','user5','User5'),(6,'user6@example.com','user6','User6'),(7,'user7@example.com','user7','User7'),(8,'user8@example.com','user8','User8'),(9,'user9@example.com','user9','User9'),(10,'user10@example.com','user10','User10'),(11,'user11@example.com','user11','User11');
UNLOCK TABLES;

-- gameinfo --

CREATE DATABASE IF NOT EXISTS `test`;
USE `test`;

DROP TABLE IF EXISTS `gameinfo`;
CREATE TABLE `gameinfo` (
  `id` int(32) unsigned NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `team` varchar(5) NOT NULL,
  `i1` int(5) NOT NULL,
  `i2` int(5) NOT NULL,
  `i3` int(5) NOT NULL,
  `i4` int(5) NOT NULL,
  `i5` int(5) NOT NULL,
  `i6` int(5) NOT NULL,
  `i7` int(5) NOT NULL,
  `i8` int(5) NOT NULL,
  `i9` int(5) NOT NULL,
  `i10` int(5) NOT NULL,
  `i11` int(5) NOT NULL,
  `i12` int(5) NOT NULL,
  `R` int(7) NOT NULL,
  `H` int(7) NOT NULL,
  `E` int(7) NOT NULL,
  `B` int(7) NOT NULL,
  `recordW` int(7) NOT NULL,
  `recordL` int(7) NOT NULL,
  `recordD` int(7) NOT NULL,
  `finalhit` varchar(30) NOT NULL,
  `homerun` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

