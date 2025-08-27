#!/bin/bash
# Replace with your bucket and folder
BUCKET_NAME="cdk-hnb659fds-assets-778983355679-ca-central-1"
LOCAL_SRC_PATH="./src"

# Sync local src/ to S3
aws s3 sync s3://cdk-hnb659fds-assets-778983355679-ca-central-1/src C:\src --delete

echo "Upload complete."

