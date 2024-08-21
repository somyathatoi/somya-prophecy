from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sources_walkthrough.config.ConfigStore import *
from sources_walkthrough.functions import *
from prophecy.utils import *
from sources_walkthrough.graph import *

def pipeline(spark: SparkSession) -> None:
    df_raw_product_line_a = raw_product_line_a(spark)
    df_raw_product_line_b = raw_product_line_b(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Sources_Walkthrough")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Sources_Walkthrough")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Sources_Walkthrough", config = Config)(pipeline)

if __name__ == "__main__":
    main()
