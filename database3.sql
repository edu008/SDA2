-- Setting initial configurations
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
SET NAMES utf8mb4;
START TRANSACTION;

-- Dropping tables if they exist
DROP TABLE IF EXISTS `cart`, `cart_inprogress`, `customer_info`, `gift_card`, `employee_info`, `registers_table`, `stores`, `item_list`, `orders`, `orders_ticket`, `return_table`, `product_inventory`, `vendorinfo`, `tax_table`, `ticket_system`, `ticket_history`, `ticket_type`;

-- Creating tables and inserting data

-- Table: customer_info
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `customer_info` (`customer_id`, `email`, `password`, `first_name`, `last_name`, `phone_number`, `rewards`, `street_address`, `city`, `state`, `zip_code`) VALUES
(1, 'johnnyfran20002@gmail.com', 'passwood', 'Johnny', 'Tejada', 6463214487, 33, '10005 Hawk Drive', 'Queens', 'NY', 12321),
(2, 'tylerherro23@gmail.com', 'password', 'Tyler', 'Herro', 3475436578, 90, '12th Street', 'New York', 'NY', 9874),
(3, 'bronny45@hotmail.com', 'lebron', 'Bronny', 'James', 2124567656, 44, '21 Wood Street', 'Woodhaven', 'VT', 7384),
(4, 'kyrieirving2@hotmail.com', 'kyrie', 'Kyrie', 'Irving', 2123434567, 14, '74 2nd Ave', 'New York', 'NY', 12343),
(6, 'michaelj23@gmail.com', 'jordan', 'Michael', 'Jordan', 2125468796, 44, '14th Street', 'Chicago', 'IL', 76854),
(7, 'cp3@yahoo.com', 'phzsuns', 'Chris', 'Paul', 8452341004, 0, '346 Broad St', 'Los Angeles', 'CA', 90212),
(9, 'bgates19@hotmail.com', 'apple', 'Bill', 'Gates', 3479845093, 0, '109 19th Street', 'Sacramento', 'CA', 29343);

-- Table: gift_card
CREATE TABLE `gift_card` (
  `gift_id` int(11) NOT NULL AUTO_INCREMENT,
  `promo_number` double NOT NULL,
  `card_balance` float NOT NULL,
  `ticket_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`gift_id`),
  KEY `ticket_id` (`ticket_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `gift_card_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket_system` (`ticket_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `gift_card_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer_info` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `gift_card` (`gift_id`, `promo_number`, `card_balance`, `ticket_id`, `customer_id`) VALUES
(3, 26576, 10, NULL, NULL);

-- Table: cart_inprogress
CREATE TABLE `cart_inprogress` (
  `CID` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `ticket_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`CID`),
  KEY `customer_id` (`customer_id`),
  KEY `ticket_id` (`ticket_id`),
  CONSTRAINT `cart_inprogress_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket_system` (`ticket_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cart_inprogress_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer_info` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: cart
CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `CID` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`cart_id`),
  KEY `product_id` (`product_id`),
  KEY `CID` (`CID`),
  CONSTRAINT `cart_ibfk_4` FOREIGN KEY (`product_id`) REFERENCES `product_inventory` (`product_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cart_ibfk_5` FOREIGN KEY (`CID`) REFERENCES `cart_inprogress` (`CID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: orders
CREATE TABLE `orders` (
  `OID` int(11) NOT NULL AUTO_INCREMENT,
  `OTID` int(11) NOT NULL,
  `stock_amount` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`OID`),
  KEY `OTID` (`OTID`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`OTID`) REFERENCES `orders_ticket` (`OTID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`product_id`) REFERENCES `product_inventory` (`product_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: orders_ticket
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
  CONSTRAINT `orders_ticket_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`employee_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `orders_ticket_ibfk_2` FOREIGN KEY (`vendor_id`) REFERENCES `vendorinfo` (`vendor_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: return_table
CREATE TABLE `return_table` (
  `RTID` int(11) NOT NULL AUTO_INCREMENT,
  `ticket_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `refunds` float NOT NULL,
  `exchanges` float DEFAULT NULL,
  PRIMARY KEY (`RTID`),
  KEY `ticket_id` (`ticket_id`),
  CONSTRAINT `return_table_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket_system` (`ticket_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: product_inventory
CREATE TABLE `product_inventory` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `brand` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `productName` varchar(50) NOT NULL,
  `productType` varchar(50) NOT NULL,
  `productSubType` varchar(50) NOT NULL,
  `unit_price` float NOT NULL,
  `cost` float NOT NULL,
  `in_stock` int(11) NOT NULL,
  `vendor_id` int(11) NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `vendor_id` (`vendor_id`),
  CONSTRAINT `product_inventory_ibfk_2` FOREIGN KEY (`vendor_id`) REFERENCES `vendorinfo` (`vendor_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: vendorinfo
CREATE TABLE `vendorinfo` (
  `vendor_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `department` varchar(100) NOT NULL,
  `street_address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(2) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `phone_number` double NOT NULL,
  `fax_number` double NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: employee_info
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
  CONSTRAINT `employee_info_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer_info` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: stores
CREATE TABLE `stores` (
  `SID` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`SID`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `stores_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`employee_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: registers_table
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: tax_table
CREATE TABLE `tax_table` (
  `TTID` int(11) NOT NULL AUTO_INCREMENT,
  `tax_year` year(4) NOT NULL,
  `state_tax` float NOT NULL,
  `county_tax` float NOT NULL,
  `city_rate` float NOT NULL,
  `tax_rate` float NOT NULL,
  PRIMARY KEY (`TTID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `tax_table` (`TTID`, `tax_year`, `state_tax`, `county_tax`, `city_rate`, `tax_rate`) VALUES
(1, 2020, 0.04, 0.04, 0.08, 0.08);

-- Table: ticket_system
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
  CONSTRAINT `ticket_system_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer_info` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ticket_system_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`employee_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: ticket_history
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: ticket_type
CREATE TABLE `ticket_type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(50) NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
