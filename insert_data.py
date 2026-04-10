from db import get_connection

def insert_data():
    conn = get_connection()
    cur = conn.cursor()

    # Block
    cur.execute("INSERT INTO Block VALUES (1, 'Saundatti') ON CONFLICT DO NOTHING")

    # Panchayat
    cur.execute("""
    INSERT INTO Panchayat VALUES
    (1, 'Aratgal', 1),
    (2, 'Betasur', 1),
    (3, 'Bhandarahalli', 1)
    ON CONFLICT DO NOTHING
    """)

    # Village
    cur.execute("""
    INSERT INTO Village VALUES
    (1, 'Aratgal', 1),
    (2, 'Basaragi Inam', 1),
    (3, 'Kitadal', 1)
    ON CONFLICT DO NOTHING
    """)

    # Department
    cur.execute("""
    INSERT INTO Department (department_name) VALUES
    ('PWD'),
    ('Rural Development'),
    ('Panchayat Raj'),
    ('Water Supply')
    ON CONFLICT DO NOTHING
    """)

    # Development
    cur.execute("""
    INSERT INTO Development 
    (work_name, department_id, estimated_cost, village_id, work_date)
    VALUES
    ('Road Construction', 1, 1500000, 1, '2024-01-10'),
    ('Water Tank Installation', 4, 800000, 3, '2024-02-05')
    ON CONFLICT DO NOTHING
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Data inserted successfully")

if __name__ == "__main__":
    insert_data()