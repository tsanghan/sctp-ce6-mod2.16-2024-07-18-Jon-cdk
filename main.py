#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, S3Backend
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.sns_topic import SnsTopic

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "AWS", region='ap-southeast-1')

        SnsTopic(self, id_="user_updates", name='user-updates-topic', kms_master_key_id="alias/aws/sns", tags={"Name": "tsanghan-ce6"})

        S3Backend(self,
            bucket="sctp-ce6-tfstate",
            key="tsanghan-ce6-mod2_10-2024-07-18-Jon.tfstate",
            region="ap-southeast-1"
        )


app = App()
MyStack(app, "sctp-ce6-mod2.16-2024-07-18-Jon-cdktf")

app.synth()
