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
        docker build -t my-fastapi2 .
        docker tag my-fastapi2:latest my-fastapi2:staging     
        ```
4. Run the docker image by using following command : `docker-compose up -d`
5. You can check the fastapi at this URL : http://localhost:8081/hello
6. To stop the docker services give following command : `docker-compose down`

## Helpful Docker commands

```bash
docker exec -it my-running-app sh (to go inside the docker) 
docker rm <container-id>
docker rmi <image-id>
docker-compose up -d 
docker-compose down
```

**Reference** : 
1. https://www.docker.com/blog/how-to-use-the-apache-httpd-docker-official-image/
2. https://github.com/docker/awesome-compose
