# Use an Ubuntu base image
FROM ubuntu:20.04

# Install required dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    zip \
    sudo \
    gnupg2 \
    zip \
    && rm -rf /var/lib/apt/lists/*

# Install SDKMAN!
RUN curl -s "https://get.sdkman.io" | bash \
    && bash -c "source $HOME/.sdkman/bin/sdkman-init.sh && \
                sdk install java 8.0.422-amzn && \
                sdk default java 8.0.422-amzn && \
                sdk install spark 3.0.1"

# Install Python and required packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    && pip3 install pyspark==3.0.1 snowflake-connector-python python-dotenv

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && sudo ./aws/install --install-dir /usr/local/aws-cli --bin-dir /usr/local/bin \
    && export PATH=/usr/local/bin:$PATH \
    && echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bashrc \
    && source ~/.bashrc \
    && rm -rf aws awscliv2.zip
