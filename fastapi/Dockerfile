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
