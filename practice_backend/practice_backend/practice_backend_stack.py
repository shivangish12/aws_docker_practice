from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)
from constructs import Construct


class PracticeBackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        lambda_function = _lambda.Function(
        self,
        "MyLambda",
        runtime=_lambda.Runtime.PYTHON_3_11,
        handler="handler.lambda_handler",
        code=_lambda.Code.from_asset("lambdas"),
)

        apigateway.LambdaRestApi(
            self,
            "MyApi",
            handler=lambda_function,
        )