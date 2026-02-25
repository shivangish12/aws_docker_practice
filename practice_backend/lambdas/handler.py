from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver

logger = Logger()
app = APIGatewayRestResolver()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "Hello Shivangi 🚀"}


def lambda_handler(event, context):
    return app.resolve(event, context)