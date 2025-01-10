import boto3
import pymysql

# AWS configuration
AWS_REGION = "us-east-1"
S3_BUCKET = "example-s3-bucket"
S3_KEY = "example-data/sample.csv"

# RDS Configuration
RDS_HOST = "example-rds-instance.abcdefg.us-east-1.rds.amazonaws.com"
RDS_PORT = 3306
RDS_USER = "admin"
RDS_PASSWORD = "password123"
RDS_DB = "exampledb"

# Glue configuration
GLUE_DATABASE = "example-glue-database"

def read_data_from_s3():
    print("Reading data from S3...")
    s3_client = boto3.client('s3', region_name=AWS_REGION)
    response = s3_client.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
    return response['Body'].read().decode('utf-8')

def write_data_to_rds(data):
    try:
        print("Attempting to write data to RDS...")
        connection = pymysql.connect(
            host=RDS_HOST,
            port=RDS_PORT,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB
        )
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO example_table (data_column) VALUES (%s)", (data,))
            connection.commit()
        print("Data successfully written to RDS!")
        return True
    except Exception as e:
        print(f"Error writing to RDS: {e}")
        return False

def write_data_to_glue(data):
    print("Writing data to Glue...")
    glue_client = boto3.client('glue', region_name=AWS_REGION)
    # Dummy logic to represent Glue usage
    print(f"Data written to Glue: {data}")

def main():
    data = read_data_from_s3()
    if not write_data_to_rds(data):
        write_data_to_glue(data)

if __name__ == "__main__":
    main()