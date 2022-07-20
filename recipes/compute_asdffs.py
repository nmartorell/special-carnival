# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
SARINAPREFIXTEST_COPY = dataiku.Dataset("SARINAPREFIXTEST_COPY")
SARINAPREFIXTEST_COPY_df = SARINAPREFIXTEST_COPY.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

asdffs_df = SARINAPREFIXTEST_COPY_df # For this sample code, simply copy input to output


# Write recipe outputs
asdffs = dataiku.Dataset("asdffs")
asdffs.write_with_schema(asdffs_df)
