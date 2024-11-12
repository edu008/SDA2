-- Adminer 4.8.1 MySQL 11.5.2-MariaDB-ubu2404 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `item_list`;
CREATE TABLE `item_list` (
  `ITID` int(11) NOT NULL AUTO_INCREMENT,
  `CID` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`ITID`),
  KEY `CID` (`CID`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `item_list_ibfk_1` FOREIGN KEY (`CID`) REFERENCES `customer`.`cart_inprogress` (`CID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `item_list_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product`.`product_inventory` (`product_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `OID` int(11) NOT NULL AUTO_INCREMENT,
  `OTID` int(11) NOT NULL,
  `stock_amount` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`OID`),
  KEY `OTID` (`OTID`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`OTID`) REFERENCES `orders_ticket` (`OTID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`product_id`) REFERENCES `product`.`product_inventory` (`product_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


DROP TABLE IF EXISTS `orders_ticket`;
CREATE TABLE `orders_ticket` (
  `OTID` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `subtotal` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `tax` float DEFAULT NULL,
  `tax_rate` float DEFAULT NULL,
  `cash` float DEFAULT NULL,
  `credit` float DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `vendor_id` int(11) NOT NULL,
  PRIMARY KEY (`OTID`),
  KEY `employee_id` (`employee_id`),
  KEY `vendor_id` (`vendor_id`),
  CONSTRAINT `orders_ticket_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee`.`employee_info` (`employee_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `orders_ticket_ibfk_2` FOREIGN KEY (`vendor_id`) REFERENCES `product`.`vendorinfo` (`vendor_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


DROP TABLE IF EXISTS `return_table`;
CREATE TABLE `return_table` (
  `RTID` int(11) NOT NULL AUTO_INCREMENT,
  `ticket_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `refunds` float NOT NULL,
  `exchanges` float DEFAULT NULL,
  PRIMARY KEY (`RTID`),
  KEY `ticket_id` (`ticket_id`),
  CONSTRAINT `return_table_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket`.`ticket_system` (`ticket_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


-- 2024-11-11 15:39:59