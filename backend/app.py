from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Billing (
        billing_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        total_amount REAL,
        billing_date TEXT
    )
    ''')

    cursor.execute("DELETE FROM Billing")

    cursor.execute('''
    INSERT INTO Billing (order_id, total_amount, billing_date)
    VALUES (1, 1000, '2024-06-01')
    ''')

    cursor.execute('''
    INSERT INTO Billing (order_id, total_amount, billing_date)
    VALUES (2, 2000, '2024-06-02')
    ''')

    conn.commit()
    conn.close()

@app.route('/api/billing')
def get_billing():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    data = conn.execute('SELECT * FROM Billing').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])
@app.route('/api/recommendations')
def get_recommendations():
    return jsonify([
        {"product_id": 1, "product_name": "Product A"},
        {"product_id": 2, "product_name": "Product B"}
    ])

@app.route('/api/fraud-detection')
def get_fraud_detection():
    return jsonify({
        "order_id": 1,
        "fraud_score": 0.2
    })

@app.route('/')
def home():
    return "Server is running!"

if __name__ == '__main__':
    init_db()
    app.run(debug=False)   