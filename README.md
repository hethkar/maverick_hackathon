# Maverick Hackathon

## Steps to create run frontend project

Reference : https://www.docker.com/blog/how-to-use-the-apache-httpd-docker-official-image/

1. Put your static html files in frontend/public-html folder
2. Build your docker image usiing following command : `cd frontend; docker build -t my-apache2 .`
3. Run the docker image using following command : `docker run -d --name my-running-app -p 8080:80 my-apache2`
4. You can check the frontend at this URL : http://localhost:8080/hello.html
5. To stop the docker give following command : `docker stop my-running-app`


## Helpful commands

```bash
docker rm <container-id>
docker rmi <image-id>
```