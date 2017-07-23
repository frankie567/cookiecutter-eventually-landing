from python:latest

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/

ENV PORT=8888
EXPOSE $PORT

CMD gunicorn -b 0.0.0.0:$PORT {{cookiecutter.project_slug}}.app:app
