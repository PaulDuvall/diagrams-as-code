# https://diagrams.mingrammer.com/docs/nodes/aws
from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway
from diagrams.aws.database import DynamodbTable
from diagrams.aws.security import IdentityAndAccessManagementIam
from diagrams.aws.devtools import Codebuild
from diagrams.aws.devtools import Codecommit
from diagrams.aws.devtools import Codedeploy
from diagrams.aws.devtools import Codepipeline
from diagrams.aws.management import Cloudformation
from diagrams.aws.devtools import CommandLineInterface

with Diagram("Serverless Web Apps", show=False, direction="TB"):
    

    with Cluster("CloudFormation"):
        cloudformation = Cloudformation("Stack")
        cloudformation >> IdentityAndAccessManagementIam("IAM") >> Codecommit("CodeCommit") >> Codebuild("CodeBuild") >> S3("S3") >> Codepipeline("CodePipeline")

    with Cluster("CodePipeline"):
        codepipeline = Codepipeline("Pipeline")
        codepipeline >> Codecommit("CodeCommit") >> Codebuild("CodeBuild") >> Cloudformation("CloudFormation")
      
    with Cluster("Serverless Application Model"):
        sam = Cloudformation("SAM Template")
        sam >> APIGateway("API Gateway") >> Lambda("Lambda") >> DynamodbTable("DynamoDB")
        cloudformation >> codepipeline >> sam
        

