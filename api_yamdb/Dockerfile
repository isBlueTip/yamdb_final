FROM python:3.7-slim

WORKDIR /app/yamdb_final

COPY api_yamdb/requirements.txt ./api_yamdb

RUN pip3 install -r api_yamdb/requirements.txt --no-cache-dir

COPY ./ ../

RUN python3 ../manage.py collectstatic --no-input

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
