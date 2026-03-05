from aws_cdk import (
    Stack,
    Duration,
    CfnOutput,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_iam as iam,
    aws_logs as logs,
    aws_ecr as ecr,
)
from constructs import Construct
import aws_cdk.aws_apprunner_alpha as apprunner


class PracticeBackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

       
        backend_repo = ecr.Repository.from_repository_name(
            self,
            "BackendLambdaRepo",
            "practice-lambda"  
        )

        docker_lambda = _lambda.DockerImageFunction(
            self,
            "DockerLambda",
            code=_lambda.DockerImageCode.from_ecr(
                repository=backend_repo,
                tag="latest"
            ),
            timeout=Duration.seconds(30)
        )


        # -----------------------------
        # 2️⃣ API Gateway
        # -----------------------------
        api = apigw.LambdaRestApi(
        self,
        "DockerApi",
        handler=docker_lambda,
        proxy=True,   # ✅ keep proxy
        )


        CfnOutput(
            self,
            "ApiEndpoint",
            value=api.url
        )

        # -----------------------------
        # 3️⃣ Frontend App Runner (React)
        # -----------------------------
        frontend_repo = ecr.Repository.from_repository_name(
            self,
            "FrontendRepo",
            "tablportal_practice"  
        )

        frontend_service = apprunner.Service(
            self,
            "FrontendAppRunnerService",
            source=apprunner.Source.from_ecr(
                repository=frontend_repo,
                tag="v2",
                image_configuration=apprunner.ImageConfiguration(
                    port=80
                )
            )
        )

        CfnOutput(
            self,
            "FrontendURL",
            value=frontend_service.service_url
        )