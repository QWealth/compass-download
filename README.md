downloads "cabinet file" from nbin


source venv/bin/activate
source .env

to run:
`python3 -m seleniumFun`

to connect:
- add yourself to the inbound security (see cdk)
- download Windows App from the app store
`+` -> "Add PC"

Username: Adminstrator

if you set up a key, then this will get you a password you can use to login:
```
aws ec2 get-password-data \
  --instance-id i-0771ba4943652edc2 \
  --priv-launch-key windows-ec2-key.pem \
  --query 'PasswordData' \
  --output text
  ```

  once connected you get to a regular windows terminal.

to upload:
`./upload_src.sh`


to download get the latest upload files:
  ```
  aws s3 ls s3://cdk-hnb659fds-assets-778983355679-ca-central-1/ --recursive \
  | sort -k1,1 -k2,2 \
  | tail -n 1
  ```

then in the windows vm:
```
$latest = aws s3 ls s3://cdk-hnb659fds-assets-778983355679-ca-central-1/ --recursive |
    Sort-Object -Property LastWriteTime |
    Select-Object -Last 1 |
    ForEach-Object { $_.Split(" ", 4)[-1] }; aws s3 cp "s3://cdk-hnb659fds-assets-778983355679-ca-central-1/$latest" .\
```