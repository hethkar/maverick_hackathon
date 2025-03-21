# Maverick Hackathon

## Steps to create run frontend project

1. Put your static html files in frontend/public-html folder
2. Build your docker image using following command : 
        ```bash
        cd frontend
        docker build -t my-apache2 .
        docker tag my-apache2:latest my-apache2:staging
        ```
3. Run the docker image using following command : `docker run -d --name my-running-app -p 8080:80 my-apache2:staging`
4. You can check the frontend at this URL : http://localhost:8080/hello.html
5. To stop the docker give following command : `docker stop my-running-app`

## Steps to create run fastapi project

1. Define your API's in fastapi\app\main.py file
2. Define your package dependency in fastapi\requirements.txt
3. Build your docker image using following command : 
        ```bash
        cd fastapi
        pytest app
        docker build -t my-fastapi2 .
        docker tag my-fastapi2:latest my-fastapi2:staging     
        ```
4. Run the docker image by using following command : `docker-compose up -d`
5. You can check the fastapi at this URL : http://localhost:8081/hello
6. To stop the docker services give following command : `docker-compose down`

**Note** : To run fastapi in local run following command
```bash
cd fastapi\app
uvicorn main:app --host 0.0.0.0 --port 8081
```

Check opensearch-knn
```bash
http://localhost:9200/_cat/plugins?v
```

## Steps to create run indexing project

1. Build your docker image using following command :
   ```bash
   cd indexing
   docker build -t my-knn-index2 .
   docker tag my-knn-index2:latest my-knn-index2:staging
   ```
2. Run the docker image by using following command : `docker-compose up -d`
3. docker logs maverick_hackathon-knn-index-1 -f

## Search customer working command

```bash
curl --request POST \
  --url 'http://localhost:8081/search_customer?query=durga' \
  --header 'content-type: application/json' \
  --data '{}'
```

```bash
curl -X 'POST' \
  'http://localhost:8081/all-MiniLM-L6-v2/eval' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "fname": "sandep",
  "address": "stevnage"
}'
```

## Kafka Consumer and producer commands

```bash
cd indexing\src
python kafka_producer.py
python kafka_consumer.py
```

## Helpful Docker commands

```bash
docker exec -it my-running-app sh (to go inside the docker) 
docker rm <container-id>
docker rmi <image-id>
docker-compose up -d 
docker-compose down
docker logs maverick_hackathon-backend-1 -f (to check backend logs)
```

**Reference** : 
1. https://www.docker.com/blog/how-to-use-the-apache-httpd-docker-official-image/
2. https://github.com/docker/awesome-compose
3. https://www.baeldung.com/ops/kafka-docker-setup
4. https://www.youtube.com/watch?v=LA-hZDnn5Hc
5. https://colab.research.google.com/drive/1mUtld_eDrqQG3H8w8gkS3yaUSG6sbOLx?usp=sharing
6. https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/pipelines
7. https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/pipelines#transformers.TextGenerationPipeline
8. https://huggingface.co/meta-llama/Llama-3-8B
9. https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
10. https://realpython.com/python-logging/
11. https://geshan.com.np/blog/2023/06/elasticsearch-docker/
12. https://www.cloudbees.com/blog/how-to-install-and-run-jenkins-with-docker-compose
13. https://tutorials.releaseworksacademy.com/learn/building-your-first-docker-image-with-jenkins-2-guide-for-developers
14. https://fastapi.tiangolo.com/tutorial/testing/#run-it
15. https://docs.confluent.io/kafka-clients/python/current/overview.html