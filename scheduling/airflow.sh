#!/bin/bash

# We use jupyter by default, but here we want to use python
unset PYSPARK_DRIVER_PYTHON

# Clone, install, and run
git clone https://github.com/mozilla/pwmgr_etl pwmgr_dataset
cd pwmgr_dataset
pip install .
spark-submit scheduling/airflow.py
