FROM python:3.7-slim

WORKDIR /app/yamdb_final
COPY ./ ./
#COPY api_yamdb/requirements.txt /api_yamdb

#RUN pip3 install -r ./api_yamdb/requirements.txt --no-cache-dir
RUN pip3 install -r ./api_yamdb/requirements.txt --no-cache-dir

#COPY ./ ../

#RUN python3 ../manage.py collectstatic --no-input
RUN python3 ./api_yamdb/manage.py collectstatic --no-input

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
