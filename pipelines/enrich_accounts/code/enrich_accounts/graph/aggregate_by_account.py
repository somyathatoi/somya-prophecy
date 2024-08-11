from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from enrich_accounts.config.ConfigStore import *
from enrich_accounts.functions import *

def aggregate_by_account(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("AccountId"))

    return df1.agg(
        count(lit(1)).alias("NumberOfOpportunity"), 
        sum(col("Amount")).alias("Amount"), 
        sum(col("ExpectedRevenue")).alias("ExpectedRevenue"), 
        last(col("ClosedQuarter")).alias("ClosedQuarter")
    )
