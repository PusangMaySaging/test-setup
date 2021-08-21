FROM python:3.8.10 

COPY . /srv/api

WORKDIR /srv/api

EXPOSE 1000

RUN pip3 install -r requirements.txt

# CMD ["python3","-u","server.py"]
CMD ["gunicorn","-w 5" ,"server:create_app()", "-b 0.0.0.0:1000"]