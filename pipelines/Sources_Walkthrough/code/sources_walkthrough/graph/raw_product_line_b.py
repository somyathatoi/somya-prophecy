from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from sources_walkthrough.config.ConfigStore import *
from sources_walkthrough.functions import *

def raw_product_line_b(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("json")\
        .option("dropFieldIfAllNull", True)\
        .schema(
          StructType([
            StructField("_corrupt_record", StringType(), True), StructField("date_introduced", StringType(), True), StructField("main_category", StringType(), True), StructField("name", StringType(), True), StructField("price_usd_cents", StringType(), True), StructField("product_id", LongType(), True), StructField("sub_category", StringType(), True)
        ])
        )\
        .load("dbfs:/course_lab/rainforest_biz_sources/product_line_b/product_line_b.json")
