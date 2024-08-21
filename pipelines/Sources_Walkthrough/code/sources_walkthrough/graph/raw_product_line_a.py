from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from sources_walkthrough.config.ConfigStore import *
from sources_walkthrough.functions import *

def raw_product_line_a(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("parquet")\
        .option("mergeSchema", True)\
        .load("dbfs:/course_lab/rainforest_biz_sources/sales_parquet/")
