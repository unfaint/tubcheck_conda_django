FROM pytorch/pytorch:latest

WORKDIR /app

RUN conda install django
RUN conda install gunicorn
RUN conda install -c conda-forge djangorestframework

COPY . /app

RUN python /app/manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--chdir", "/app", "--bind", ":8000", "tubcheck.wsgi:application"]