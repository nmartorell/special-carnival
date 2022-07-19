# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# Read recipe inputs
SARINAPREFIXTEST_COPY = dataiku.Dataset("SARINAPREFIXTEST_COPY")
SARINAPREFIXTEST_COPY_df = dkuspark.get_dataframe(sqlContext, SARINAPREFIXTEST_COPY)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
test_df = SARINAPREFIXTEST_COPY_df # For this sample code, simply copy input to output

# Write recipe outputs
test = dataiku.Dataset("test")
dkuspark.write_with_schema(test, test_df)
