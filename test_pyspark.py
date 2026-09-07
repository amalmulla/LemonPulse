import pytest
import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql import Row
from LemonPulse import extract_anomalies

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


@pytest.fixture(scope="session")
def spark():
    """Create a local Spark session for testing."""
    spark_session = SparkSession.builder \
        .master("local[1]") \
        .appName("pytest-pyspark-local-testing") \
        .getOrCreate()
    yield spark_session
    spark_session.stop()

def test_extract_anomalies_tuple(spark):
    """Test extract_anomalies with tuple RDD format."""
    # Data format: (parameter, value)
    data = [
        ("ph", 6.2),
        ("ph", 7.1),
        ("ph", 5.8),
        ("humidity", 40.0),
        ("humidity", 55.5),
        ("temp", 22.0),
        ("temp", 30.0),
        ("temp", 15.0)
    ]
    rdd = spark.sparkContext.parallelize(data)
    
    results = extract_anomalies(rdd, is_dataframe_row=False)
    
    # results is a list of tuples: [("ph", (min, max)), ...]
    results_dict = {k: v for k, v in results}
    
    assert results_dict["ph"] == (5.8, 7.1)
    assert results_dict["humidity"] == (40.0, 55.5)
    assert results_dict["temp"] == (15.0, 30.0)

def test_extract_anomalies_dataframe_row(spark):
    """Test extract_anomalies with DataFrame Row format."""
    data = [
        Row(parameter="ph", value=6.2),
        Row(parameter="ph", value=7.1),
        Row(parameter="ph", value=5.8),
        Row(parameter="humidity", value=40.0),
        Row(parameter="humidity", value=55.5),
        Row(parameter="temp", value=22.0),
        Row(parameter="temp", value=30.0),
        Row(parameter="temp", value=15.0)
    ]
    rdd = spark.sparkContext.parallelize(data)
    
    results = extract_anomalies(rdd, is_dataframe_row=True)
    
    results_dict = {k: v for k, v in results}
    
    assert results_dict["ph"] == (5.8, 7.1)
    assert results_dict["humidity"] == (40.0, 55.5)
    assert results_dict["temp"] == (15.0, 30.0)
