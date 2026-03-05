# from aws_lambda_powertools import Logger
# from aws_lambda_powertools.event_handler.api_gateway import (
#     APIGatewayRestResolver,
#     CORSConfig,
# )

# logger = Logger()

# cors_config = CORSConfig(
#     allow_origin="*",
#     allow_headers=["Content-Type"],
#     allow_methods=["GET", "OPTIONS"],
# )

# app = APIGatewayRestResolver(cors=cors_config)


# @app.get("/hello")
# def hello():
#     return {"message": "Hello Shivangi 🚀"}


# @app.get("/health")
# def health():
#     return {"status": "ok"}


# def lambda_handler(event, context):
#     return app.resolve(event, context)


# import json

# def lambda_handler(event, context):
#     return {
#         "statusCode": 200,
#         "headers": {
#             "Access-Control-Allow-Origin": "*",
#             "Access-Control-Allow-Headers": "*",
#             "Access-Control-Allow-Methods": "GET,OPTIONS"
#         },
#         "body": json.dumps({"message": "CORS is working"})
#     }

from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import (
    APIGatewayRestResolver,
    CORSConfig,
)

logger = Logger()

cors_config = CORSConfig(
    allow_origin="*",
    allow_headers=["Content-Type"],
)

app = APIGatewayRestResolver(cors=cors_config)


@app.get("/hello")
def hello():
    return {
        "message": "Hello Shivangi 🚀",
        "version": "latest"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


def lambda_handler(event, context):
    return app.resolve(event, context)