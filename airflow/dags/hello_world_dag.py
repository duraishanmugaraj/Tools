from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta  # Import timedelta
import logging

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create a DAG instance
dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval='@daily',
    start_date=datetime(2024, 8, 14),
    catchup=False,
)

# Define Python task
def hello_world():
    logging.info("Hello, World!")

# Create Python and Bash tasks
python_task = PythonOperator(
    task_id='python_hello_task',
    python_callable=hello_world,
    dag=dag,
)

bash_task = BashOperator(
    task_id='bash_hello_task',
    bash_command='echo "Hello from Bash!"',
    dag=dag,
)

# Set task dependencies
python_task >> bash_task
