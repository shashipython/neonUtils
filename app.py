from fastapi import FastAPI
from db import get_connection

app = FastAPI()

@app.get("/development")
def get_data(village_id: int = None, panchayat_id: int = None):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    SELECT d.development_id, d.work_name, d.estimated_cost,
           d.work_date, dep.department_name,
           v.village_name, p.panchayat_name
    FROM Development d
    JOIN Village v ON d.village_id = v.village_id
    JOIN Panchayat p ON v.panchayat_id = p.panchayat_id
    JOIN Department dep ON d.department_id = dep.department_id
    WHERE 1=1
    """

    values = []

    if village_id:
        query += " AND d.village_id = %s"
        values.append(village_id)

    if panchayat_id:
        query += " AND p.panchayat_id = %s"
        values.append(panchayat_id)

    cur.execute(query, values)

    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]

    return [dict(zip(columns, row)) for row in rows]