FROM python:3.8-slim-buster 

RUN mkdir -p /app

COPY . /app

RUN pip install -r /app/requirements.txt



#EXPOSE 5000

CMD ["python3", "/app/app.py"]
