FROM python:3.9
RUN mkdir -p /code/app
WORKDIR /code/app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000:5000
COPY /app /code/app/
CMD [ "python", "./src/server/server.py" ]