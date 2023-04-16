FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt ./


RUN pip install -r requirements.txt

COPY mysite ./mysite

COPY guestbook ./guestbook

COPY render ./render

RUN touch db.sqlite3

RUN python manage.py migrate

EXPOSE 80

CMD ["gunicorn"  , "-b", "0.0.0.0:80", "mysite.wsgi:application"]





