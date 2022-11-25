# Starting up
To start working with model inference you have to create image. <br>

You may build it from `online_inference/` 
~~~
docker build . --tag ampiro/mlops_hw2:v1
~~~
or via pulling it from docker hub
~~~
docker pull ampiro/mlops_hw2:v1
~~~

Starting container and enter interactive mode
~~~
docker run -it -d --name coampiro ampiro/mlops_hw2:v1
docker exec -it coampiro bash
~~~
Running test from local machine
~~~
docker exec -it coampiro bash ./run_tests.sh
~~~

# Image size optimization
`yet to be added`

