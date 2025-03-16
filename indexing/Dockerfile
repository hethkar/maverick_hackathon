FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY ./startup.sh /app/startup.sh
COPY ./knnIndexPayload.json /app/knnIndexPayload.json
COPY ./data /app/data
COPY ./src /app/src

RUN chmod a+x /app/startup.sh

FROM builder AS dev-envs

RUN apt-get update
RUN apt-get -y install vim
RUN apt-get -y install curl
RUN apt-get -y install iputils-ping
RUN apt-get install netcat-traditional

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# EXPOSE 8000

CMD ["/bin/bash","-c","sleep 2; /app/startup.sh"]