import aws_cdk as core
import aws_cdk.assertions as assertions

from practice_backend.practice_backend_stack import PracticeBackendStack

# example tests. To run these tests, uncomment this file along with the example
# resource in practice_backend/practice_backend_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PracticeBackendStack(app, "practice-backend")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
