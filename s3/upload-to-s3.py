#!/usr/bin/env python3

import logging
import boto3
from botocore.exceptions import ClientError
import os
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1',
    # signature_version = 'v4'
)

session = boto3.Session(profile_name='19873900')
s3 = session.client('s3')
# with open("FILE_NAME", "rb") as f:
#     s3.upload_fileobj(f, "BUCKET_NAME", "OBJECT_NAME")


def list_all_buckets():
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3', config=my_config)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


list_all_buckets()
list_bucket_files()
upload_file_to_bucket()