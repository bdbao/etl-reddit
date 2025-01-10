# Data Pipeline with Reddit, Airflow, Celery, Postgres, S3, AWS Glue, Athena, and Redshift

This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Reddit data into a Redshift data warehouse. The pipeline leverages a combination of tools and services including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

## Table of Contents

- [Data Pipeline with Reddit, Airflow, Celery, Postgres, S3, AWS Glue, Athena, and Redshift](#data-pipeline-with-reddit-airflow-celery-postgres-s3-aws-glue-athena-and-redshift)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Architecture](#architecture)
  - [Prerequisites](#prerequisites)
  - [System Setup](#system-setup)
  - [More steps:](#more-steps)

## Overview

The pipeline is designed to:

1. Extract data from Reddit using its API.
2. Store the raw data into an S3 bucket from Airflow.
3. Transform the data using AWS Glue and Amazon Athena.
4. Load the transformed data into Amazon Redshift for analytics and querying.

## Architecture
![RedditDataEngineering.png](assets%2FRedditDataEngineering.png)
1. **Reddit API**: Source of the data.
2. **Apache Airflow & Celery**: Orchestrates the ETL process and manages task distribution.
3. **PostgreSQL**: Temporary storage and metadata management.
4. **Amazon S3**: Raw data storage.
5. **AWS Glue**: Data cataloging and ETL jobs.
6. **Amazon Athena**: SQL-based data transformation.
7. **Amazon Redshift**: Data warehousing and analytics.

## Prerequisites
- AWS Account with appropriate permissions for S3, Glue, Athena, and Redshift.
- Reddit API credentials.
- Docker Installation.
- Python 3.9 or higher (e.g: 3.10.16).

## System Setup
1. Clone the repository.
   ```bash
    git clone https://github.com/bdbao/etl-reddit.git
   ```
2. Create a virtual environment.
   ```bash
    python -m venv venv
   ```
3. Activate the virtual environment.
   ```bash
    source venv/bin/activate
   ```
4. Install the dependencies.
   ```bash
    pip install -r requirements.txt
   ```
5. Rename the configuration file and the credentials to the file.
   ```bash
    mv config/config.conf.example config/config.conf
   ```
6. Starting the containers
   ```bash
    docker-compose up -d
   ```
7. Launch the Airflow web UI.
   ```bash
    open http://localhost:8080
   ```

## More steps:
- How to Get `reddit_secret_key` and `reddit_client_id` for `config.conf`:
   ```
   ### 1. Log in to Reddit
   - Go to [https://www.reddit.com](https://www.reddit.com).
   - Log in with your Reddit account.

   ### 2. Access the Developer Portal
   - Visit [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).

   ### 3. Create a New Application
   - Scroll down and click **"Create App"** or **"Create Another App"**.
   - **Name:** Provide a name for your app (e.g., `"Reddit ETL App"`).
   - **App Type:** Select **script**.
   - **Description:** Provide a short description of your app.
   - **About URL:** (Optional) Leave blank.
   - **Redirect URI:** Set it to `http://localhost:8080`. (Required for OAuth but can be left as is for now.)
   - **Permissions:** No additional permissions are needed for basic data extraction.

   ### 4. Retrieve Client ID and Secret Key
   - Once created, the **Client ID** will appear at the top of the application page (a string under your app name and "personal use script").
   - The **Secret Key** will be listed under the `"secret"` section.
   ```
- How to Get AWS Credentials and Bucket Details for `config.conf`:
   ```
   ### 1. **Create or Access Your AWS Account**
   - Go to [https://aws.amazon.com](https://aws.amazon.com) and log in to your AWS account.
   - If you don't have an AWS account, create a new one.

   ---

   ### 2. **Access AWS IAM (Identity and Access Management)**
   - Open the [IAM Console](https://console.aws.amazon.com/iam/).
   - Navigate to the **Users** section.
   - Either select an existing user or create a new one if necessary.

   ---

   ### 3. **Get Your AWS Access Key and Secret Key**
   - **If creating a new user:**
   - Assign the necessary permissions (e.g., `AmazonS3FullAccess`, `AmazonS3ReadOnlyAccess`).
   - After creating the user, you will be shown the **Access Key ID** and **Secret Access Key**. 
   - **Copy them securely**, as you won't be able to view them again.

   - **If using an existing user:**
   - Go to **Users > Security Credentials** tab.
   - Under the **Access Keys** section, you can create a new key if none exists.

   ---

   ### 4. **Get the AWS Session Token (Optional for Temporary Credentials)**
   - If you're using **temporary credentials**, you will need a **Session Token**.
   - Generate temporary credentials using the AWS CLI:

   `aws sts get-session-token --duration-seconds 3600`

   ### 5. Set the AWS Region
   - The AWS Region is the data center where your S3 bucket resides.
   - Example: us-east-1 for US East (N. Virginia).

   ### 6. Get the S3 Bucket Name
   - To find your S3 bucket name:
      - Go to the S3 Console.
      - Locate the name of your existing bucket.
   - If creating a new bucket:
      - Click Create Bucket.
      - Provide a unique bucket name and select a region.
      - Complete the other settings and create the bucket.
   ```
- Open localhost:8080 (username/pw is **admin**)
