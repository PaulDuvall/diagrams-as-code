# https://diagrams.mingrammer.com/docs/nodes/aws
from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.network import Route53
from diagrams.aws.network import APIGateway
from diagrams.aws.database import DynamodbTable 

with Diagram("Running Lambda", show=False):
    LambdaGetData = Lambda("GetData")
    myDynamodbTable = DynamodbTable("CloudProviders")

                        
    with Cluster("Storage"):
        s3 = [S3("Pipeline"),
                    S3("Artifacts"),
                    S3("Storage1")]
        
    api = APIGateway("GetData") 

    api >> LambdaGetData >> myDynamodbTable