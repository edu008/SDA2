DROP TABLE IF EXISTS `customer_action_logs`;
CREATE TABLE customer_action_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    action_type VARCHAR(50),
    customer_id INT,
    details TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
