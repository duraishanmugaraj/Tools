#!/bin/bash

# Update the system
sudo yum update -y

# Install git
sudo yum install -y git

#Install aws cli
sudo yum remove awscli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install --install-dir /usr/local/aws-cli --bin-dir /usr/local/bin
export PATH=/usr/local/bin:$PATH
echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
rm -rf aws
rm -rf awscliv2.zip

sudo yum install -y python3-pip
python3 -m pip install --upgrade pip
python3 -m pip install jupyter
python3 -m pip install python-dotenv
python3 -m pip install ipykernel
python3 -m pip install snowflake-connector-python

#sudo cat /var/log/cloud-init-output.log
