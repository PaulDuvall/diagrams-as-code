from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.network import Route53
from diagrams.aws.network import APIGateway

with Diagram("Running Lambda", show=False):
    dns = Route53("dns")

    with Cluster("Event Flows"):
        with Cluster("Processing"):
            handlers = [Lambda("GetData"),
                        Lambda("TestData"),
                        Lambda("proc3")]
                        
    with Cluster("Storage"):
        handlers = [S3("Pipeline"),
                    S3("Artifacts"),
                    S3("Storage1")]
        
    store = S3("events store") 
    tbd = APIGateway("GetData") 

    handlers >> store