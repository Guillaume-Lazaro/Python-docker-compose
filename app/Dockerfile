# FROM alpine
# WORKDIR /app

# EXPOSE 5000
# RUN apk add --update --no-cache \
#     python3 \
#     py3-pip \
#     vim \
#     && rm -rf /var/cache/apk/*

# COPY . .

# RUN pip3 install -r requirements.txt
# CMD [ "python3", "./app.py" ]

# FROM mysql 
# WORKDIR /app
# ENV MYSQL_DATABASE=mybase \
#     MYSQL_ROOT_PASSWORD=root \
#     MYSQL_ROOT_USER=root \
#     ALLOW_EMPTY_PASSWORD=yes

# ADD ./db/init.sql /docker-entrypoint-bdd.db.d
# EXPOSE 3306

FROM python:3.6
EXPOSE 5000
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app.py /app
CMD python app.py