FROM python:3.9-slim

WORKDIR /application

COPY requirements.txt /application/
RUN pip3 install --no-cache-dir --upgrade --requirement /application/requirements.txt
COPY . /application/

EXPOSE 8000

VOLUME data/ /application/data/

WORKDIR /application/src
CMD ["bash", "run.sh"]