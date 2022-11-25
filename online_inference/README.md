# Starting up
To start working with model inference you have to create image. <br>

You may build it from `online_inference/` 
~~~
docker build . --tag ampiro/mlops_hw2:v1
~~~
or via pulling it from [docker hub](https://hub.docker.com/repository/docker/ampiro/mlops_hw2)
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
I've tried many ways to optimize the image size. 
1) The best size of 76mb was achieved with distroless. However, I can't access such container with bash, so, I've rejected this version. 

2) I've tried multistage build with different distros, but I've always had bigger size. The smallest one was 558mb.

3) And my final version, which is commited, just use python:3.9-slim. The size of final image is 552mb
Note: while I was writing this file, I tried to follow the rules described in [best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/). Thus i have some optimization such as .dockerignore
