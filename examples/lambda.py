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
from diagrams.aws.devtools import CommandLineInterface
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("Serverless Web Apps", show=False):
    

    with Cluster("CloudFormation"):
        cloudformation = Cloudformation("Stack")
        cloudformation >> IdentityAndAccessManagementIam("Permissions") >> Codecommit("Build") >> Codebuild("Deploy") >> S3("Deploy") >> Codepipeline("Pipeline")

    with Cluster("CodePipeline"):
        codepipeline = Codepipeline("Pipeline")
        codepipeline >> Codecommit("Source") >> Codebuild("Build") >> Cloudformation("Deploy")
      
    with Cluster("Serverless Application Model"):
        sam = Cloudformation("SAM Template")
        sam >> APIGateway("GetData") >> Lambda("GetData") >> DynamodbTable("CloudProviders")
        cloudformation >> codepipeline >> sam
        

