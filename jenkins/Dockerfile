FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update
RUN apt-get install -y ca-certificates curl gnupg git
RUN apt-get install -y --no-install-recommends docker.io
RUN mkdir -p /usr/lib/docker/cli-plugins && \
    curl -SL https://github.com -o /usr/lib/docker/cli-plugins/docker-compose && \
    chmod +x /usr/lib/docker/cli-plugins/docker-compose
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER jenkins