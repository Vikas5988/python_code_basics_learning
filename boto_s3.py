import boto3


s3=boto3.resource("s3")
print(s3)
def show_buckets(x):
    for bucket in x.buckets.all():
        print(bucket.name)
               
               
def create_buckets(y):
   # s3.create_bucket(Bucket="vsr-boto3-test-1-mar-2026")
        s3.create_bucket(Bucket="vsr-boto3-test2-1-mar-2026",
                     CreateBucketConfiguration={
                         'LocationConstraint': 'ap-south-1', #it should match the default region set
                         },)
               

create_buckets(s3)

show_buckets(s3)



# s4 is written instead of S3 to check the function of boto3. 

""" s5=boto3.resource("s3")
def show_buckets(x):
    for bucket in x.buckets.all():
        print(bucket.name)
               
show_buckets(s5) """


