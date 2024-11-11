CREATE TABLE post (
    p_id INT PRIMARY KEY AUTO_INCREMENT,
    p_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    p_image VARCHAR(127),
    p_resume VARCHAR(255)
    p_status ENUM('on', 'off') DEFAULT 'on',
    p_expiration_date DATE
)