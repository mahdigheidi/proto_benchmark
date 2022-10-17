FROM python:3.10-slim

WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install protobuf==4.21.7 six==1.16.0

COPY list_item_pb2.py list_item_pb2.py
COPY test.py test.py
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

CMD [ "python", "test.py" ]