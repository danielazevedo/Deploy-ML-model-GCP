# GCP-Projects

This repository presents two simple projects made using Google Cloud Platform: **Deploy_ML_model** and **Run_ETL_pipeline**.


All the code was run through the Google Cloud SDK (https://cloud.google.com/sdk).


## Deploy_ML_model

Deployment of a Machine Learning model in Google Cloud Platform, using the **App Engine**.

This was implemented using Python and Flask and the ML model trained was a Multinomial Naive Bayes. The goal of the ML model is to predict if a given text is a spam message or not.

For an example of how to use **App Engine**, see https://console.cloud.google.com/getting-started?tutorial=python_gae_quickstart.


## Run_ETL_pipeline

Creation of a data pipeline that extracts data from parquet files, then applies some transformations and finally stores the data in a database. This was implemented using **Dataflow** service from GCP (using Apache Beam).

A **Bucket Storage** was created to store some data and **Big Query** was used to create the database and store the output from the ETL process.

For an example of how to use **Dataflow**, see https://console.cloud.google.com/getting-started?walkthrough_tutorial_id=python_dataflow_quickstart.
