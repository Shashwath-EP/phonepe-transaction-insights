import sqlite3
from transform import get_transaction_df, get_user_df, get_top_df

# ---------------- DB CONNECTION ---------------- #
# Create/connect to SQLite database file
conn = sqlite3.connect("phonepe.db")
cursor = conn.cursor()

# ---------------- CREATE TABLES ---------------- #
# Create tables if they don't exist

cursor.execute("""
CREATE TABLE IF NOT EXISTS aggregated_transaction (
    state TEXT,
    year INTEGER,
    quarter INTEGER,
    transaction_type TEXT,
    count INTEGER,
    amount REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS aggregated_user (
    state TEXT,
    year INTEGER,
    quarter INTEGER,
    brand TEXT,
    count INTEGER,
    percentage REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS top_transaction (
    state TEXT,
    year INTEGER,
    quarter INTEGER,
    district TEXT,
    count INTEGER,
    amount REAL
)
""")

# ---------------- CLEAR OLD DATA ---------------- #
# Remove old records before inserting fresh data
cursor.execute("DELETE FROM aggregated_transaction")
cursor.execute("DELETE FROM aggregated_user")
cursor.execute("DELETE FROM top_transaction")

# ---------------- LOAD TRANSACTION DATA ---------------- #
txn_df = get_transaction_df()

for _, row in txn_df.iterrows():
    cursor.execute("""
        INSERT INTO aggregated_transaction
        (state, year, quarter, transaction_type, count, amount)
        VALUES (?, ?, ?, ?, ?, ?)
    """, tuple(row))

# ---------------- LOAD USER DATA ---------------- #
user_df = get_user_df()

for _, row in user_df.iterrows():
    cursor.execute("""
        INSERT INTO aggregated_user
        (state, year, quarter, brand, count, percentage)
        VALUES (?, ?, ?, ?, ?, ?)
    """, tuple(row))

# ---------------- LOAD TOP DISTRICT DATA ---------------- #
top_df = get_top_df()

for _, row in top_df.iterrows():
    cursor.execute("""
        INSERT INTO top_transaction
        (state, year, quarter, district, count, amount)
        VALUES (?, ?, ?, ?, ?, ?)
    """, tuple(row))

# ---------------- SAVE & CLOSE ---------------- #
conn.commit()
cursor.close()
conn.close()

print("Data loaded successfully into SQLite!")