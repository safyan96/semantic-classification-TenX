from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_iam as iam,
    aws_ecs_patterns as ecs_patterns,
    aws_logs as logs,
    Stack,
    App,
    CfnOutput,
    CfnParameter,
)
from constructs import Construct


class FastAPIStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        project_name_param = CfnParameter(
            self, "ProjectName", type="String", description="Name of the project"
        )

        # Create a VPC for the service
        vpc = ec2.Vpc(self, "FastAPIVpc", max_azs=2)

        # Define a Fargate service
        task_definition = ecs.FargateTaskDefinition(
            self, "FastAPITaskDefinition", cpu=4 * 256, memory_limit_mib=8 * 512
        )

        # Add a container to the task definition
        container = task_definition.add_container(
            "FastAPIContainer",
            image=ecs.ContainerImage.from_registry("pacman1994/fast:v1"),
            logging=ecs.AwsLogDriver(
                stream_prefix="FastAPI",
                log_group=logs.LogGroup(self, "FastAPILogGroup"),
            ),
        )

        # Expose port 8002 for the FastAPI container
        container.add_port_mappings(
            ecs.PortMapping(
                container_port=8002, host_port=8002, protocol=ecs.Protocol.TCP
            )
        )

        # Create the Fargate service
        service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "FastAPIService",
            cluster=ecs.Cluster(self, "FastAPICluster", vpc=vpc),
            task_definition=task_definition,
            desired_count=2,
        )

        # Output the load balancer DNS
        CfnOutput(
            self, "LoadBalancerDNS", value=service.load_balancer.load_balancer_dns_name
        )


app = App()
FastAPIStack(app, "FastAPIStack")
app.synth()
