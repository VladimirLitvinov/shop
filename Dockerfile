FROM python:3.12-slim

COPY shop/requirements.txt requirements.txt
COPY diploma-frontend diploma-frontend/
COPY shop shop/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR diploma-frontend/


RUN python setup.py sdist
RUN pip install dist/diploma-frontend-0.6.tar.gz


WORKDIR /
WORKDIR shop/

RUN python manage.py migrate && python manage.py loaddata shop-fixture.json

EXPOSE 8000


CMD ["gunicorn", "app.wsgi:application", "--workers", "3", "--bind", "0.0.0.0:8000"]
