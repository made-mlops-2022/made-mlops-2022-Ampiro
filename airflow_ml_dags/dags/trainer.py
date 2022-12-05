from datetime import timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.sensors.python import PythonSensor
from docker.types import Mount

from myutils import wait_for_file


default_args = {
    "owner": "airflow",
    "email": ["maximampiro@gmail.com"],
    'email_on_failure': True,
    'email_on_retry': True,
    'retry_exponential_backoff': True,
    "retry_delay": timedelta(minutes=5),
    'retries': 3
}

with DAG(
        "Trainer",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=days_ago(10),
) as dag:

    wait = PythonSensor(
        task_id="wait_for_file",
        python_callable=wait_for_file,
        op_kwargs={'file_path': 'data/raw/{{ ds }}/data.csv'},
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke",
    )

    preprocess = DockerOperator(
        image="airflow-preprocess",
        command="--input-dir /data/raw/{{ ds }} --output-dir /data/processed/{{ ds }}",
        task_id="docker-airflow-preprocess",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source="/home/ampiro/Ampiro/VK_MLOps/airflow-examples/data/",
                target="/data", type='bind'
            )
        ]
    )

    split = DockerOperator(
        image="airflow-split",
        command="--input-dir /data/raw/{{ ds }} --output-dir /data/processed/{{ ds }}",
        task_id="docker-airflow-split",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source="/home/ampiro/Ampiro/VK_MLOps/airflow-examples/data/",
                target="/data", type='bind'
            )
        ]
    )

    train = DockerOperator(
        image="airflow-train",
        command="--data-dir /data/processed/{{ ds }} --model-save-dir /data/models/{{ ds }}",
        task_id="docker-airflow-train",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source="/home/ampiro/Ampiro/VK_MLOps/airflow-examples/data/",
                target="/data", type='bind'
            )
        ]
    )

    evaluate = DockerOperator(
        image="airflow-predict",
        command="--data-dir /data/processed/{{ ds }} --model-dir /data/models/{{ ds }} --output-dir /data/evaluation/predictions/{{ ds }}",
        task_id="docker-airflow-evaluate",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source="/home/ampiro/Ampiro/VK_MLOps/airflow-examples/data/",
                target="/data", type='bind'
            )
        ]
    )

    metrics = DockerOperator(
        image="airflow-metrics",
        command="--data-dir /data/processed/{{ ds }} --data-type train --predict-dir /data/evaluation/predictions/{{ ds }} --output-dir /data/evaluation/metrics/{{ ds }}",
        task_id="docker-airflow-metrics",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source="/home/ampiro/Ampiro/VK_MLOps/airflow-examples/data/",
                target="/data", type='bind'
            )
        ]
    )

    wait >> preprocess >> split >> train >> evaluate >> metrics
