FROM ubuntu

RUN apt-get update
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install curl gnupg


RUN apt-get install -y python3.7
RUN apt install -y python3-pip
RUN pip3 install --upgrade pip

RUN pip install pandas
RUN mkdir -p /app
COPY . /app
WORKDIR app

ENTRYPOINT ["python3", "run.py"]




