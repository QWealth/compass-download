aws ec2 get-password-data \
  --instance-id i-0390cd48483156cfe \
  --priv-launch-key windows-ec2-key.pem \
  --query 'PasswordData' \
  --output text

