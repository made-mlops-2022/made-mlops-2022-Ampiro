from datetime import timedelta
from airflow.models import Variable
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount


var = Variable.set("which_model", "2022-11-26")

default_args = {
    "owner": "airflow",
    "email": ["maximampiro@gmail.com"],
    'email_on_failure': True,
    'email_on_retry': True,
    'retry_exponential_backoff': True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "Data_generator",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:
    generate = DockerOperator(
        image="airflow-generate",
        command="/data/raw/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-generate",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source="/home/ampiro/Ampiro/VK_MLOps/airflow-examples/data/",
                target="/data", type='bind'
            )
        ]
    )
