FROM python:3.11-alpine
COPY . /code 
ENV PYTHONDOTWRITEBYTECODE 1 
ENV PYTHONUNPUFFERED 1 
WORKDIR /code 
RUN pip install --upgrade pip && pip install -r requirements.txt 
RUN python manage.py migrate 
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
EXPOSE 8000