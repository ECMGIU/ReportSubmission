import os
import boto3, botocore

S3_BUCKET = "bucketeer-304d4dd8-6f5b-4445-8311-22708b0fc363"
S3_KEY = "AKIAX7CRDYXPZI2BJ44L"
S3_SECRET = "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"
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY = os.urandom(32)
DEBUG = True
PORT = 5000

s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET
)


def upload_file_to_s3(file, bucket_name, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        print("Error: Please Retry", e)
        return e

    return "{}{}".format(app.config["S3_LOCATION"], file.filename)
