from python:latest

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/

ENV PORT=8888
EXPOSE $PORT

ENV FLASK_APP=/code/{{cookiecutter.project_slug}}/app.py

CMD flask run -h 0.0.0.0 -p $PORT
