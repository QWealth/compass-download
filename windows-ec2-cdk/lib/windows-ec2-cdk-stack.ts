import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as s3assets from "aws-cdk-lib/aws-s3-assets";
import * as path from "path";
import * as iam from "aws-cdk-lib/aws-iam";

export class WindowsEc2UtilityStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    cdk.Tags.of(this).add("product", "ifm");

    const myIp = "107.159.65.239/32";

    const vpc = ec2.Vpc.fromLookup(this, "DefaultVpc", { isDefault: true });

    const sg = new ec2.SecurityGroup(this, "WindowsEc2", {
      vpc,
      description: "Allow Thomas and databases",
      allowAllOutbound: true,
    });

    sg.addIngressRule(ec2.Peer.ipv4(myIp), ec2.Port.tcp(3389), "Allow RDP from my IP");
    sg.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(5432), "Allow DB traffic");

    const windowsAmi = ec2.MachineImage.latestWindows(
      ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE
    );

    const instance = new ec2.Instance(this, "WindowsInstance", {
      vpc,
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MICRO),
      machineImage: windowsAmi,
      securityGroup: sg,
      vpcSubnets: { subnetType: ec2.SubnetType.PUBLIC },
      keyName: "windows-ec2-key",
    });

    const srcAsset = new s3assets.Asset(this, "SrcAsset", {
      path: path.join(__dirname, "../../src"),
    });

    srcAsset.grantRead(instance.role);

    const s3User = new iam.User(this, "S3PullUser", {
      userName: "windows-ec2-s3-user",
    });

    const bucketPolicy = new iam.PolicyStatement({
      actions: ["s3:GetObject"],
      resources: [
        `arn:aws:s3:::${srcAsset.s3BucketName}/${srcAsset.s3ObjectKey}`, // ✅ fixed
      ],
      effect: iam.Effect.ALLOW,
    });

    s3User.addToPolicy(bucketPolicy);

    const accessKey = new iam.CfnAccessKey(this, "S3PullUserKey", {
      userName: s3User.userName,
    });

    instance.userData.addCommands(
      "Set-ExecutionPolicy Bypass -Scope Process -Force",
      "[System.Net.ServicePointManager]::SecurityProtocol = 'Tls12'",
      "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))",
      "choco install -y python3",
      "choco install -y vim",
      "choco install -y awscli",

      "if (-not (Test-Path C:\\src)) { New-Item -ItemType Directory -Path C:\\src }",

      `Read-S3Object -BucketName cdk-hnb659fds-assets-778983355679-ca-central-1 -Key ${srcAsset.s3ObjectKey} -File C:\\\\src.zip`,
      "Expand-Archive -Force C:\\\\src.zip C:\\\\src",

      `schtasks /Create /SC DAILY /TN RunMainPy /TR "python C:\\\\src\\\\main.py" /ST 04:00`
    );

    new cdk.CfnOutput(this, "S3PullUserAccessKeyId", { value: accessKey.ref });
    new cdk.CfnOutput(this, "S3PullUserSecretAccessKey", { value: accessKey.attrSecretAccessKey });
  }
}
