from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_ecr as ecr,
)
from constructs import Construct


class PracticeBackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        repository = ecr.Repository.from_repository_name(
            self,
            "PracticeLambdaRepo",
            "practice-lambda"
        )

        lambda_function = _lambda.DockerImageFunction(
            self,
            "DockerLambda",
            code=_lambda.DockerImageCode.from_ecr(
            repository,
            tag_or_digest="latest"),
        )

        apigateway.LambdaRestApi(
            self,
            "DockerApi",
            handler=lambda_function,
        )