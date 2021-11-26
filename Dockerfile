# FROM ubuntu:18
# FROM rasa/rasa:2.8.10
FROM rasa/rasa
# FROM python:alpine3.8
ENTRYPOINT []
# RUN apt-get update && apt-get install -y python3 python3-pip && pip install psycopg2-binary && python3 -m pip install --no-cache rasa==2.8.10
# ADD . /ChatBot_v1/
# RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /ChatBot_v1
COPY . /ChatBot_v1
USER root
RUN pip install -r requirements.txt
# RUN chmod a+x /ChatBot_v1/start_services.sh
EXPOSE 5005
CMD /ChatBot_v1/start_services.sh
