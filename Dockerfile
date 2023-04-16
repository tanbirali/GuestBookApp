FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn"  , "-b", "0.0.0.0:80", "mysite.wsgi:app"]





