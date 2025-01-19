FROM python:3.12

WORKDIR /usr/src/UgostyMainService/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apt-get update \
#    && apt-get -y install libpq-dev gcc \
#    && pip install psycopg2

# install dependencies

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Install production dependencies.


RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt





COPY . .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]