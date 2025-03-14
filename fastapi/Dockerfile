# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder
# FROM python:3.9.21-alpine3.20 AS builder
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# COPY requirements_2.txt ./
# RUN --mount=type=cache,target=/root/.cache/pip \
#     pip install -r requirements_2.txt

COPY ./app /app

FROM builder AS dev-envs

RUN apt-get update
RUN apt-get -y install vim

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
EXPOSE 8000

# RUN <<EOF
# useradd -s /bin/bash -m vscode
# groupadd docker
# usermod -aG docker vscode
# EOF
# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /