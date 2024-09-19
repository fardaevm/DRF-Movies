FROM python:3.12.4-slim-bookworm

# set working directory
WORKDIR /drf

# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat-traditional gcc postgresql \
  && apt-get clean

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# add app
COPY . .

ENTRYPOINT ["/entrypoint.sh"]