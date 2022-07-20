# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
asdf = dataiku.Dataset("asdf")
asdf_df = asdf.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

asdff_df = asdf_df # For this sample code, simply copy input to output


# Write recipe outputs
asdff = dataiku.Dataset("asdff")
asdff.write_with_schema(asdff_df)
