-- Adminer 4.8.1 MySQL 11.5.2-MariaDB-ubu2404 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `ticket_system`;
CREATE TABLE `ticket_system` (
  `ticket_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `time` time NOT NULL,
  `quantity` int(11) NOT NULL,
  `subtotal` float NOT NULL,
  `total` float NOT NULL,
  `cost` float NOT NULL,
  `discount` float DEFAULT NULL,
  `tax` float NOT NULL,
  `tax_rate` float NOT NULL,
  `cash` float NOT NULL,
  `credit` float NOT NULL,
  `cart_purchase` tinyint(1) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`ticket_id`),
  KEY `customer_id` (`customer_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `ticket_system_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer`.`customer_info` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ticket_system_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employee`.`employee_info` (`employee_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

DROP TABLE IF EXISTS `ticket_history`;
CREATE TABLE `ticket_history` (
  `history_id` int(11) NOT NULL AUTO_INCREMENT,
  `ticket_id` int(11) NOT NULL,
  `change_date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `priority` varchar(20) NOT NULL,
  `remarks` text DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `ticket_id` (`ticket_id`),
  CONSTRAINT `ticket_history_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket_system` (`ticket_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

DROP TABLE IF EXISTS `ticket_type`;
CREATE TABLE `ticket_type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(50) NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
-- 2024-11-11 15:41:20