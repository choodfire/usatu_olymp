CREATE TABLE IF NOT EXISTS payments (
    pension_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    type VARCHAR(255) NOT NULL,
    amount FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);