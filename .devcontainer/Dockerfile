# Use an Ubuntu base image
FROM ubuntu:20.04

# Install required dependencies
# RUN apt-get update

# # Install Python and required packages
# RUN apt-get update && apt-get install -y \
#     python-pip \
#     && pip install pyspark==3.0.1 snowflake-connector-python python-dotenv

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && sudo ./aws/install --install-dir /usr/local/aws-cli --bin-dir /usr/local/bin \
    && export PATH=/usr/local/bin:$PATH \
    && echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bashrc \
    && source ~/.bashrc \
    && rm -rf aws awscliv2.zip
