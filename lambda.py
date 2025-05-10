import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,

        # Qute comment ;^)
        "body": json.dumps("Hayyy there! 👻") # ; )
    }
