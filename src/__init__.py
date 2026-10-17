"""Helper modules for Tugas 1."""

import pandas as pd
import polars as pl

DATA_PATH = "data.csv"

lazy_data = pl.scan_csv(DATA_PATH, infer_schema_length=10000)