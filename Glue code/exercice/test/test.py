import os
import shutil
import sys

import pytest
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StringType, StructField, StructType

# Get the directory of the current script
os
current_dir = os.path.dirname(os.path.realpath(__file__))
# Add the parent directory of the project to sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, "../.."))
sys.path.insert(0, parent_dir)

from exercice.common.reader import create_df_with_schema, read_from_parquet
from exercice.common.writer import write_to_parquet


@pytest.fixture(scope="session")
def spark():
    spark_session = SparkSession.builder.appName("pytest-pyspark").getOrCreate()
    yield spark_session
    spark_session.stop()


def test_read_from_parquet(spark):
    test_data_path = "C:/Users/jselmi/Downloads/tables/tables/reac_ref_act_type"

    df = read_from_parquet(test_data_path)

    assert df is not None
    assert isinstance(df, DataFrame)
    assert df.count() > 0


def test_create_df_with_schema(spark):
    data = [("Jihed", "2000-04-28"), ("Jesser", "2000-06-23")]
    schema = StructType(
        [
            StructField("name", StringType(), True),
            StructField("date", StringType(), True),
        ]
    )
    df = spark.createDataFrame(data, schema)

    new_schema = StructType(
        [
            StructField("name", StringType(), True),
            StructField("date", StringType(), True),
        ]
    )

    # Call the function
    new_df = create_df_with_schema(df, new_schema)

    assert new_df is not None
    assert isinstance(new_df, DataFrame)
    assert len(new_df.columns) > 0


def test_write_to_parquet(spark):
    test_data_path = "C:/Users/jselmi/Downloads/tables/tables/reac_ref_act_type"

    df = read_from_parquet(test_data_path)

    output_file_path = "output/"

    result_path = write_to_parquet(df, output_file_path)

    assert os.path.exists(result_path)
    assert result_path == output_file_path

    written_df = spark.read.parquet(result_path)
    assert written_df.schema == df.schema

    shutil.rmtree(output_file_path)
