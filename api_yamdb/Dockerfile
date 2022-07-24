#FROM python:3.7-slim
#WORKDIR /app
#COPY ./ ./
#RUN pip3 install -r ./api_yamdb/requirements.txt --no-cache-dir
#RUN python3 ./api_yamdb/manage.py collectstatic --no-input
#CMD ["gunicorn", "api_yamdb.api_yamdb.wsgi:application", "--bind", "0:8000"]

FROM python:3.7-slim
WORKDIR /app/api_yamdb
COPY ./ ../
RUN pwd
RUN ls -R
#RUN pip3 install -r ./api_yamdb/requirements.txt --no-cache-dir
#RUN python3 ./api_yamdb/manage.py collectstatic --no-input
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]
