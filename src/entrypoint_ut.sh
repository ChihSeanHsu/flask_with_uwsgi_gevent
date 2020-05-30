#!/bin/bash
until nc -z dynamodb-local 8000
do
  echo "Waiting for database connection..."
  # wait for 5 seconds before check again
  sleep 5
done

# run migrate
python create_table.py

# run server
if [ $GEVENT = "1" ]; then 
    echo 'Run Gevent'
    /usr/local/bin/uwsgi uwsgi_g.ini
else
    echo 'Run Threading'
    /usr/local/bin/uwsgi uwsgi.ini
fi