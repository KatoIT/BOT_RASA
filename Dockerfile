FROM ubuntu:18.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --u$
ADD . /ChatBot_v1/
RUN chmod +x /ChatBot_v1/start_services.sh
CMD /ChatBot_v1/start_services.sh
