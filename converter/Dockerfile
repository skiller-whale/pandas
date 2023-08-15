FROM python:3.11

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app/

ADD scripts/jupyter_converter.py jupyter_converter.py

RUN mkdir .exercises

CMD python jupyter_converter.py
