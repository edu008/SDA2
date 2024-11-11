-- Adminer 4.8.1 MySQL 11.5.2-MariaDB-ubu2404 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `cart`;
CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `CID` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`cart_id`),
  KEY `product_id` (`product_id`),
  KEY `CID` (`CID`),
  CONSTRAINT `cart_ibfk_4` FOREIGN KEY (`product_id`) REFERENCES `product`.`product_inventory` (`product_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cart_ibfk_5` FOREIGN KEY (`CID`) REFERENCES `cart_inprogress` (`CID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


DROP TABLE IF EXISTS `cart_inprogress`;
CREATE TABLE `cart_inprogress` (
  `CID` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `ticket_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`CID`),
  KEY `customer_id` (`customer_id`),
  KEY `ticket_id` (`ticket_id`),
  CONSTRAINT `cart_inprogress_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket`.`ticket_system` (`ticket_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cart_inprogress_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer_info` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


DROP TABLE IF EXISTS `customer_info`;
CREATE TABLE `customer_info` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password` varchar(60) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone_number` double NOT NULL,
  `rewards` float DEFAULT NULL,
  `street_address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(2) NOT NULL,
  `zip_code` int(11) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

INSERT INTO `customer_info` (`customer_id`, `email`, `password`, `first_name`, `last_name`, `phone_number`, `rewards`, `street_address`, `city`, `state`, `zip_code`) VALUES
(1,	'johnnyfran20002@gmail.com',	'passwood',	'Johnny',	'Tejada',	6463214487,	33,	'10005 Hawk Drive ',	'Queens',	'NY',	12321),
(2,	'tylerherro23@gmail.com',	'password',	'Tyler',	'Herro',	3475436578,	90,	'12th Street',	'New York',	'NY',	9874),
(3,	'bronny45@hotmail.com',	'lebron',	'Bronny',	'James',	2124567656,	44,	'21 Wood Street',	'Woodhaven',	'VT',	7384),
(4,	'kyrieirving2@hotmail.com',	'kyrie',	'Kyrie',	'Irving',	2123434567,	14,	'74 2nd Ave',	'New York',	'NY',	12343),
(6,	'michaelj23@gmail.com',	'jordan',	'Michael',	'Jordan',	2125468796,	44,	'14th Street',	'Chicago ',	'IL',	76854),
(7,	'cp3@yahoo.com',	'phzsuns',	'Chris',	'Paul',	8452341004,	0,	'346 Broad St',	'Los Angeles',	'CA',	90212),
(9,	'bgates19@hotmail.com',	'apple',	'Bill',	'Gates',	3479845093,	0,	'109 19th Street',	'Sacramento',	'CA',	29343);

DROP TABLE IF EXISTS `gift_card`;
CREATE TABLE `gift_card` (
  `gift_id` int(11) NOT NULL AUTO_INCREMENT,
  `promo_number` double NOT NULL,
  `card_balance` float NOT NULL,
  `ticket_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`gift_id`),
  KEY `ticket_id` (`ticket_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `gift_card_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket`.`ticket_system` (`ticket_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `gift_card_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer_info` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

INSERT INTO `gift_card` (`gift_id`, `promo_number`, `card_balance`, `ticket_id`, `customer_id`) VALUES
(3,	26576,	10,	NULL,	NULL);

-- 2024-11-11 15:39:40