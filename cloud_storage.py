import boto3
import os

class CloudStorage:
    def __init__(self, bucket_name):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload_file(self, file_name):
        self.s3.upload_file(file_name, self.bucket_name, file_name)
        print(f"Uploaded {file_name} to {self.bucket_name}")

    def download_file(self, file_name):
        self.s3.download_file(self.bucket_name, file_name, file_name)
        print(f"Downloaded {file_name} from {self.bucket_name}")
