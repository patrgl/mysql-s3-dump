import subprocess
import os
from datetime import date
import boto3
from botocore.config import Config
from dotenv import load_dotenv
load_dotenv()


# Set DB connection params
host = os.getenv("MYSQLHOST")
port = os.getenv("MYSQLPORT")
user = os.getenv("MYSQLUSER")
password = os.getenv("MYSQLPASSWORD")
database = os.getenv("MYSQLDATABASE")
backup_file = f"{date.today()}.sql"

##set S3 connection
s3 = boto3.resource("s3", 
            aws_access_key_id = os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name = os.getenv('AWS_BUCKET_REGION'),
            config = Config(signature_version='s3v4', s3 = {"addressing_style" : "path"})
        )

##run mysqldump
command = f"mysqldump --port={port} -h{host} -u{user} -p{password} {database} > {backup_file}"
process = subprocess.run(command, shell=True)


if process.returncode != 0:
    print(f"Database backup failed with return code {process.returncode}.")
    quit()
    
print("Database dump completed successfully.")

##upload .sql to S3
try: 
    s3.Bucket(os.getenv('AWS_BUCKET_NAME')).put_object(
    Key = f"backupDB/{backup_file}", 
    Body = open(backup_file, 'rb')
    )
    print("Database dump succesfully uploaded to S3.")
    os.remove(backup_file)
    print("Local copy deleted succesfully.")
except:
    print("Failed to upload dump to S3 bucket.")

    
