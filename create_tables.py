from db import get_connection

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Block (
        block_id INT PRIMARY KEY,
        block_name VARCHAR(100)
    );

    CREATE TABLE IF NOT EXISTS Panchayat (
        panchayat_id INT PRIMARY KEY,
        panchayat_name VARCHAR(100),
        block_id INT REFERENCES Block(block_id)
    );

    CREATE TABLE IF NOT EXISTS Village (
        village_id INT PRIMARY KEY,
        village_name VARCHAR(100),
        panchayat_id INT REFERENCES Panchayat(panchayat_id)
    );

    CREATE TABLE IF NOT EXISTS Department (
        department_id SERIAL PRIMARY KEY,
        department_name VARCHAR(150)
    );

    CREATE TABLE IF NOT EXISTS Development (
        development_id SERIAL PRIMARY KEY,
        work_name VARCHAR(255),
        department_id INT REFERENCES Department(department_id),
        estimated_cost DECIMAL,
        village_id INT REFERENCES Village(village_id),
        work_date DATE
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Tables created successfully")

if __name__ == "__main__":
    create_tables()