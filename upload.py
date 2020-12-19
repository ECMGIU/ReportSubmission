import os
import boto3, botocore

S3_BUCKET = "bucketeer-304d4dd8-6f5b-4445-8311-22708b0fc363"
S3_KEY = "AKIAX7CRDYXPZI2BJ44L"
S3_SECRET = "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"
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY = os.urandom(32)
DEBUG = True
PORT = 5000



