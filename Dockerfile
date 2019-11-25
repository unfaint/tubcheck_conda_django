FROM pytorch/pytorch:latest

WORKDIR /app

RUN conda install django
RUN conda install gunicorn

RUN conda install -c conda-forge djangorestframework

COPY . /app

EXPOSE 8000