
 # make dockerfile for deploy django
FROM python:3.9.15-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# install dependencies

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt


#COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
#RUN chmod +x /usr/src/app/entrypoint.sh
#RUN chmod +x entrypoint.sh
# copy project

COPY . .

#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]