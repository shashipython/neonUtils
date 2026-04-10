import json
from decimal import Decimal

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def success(data):
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(data, default=decimal_default)
    }

def error(message, code=400):
    return {
        "statusCode": code,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({"error": message})
    }