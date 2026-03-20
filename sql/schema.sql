CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    transaction_type VARCHAR(100),
    count BIGINT,
    amount DOUBLE
);