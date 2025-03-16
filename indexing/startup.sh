#! /bin/bash

date
echo "current location"
pwd

elasticServerHost=$ELASTIC_SERVER_HOST
elasticServerPort=$ELASTIC_SERVER_PORT

if [[ -z "$elasticServerHost" ]]; then
   elasticServerHost="localhost"
fi

if [[ -z "$elasticServerPort" ]]; then
   elasticServerPort="9200"
fi

echo $elasticServerHost
echo $elasticServerPort

echo "waiting for open search to start"
date
while ! nc -z $elasticServerHost $elasticServerPort; do sleep 1; done
date
echo "Open search started"

echo "Creating Index"
curl -X PUT -H "Content-Type: application/json" -d @knnIndexPayload.json http://{$elasticServerHost}:{$elasticServerPort}/consumer_knn_index

echo "Starting the indexing"
python ./src/vectorizerhfcustomer.py
echo "Indexing completed"

tail -f /dev/null
