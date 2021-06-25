FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY app.py /usr/src/app/
COPY templates /usr/src/app/templates
COPY static /usr/src/app/static

CMD python -u app.py
