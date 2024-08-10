#!/bin/sh
#bash codespaces.bash
source /usr/local/sdkman/bin/sdkman-init.sh

sdk install java 8.0.422-amzn
sdk default java 8.0.422-amzn
sdk install spark 3.0.1
pip install pyspark==3.0.1
pip install snowflake-connector-python python-dotenv

#Install aws cli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install --install-dir /usr/local/aws-cli --bin-dir /usr/local/bin
export PATH=/usr/local/bin:$PATH
echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
rm -rf aws
rm -rf awscliv2.zip