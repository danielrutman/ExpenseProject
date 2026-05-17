"""Lambda handler — direct AWS Lambda handler for expenses bot"""
import json
import logging
import base64
from expenses_bot import app

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    """handles incoming API Gateway requests and routes to Flask app"""

    # extract request body from API Gateway event
    body = event.get("body") or ""
    # decode base64 body if API Gateway encoded it
    if event.get("isBase64Encoded"):
        body = base64.b64decode(body).decode("utf-8")
    logger.info("Incoming body: %s", body)

    # create Flask test request context
    with app.test_request_context(
        path="/bot",
        method="POST",
        content_type="application/x-www-form-urlencoded",
        data=body
    ):
        # run the Flask app and get response
        from expenses_bot import main_router
        response = main_router()

    logger.info("Response body: %s", response)
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/xml"},
        "body": str(response),
        "isBase64Encoded": False
    }