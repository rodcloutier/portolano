FROM python:3.6-alpine
MAINTAINER "rodcloutier@gmail.com"

WORKDIR  /app

RUN    apk update \
  &&   apk add ca-certificates wget \
  &&   update-ca-certificates \
  &&   wget -nv https://storage.googleapis.com/kubernetes-helm/helm-v2.4.1-linux-amd64.tar.gz -O helm.tar.gz \
  &&   tar -vxzf helm.tar.gz \
  &&   rm helm.tar.gz

ENV PATH $PATH:/app/linux-amd64

COPY requirements/install.pip .
RUN pip install -r install.pip

ENV PORTOLANO_CONFIG_FILE /app/config/default.py

ADD portolano/ portolano/
ADD config/ config/

EXPOSE 5000

ENTRYPOINT ["gunicorn"]
CMD ["--config", "config/gunicorn_config.py", "portolano:connexion_app"]

