-- Adminer 4.8.1 MySQL 11.5.2-MariaDB-ubu2404 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `employee_info`;
CREATE TABLE `employee_info` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `pin_number` int(11) DEFAULT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `user_id` double DEFAULT NULL,
  `phone_number` double NOT NULL,
  `SSN` double DEFAULT NULL,
  `street_address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(2) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `start_date` date DEFAULT NULL,
  `company_name` varchar(50) NOT NULL,
  `number_of_stores` varchar(11) DEFAULT NULL,
  `user_type` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `customer_id` (`customer_id`),
  CONSTRAINT `employee_info_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer`.`customer_info` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

INSERT INTO `employee_info` (`employee_id`, `email`, `password`, `pin_number`, `first_name`, `last_name`, `user_id`, `phone_number`, `SSN`, `street_address`, `city`, `state`, `zip_code`, `start_date`, `company_name`, `number_of_stores`, `user_type`, `customer_id`) VALUES
(1,	'johnnyfran20002@gmail.com',	'passwood',	231,	'Johnny',	'Tejada',	214564056,	6463214487,	756434736,	'10005 Hawk Drive',	'Queens',	'NY',	11105,	'2020-11-02',	'Walmart',	'3',	1,	1),
(2,	'tylerherro23@gmail.com',	'herro',	112,	'Tyler',	'Herro',	435678987,	3475436897,	123456789,	'12th Street',	'New York',	'NY',	9873,	'2019-07-01',	'Shop Rite',	NULL,	2,	2),
(3,	'bronny45@hotmail.com',	'lebron',	113,	'Bronny',	'James',	112323454,	2124568745,	78234325,	'21 Wood Street',	'Woodhaven',	'VT',	12321,	'2019-03-02',	'Walmart',	NULL,	2,	3),
(4,	'usher54@aim.com',	'usher',	555,	'Usher',	'Man',	345432345,	8454342212,	958674345,	'76 Cross Street',	'Houston',	'NY',	85743,	'2020-12-05',	'Walmart',	NULL,	2,	NULL),
(5,	'chrisbrown@gmail.com',	'pass',	111,	'Chris',	'Brown',	111111111,	7187654783,	746378273,	'19 West Street',	'Denver',	'CL',	43454,	'2019-07-03',	'Walmart',	NULL,	2,	NULL),
(6,	'kyrieirving2@hotmail.com',	'kyrie',	705,	'Kyrie',	'Irving',	123456789,	2129857843,	123456789,	'71 2nd Ave',	'New York',	'NY',	12343,	'2017-07-03',	'Tops',	'4',	1,	4);

DROP TABLE IF EXISTS `registers_table`;
CREATE TABLE `registers_table` (
  `register_id` int(11) NOT NULL AUTO_INCREMENT,
  `open_total` float NOT NULL,
  `close_total` float DEFAULT NULL,
  `register_num` int(11) NOT NULL,
  `open_emp_id` int(11) NOT NULL,
  `close_emp_id` int(11) DEFAULT NULL,
  `open_time` datetime NOT NULL,
  `close_time` datetime DEFAULT NULL,
  `drop_time` datetime DEFAULT NULL,
  `drop_emp_id` int(11) DEFAULT NULL,
  `drop_total` float DEFAULT NULL,
  `note` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`register_id`),
  KEY `fk_open_emp_id` (`open_emp_id`),
  KEY `fk_close_emp_id` (`close_emp_id`),
  KEY `fk_drop_emp_id` (`drop_emp_id`),
  CONSTRAINT `fk_close_emp_id` FOREIGN KEY (`close_emp_id`) REFERENCES `employee_info` (`employee_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_drop_emp_id` FOREIGN KEY (`drop_emp_id`) REFERENCES `employee_info` (`employee_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_open_emp_id` FOREIGN KEY (`open_emp_id`) REFERENCES `employee_info` (`employee_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


DROP TABLE IF EXISTS `stores`;
CREATE TABLE `stores` (
  `SID` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`SID`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `stores_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`employee_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


-- 2024-11-11 15:39:20