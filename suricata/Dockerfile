FROM ubuntu:20.04

USER root

RUN apt-get -y update

RUN apt install -y software-properties-common

RUN apt update

RUN add-apt-repository -y ppa:oisf/suricata-stable

RUN apt-get update && apt-get -y install suricata

RUN apt install -y vim

RUN apt install net-tools

RUN mkdir -p /var/log/suricata /var/run/suricata /var/lib/suricata

RUN suricata-update -V --no-check-certificate update-sources && \
    suricata-update -V --no-check-certificate enable-source oisf/trafficid && \
    suricata-update -V --no-check-certificate --no-test --no-reload && \
    /usr/bin/suricata -V

RUN cp -a /etc/suricata /etc/suricata.dist


RUN suricata-update


VOLUME /var/log/suricata
VOLUME /var/lib/suricata
VOLUME /etc/suricata

CMD service suricata start && tail -F /var/log/suricata/suricata.log