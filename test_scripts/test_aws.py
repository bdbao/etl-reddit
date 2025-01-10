from etls.aws_etl import connect_to_s3
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY, AWS_BUCKET_NAME

s3 = connect_to_s3()
print("S3 connection successful:", s3 is not None)
print(s3.exists(AWS_BUCKET_NAME))  # Check if the bucket exists
