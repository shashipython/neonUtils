import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lambda_function import lambda_handler

event = {
    "queryStringParameters": {
        "village_id": "1"
    }
}

response = lambda_handler(event, None)

print(response)