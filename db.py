import pg8000
import os
from dotenv import load_dotenv

load_dotenv()  # 🔥 loads .env file

def get_connection():
    return pg8000.connect(
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        port=int(os.environ.get('DB_PORT', 5432)),
        database=os.environ['DB_NAME'],
        ssl_context=True,
        timeout=10
    )