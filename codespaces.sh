
sudo apt-get update
sudo apt-get install -y openjdk-11-

wget https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-without-hadoop.tgz

tar xzf spark-3.0.1-bin-without-hadoop.tgz
sudo mv spark-3.0.1-bin-without-hadoop /usr/local/spark
rm -rf spark-3.0.1-bin-without-hadoop.tgz

echo 'export SPARK_HOME=/usr/local/spark' >> ~/.bashrc
echo 'export PATH=$PATH:$SPARK_HOME/bin' >> ~/.bashrc
source ~/.bashrc


sdk install java 8.0.422-amzn
sdk install spark 3.0.1
pip install pyspark==3.0.1
