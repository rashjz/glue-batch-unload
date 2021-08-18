# Global imports
import sys

# Global variables
JOB_NAME                    = 'AWS DynamoDB Table Unload'
ARGUMENT_KEY_DYNAMODB_TABLE = 'dynamodb_table'
ARGUMENT_KEY_S3_LOCATION    = 's3_location'

def unload():
    # Import AWS Glue specific libraries
    from awsglue.utils import getResolvedOptions
    from pyspark.context import SparkContext
    from awsglue.context import GlueContext
    from awsglue.job import Job

    # Parse command line arguments
    args = getResolvedOptions(sys.argv, [ARGUMENT_KEY_DYNAMODB_TABLE, ARGUMENT_KEY_S3_LOCATION])
    SOURCE_DYNAMODB_TABLE = args[ARGUMENT_KEY_DYNAMODB_TABLE]
    TARGET_S3_LOCATION    = args[ARGUMENT_KEY_S3_LOCATION]

    # Job setup
    spark_context = SparkContext()
    glue_context = GlueContext(spark_context)
    job = Job(glue_context)
    job.init(JOB_NAME, args)

    # Read DynamoDB
    ddb_df = glue_context.create_dynamic_frame.from_options(
        connection_type = "dynamodb",
        connection_options = {
            "dynamodb.input.tableName":SOURCE_DYNAMODB_TABLE,
            "dynamodb.throughput.read.percent":"0.5"
        }
    ).toDF()

    # Write to Amazon S3
    ddb_df.write.json(TARGET_S3_LOCATION)
    
if __name__ == "__main__":
   unload()
