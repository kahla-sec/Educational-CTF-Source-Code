FROM ubuntu:19.10
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y npm nodejs mysql-server
WORKDIR /data/
COPY index.js .
COPY static /data/static
COPY templates /data/templates
COPY package.json .
RUN npm install
CMD node index.js
