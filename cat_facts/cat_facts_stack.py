from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)

class CatFactsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda = _lambda.Function(
            self,
            'CatFactsHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda/deployment.zip'),
            handler='cat_facts.handler',
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda
        )
