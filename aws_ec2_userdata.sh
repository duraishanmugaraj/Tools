#!/bin/bash

# Update the system
sudo yum update -y

# Install git
sudo yum install -y git

# Install Python 3.9 and pip
sudo yum install -y python3-pip

# Upgrade pip to the latest version
python3 -m pip install --upgrade pip

# Install Jupyter Notebook
python3 -m pip install jupyter

# Install python-dotenv
python3 -m pip install python-dotenv

# Install IPython kernel
python3 -m pip install ipykernel

# Install Snowflake connector
python3 -m pip install snowflake-connector-python

#sudo cat /var/log/cloud-init-output.log
