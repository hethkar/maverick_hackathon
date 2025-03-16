#! /bin/bash

docker-compose down

cd frontend
docker build -t my-apache2 .
docker tag my-apache2:latest my-apache2:staging

cd ..

cd fastapi
pytest app
docker build -t my-fastapi2 .
docker tag my-fastapi2:latest my-fastapi2:staging    

cd ..

cd indexing
docker build -t my-knn-index2 .
docker tag my-knn-index2:latest my-knn-index2:staging

cd ..

docker-compose up -d
