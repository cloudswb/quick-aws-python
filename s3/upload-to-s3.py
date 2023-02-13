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

# Initialize a s3 client object using a specific profile name.
# refer to : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
session = boto3.Session(profile_name='19873900')
s3 = session.client('s3')


def list_all_buckets():
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

def list_bucket_files():
    
    response = s3.list_objects(Bucket='zkdoc', MaxKeys=2)

    for my_bucket_object in response['Contents']:
        print(my_bucket_object['Key'])


def upload_file_to_bucket(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    s3.upload_file(file_name, bucket, object_name)       

def delete_object_from_bucket(bucket, object_name=None):
    """Delete a file from an S3 bucket

    :param bucket: Bucket to delete from.
    :param object_name: S3 object name.
    :return: True if file was uploaded, else False
    """
    response = s3.delete_object(Bucket='zkdoc', Key='Tech_Transcripts_reInvent_Combined.pdf')
    print(response)




# Bucket operations refer to: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_object
# List all buckets using the specific profile credentional.
list_all_buckets()
# list fils in bucket.
list_bucket_files()
# upload one file to bucket.
upload_file_to_bucket('/Users/zhangkap/Downloads/Tech_Transcripts_reInvent_Combined.pdf', 'zkdoc', 'Tech_Transcripts_reInvent_Combined.pdf')
# delete one object from the specific bucket.
delete_object_from_bucket('Tech_Transcripts_reInvent_Combined.pdf', 'zkdoc')
