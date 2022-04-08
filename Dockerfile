FROM ubuntu:latest

COPY . /app/

WORKDIR /app

RUN apt-get update
RUN apt-get install screen
RUN apt-get install python3.8 -y
RUN apt-get install python3-pip -y
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

CMD [ "./run_all.sh" ]
