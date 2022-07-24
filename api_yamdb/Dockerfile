FROM python:3.7-slim
WORKDIR /app
COPY ./ ./
RUN pip3 install -r ./api_yamdb/requirements.txt --no-cache-dir
RUN python3 ./api_yamdb/manage.py collectstatic --no-input
CMD python3 ./api_yamdb/manage.py runserver
