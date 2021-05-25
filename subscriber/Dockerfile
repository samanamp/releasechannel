FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./requirements.txt /requirements.txt
RUN ls && pip install -r /requirements.txt
COPY ./app /app
