from db import get_connection
from response import success, error
import json

def lambda_handler(event, context):
    try:
        http_method = event.get("httpMethod")

        conn = get_connection()
        cursor = conn.cursor()

        # ========================
        # ✅ GET API (Fetch data)
        # ========================
        if http_method == "GET":
            query = "SELECT * FROM development"
            cursor.execute(query)
            rows = cursor.fetchall()

            result = []
            for row in rows:
                result.append({
                    "id": row[0],
                    "work_name": row[1],
                    "department_id": row[2],
                    "estimated_cost": row[3],
                    "village_id": row[4],
                    "work_date": str(row[5])
                })

            cursor.close()
            conn.close()
            return success(result)

        # ========================
        # ✅ POST API (Insert data)
        # ========================
        elif http_method == "POST":
            body = json.loads(event.get("body", "{}"))

            work_name = body.get("work_name")
            department_id = body.get("department_id")
            estimated_cost = body.get("estimated_cost")
            village_id = body.get("village_id")
            work_date = body.get("work_date")

            query = """
                INSERT INTO development 
                (work_name, department_id, estimated_cost, village_id, work_date)
                VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(query, (
                work_name,
                department_id,
                estimated_cost,
                village_id,
                work_date
            ))

            conn.commit()

            cursor.close()
            conn.close()

            return success({"message": "Data inserted successfully"})

        else:
            return error("Method not allowed", 405)

    except Exception as e:
        print("ERROR:", str(e))
        return error(str(e), 500)