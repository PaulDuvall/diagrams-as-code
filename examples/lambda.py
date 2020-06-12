# https://diagrams.mingrammer.com/docs/nodes/aws
from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.network import Route53
from diagrams.aws.network import APIGateway
from diagrams.aws.database import DynamodbTable
from diagrams.aws.security import IdentityAndAccessManagementIam
from diagrams.aws.devtools import Codebuild
from diagrams.aws.devtools import Codecommit
from diagrams.aws.devtools import Codedeploy
from diagrams.aws.devtools import Codepipeline
from diagrams.aws.management import Cloudformation

with Diagram(show=False):

    with Cluster("CloudFormation"):
        cloudformation = [S3("Pipeline"),
                          Codecommit("Source"),
                          S3("Storage")]

    with Cluster("CodePipeline"):
        codepipeline = [Codecommit("Source"),
                          Codebuild("BuildSAM"),
                          Cloudformation("DeployLambda")]
                        
    with Cluster("SAM"):
        sam = [APIGateway("GetData"),
                    Lambda("GetData"),
                    DynamodbTable("CloudProviders")]
        

    cloudformation >> codepipeline >> sam