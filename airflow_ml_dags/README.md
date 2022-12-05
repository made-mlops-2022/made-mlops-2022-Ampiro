# Airflow setup

To run airflow execute those commands
~~~
export FERNET_KEY=$(python3 -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
docker-compose up --build
~~~

Entering Airflow [localhost:8080](http://localhost:8080/home):
- login:    `admin`
- password: `admin`

To run predict you may change variable `which_model` in Airflow
- "2022-11-26" # Example

To run tests:
~~~
docker exec -it airflow-examples-scheduler-1 pytest tests/
~~~

To stop airflow:
~~~
docker-compose down --remove-orphans
~~~