# Project Introduction

This is project introduction

# Setup

### Setting up Postgres

This is the most tricky part when setting up the application. You will need to make sure that `postgresql` is installed on your system. Here is how you can install it on Ubuntu:

```bash
# install postgres and required libs
sudo apt install postgresql postgresql-contrib libpq-dev
# create a new user formester as specified in database.yml
sudo -u postgres createuser -s snippetclass
# get into the psql prompt to do some work
sudo -u postgres psql
# setup password for the user formester
\password snippetclass
# when prompted enter `snippetclass` as password
# then quit
\q
```

```
sudo -u postgres psql
postgres=# create database mydb;
postgres=# create user myuser with encrypted password 'mypass';
postgres=# grant all privileges on database mydb to myuser;
```
