FROM python:3.7-slim
WORKDIR /app/api_yamdb
COPY ./ ../
RUN pip3 install -r ./requirements.txt --no-cache-dir
RUN python3 ./manage.py collectstatic --no-input
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]
