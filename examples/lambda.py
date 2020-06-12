from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.network import Route53

with Diagram("Running Lambda", show=False):
    dns = Route53("dns")

    with Cluster("Event Flows"):
        with Cluster("Processing"):
            handlers = [Lambda("proc1"),
                        Lambda("proc2"),
                        Lambda("proc3")]
        
    store = S3("events store")        

    handlers >> store