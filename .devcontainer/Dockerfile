FROM python:3.11
ENV PYTHONUNBUFFERED 1
ARG DOCKER_HOME="/opt/motiong"
ARG DOCKER_CODE="/opt/motiong/code"
ARG DOCKER_GROUP="motiong"
ARG DOCKER_USER="motiong"
ARG DOCKER_UID=5000
WORKDIR ${DOCKER_CODE}

RUN groupadd -g ${DOCKER_UID} ${DOCKER_GROUP} \
    && useradd -r -u ${DOCKER_UID} -g ${DOCKER_GROUP} -d ${DOCKER_HOME} ${DOCKER_USER} \
    && chown -R ${DOCKER_USER}:${DOCKER_GROUP} ${DOCKER_HOME}

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y git && \
    apt-get install -y openssh-client && \
    pip install --upgrade pip && \
    pip install poetry==1.8.3 && \
    poetry config virtualenvs.create false

RUN mkdir ${DOCKER_HOME}/.ssh && \
    chown -R ${DOCKER_USER} ${DOCKER_HOME}/.ssh && \
    ssh-keyscan github.com >> ${DOCKER_HOME}/.ssh/known_hosts

ENV PATH "$PATH:/opt/motiong/.local/bin"
ENV PYTHONPATH=.
USER ${DOCKER_USER}
ENTRYPOINT [ "/bin/sh", "-c" ]

