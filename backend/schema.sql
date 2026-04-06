CREATE TABLE IF NOT EXISTS Billing (
    billing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    total_amount REAL,
    billing_date TEXT
);

INSERT INTO Billing (order_id, total_amount, billing_date)
VALUES (1, 1000, '2024-06-01');

INSERT INTO Billing (order_id, total_amount, billing_date)
VALUES (2, 2000, '2024-06-02');

SELECT * FROM Billing;
