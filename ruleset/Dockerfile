FROM python:alpine3.17

USER root

RUN mkdir -p /usr/share/python

WORKDIR /usr/share/python

RUN pip install --upgrade pip

RUN pip install requests-oauthlib

RUN pip install oauthlib

RUN pip install graphqlclient


RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev

RUN pip install --no-cache-dir matplotlib pandas

CMD tail -f /usr/share/python/py.log


