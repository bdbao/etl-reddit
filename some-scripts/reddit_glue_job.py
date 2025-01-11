import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from pyspark.sql.functions import concat_ws
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1736565918085 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://bdbao-redditdataengineering/raw/reddit_20250110.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1736565918085")


# convert DynamicFrame to DataFrame
df = AmazonS3_node1736565918085.toDF()

# concatenate the 3 columns into a single column
df_combined = df.withColumn('ESS_updated', concat_ws('-', df['edited'], df['spoiler'], df['stickied']))
df_combined = df_combined.drop('edited', 'spoiler', 'stickied')

# convert back to DynamicFrame
S3bucket_node_combined = DynamicFrame.fromDF(df_combined, glueContext, 'S3bucket_node_combined')


# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=AmazonS3_node1736565918085, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1736564097424", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1736565920208 = glueContext.write_dynamic_frame.from_options(frame=S3bucket_node_combined, connection_type="s3", format="csv", connection_options={"path": "s3://bdbao-redditdataengineering/transformed/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1736565920208")

job.commit()
