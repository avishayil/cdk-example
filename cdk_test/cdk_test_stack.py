from aws_cdk import core
from example_service import example_service

class CdkTestStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        example_service.ExampleService(self, "Examples")
