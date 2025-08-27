#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { WindowsEc2UtilityStack } from "../lib/windows-ec2-cdk-stack";

const app = new cdk.App();
new WindowsEc2UtilityStack(app, "WindowsEc2UtilityStack", {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});