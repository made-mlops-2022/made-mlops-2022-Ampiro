from datetime import timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

from airflow.sensors.python import PythonSensor
from myutils import wait_for_file

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
        "Predictor",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:

    wait_train_data = PythonSensor(
        task_id="wait_train_data",
        python_callable=wait_for_file,
        op_kwargs={'file_path': 'data/processed/{{ ds }}/train_data.csv'},
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke",
    )

    wait_model = PythonSensor(
        task_id="wait_model",
        python_callable=wait_for_file,
        op_kwargs={
            'file_path': 'data/models/{{ var.value.which_model }}/model.pkl'
        },
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke",
    )

    predict = DockerOperator(
        image="airflow-predict",
        command="--data-dir /data/processed/{{ ds }} --model-dir /data/models/{{ var.value.which_model }} --output-dir /data/inference/predictions/{{ ds }}",
        task_id="docker-airflow-predict",
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
        command="--data-dir /data/processed/{{ ds }} --data-type train --predict-dir /data/inference/predictions/{{ ds }} --output-dir /data/inference/metrics/{{ ds }}",
        task_id="docker-airflow-predict_metrics",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source="/home/ampiro/Ampiro/VK_MLOps/airflow-examples/data/",
                target="/data", type='bind'
            )
        ]
    )

    wait_model >> wait_train_data >> predict >> metrics
