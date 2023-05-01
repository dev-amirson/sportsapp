# Sports Tracker App

This is a repository for a web application developed with Django for “Teams and Players” App.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Features](#features)
3. [Getting Started:](#getting-started)
   - [Docker Setup (recommended)](#docker-setup-recommended)
   - [Local Setup](#local-setup-alternative-to-docker)

## Project Structure

    ..
    ├── main                           # Starter main app
    ├── sportsapp                      # Django project configurations
    ├── static                         # Static assets
    ├── templates                      # Template directory
    ├── README.md
    └── ...

## Features

1. **Local Authentication** using email and password
2. [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
3. Docker Development


# Getting Started:

Following are instructions on setting up your development environment.

The recommended way for running the project locally and for development is using Docker.

It's possible to also run the project without Docker.

## Docker Setup (Recommended)

This project is set up to run using [Docker Compose](https://docs.docker.com/compose/) by default. It is the recommended way. You can also use existing Docker Compose files as basis for custom deployment, e.g. [Docker Swarm](https://docs.docker.com/engine/swarm/), [kubernetes](https://kubernetes.io/), etc.

1. Install Docker:
   - Linux - [get.docker.com](https://get.docker.com/)
   - Windows or MacOS - [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Clone this repo and `cd sportsapp`
3. Make sure `Pipfile.lock` exists. If it doesn't, generate it with:
   ```sh
   $ docker run -it --rm -v "$PWD":/django -w /django python:3.10 pip3 install --no-cache-dir -q pipenv && pipenv lock
   ```
4. Use `.env.example` to create `.env`:
   ```sh
   $ cp .env.example .env
   ```
5. Update `.env` and `docker-compose.yml` replacing all `<placeholders>`
   1. Use `python -c 'from secrets import token_urlsafe; print("SECRET_KEY=" + token_urlsafe(50))'` to generate the random `SECRET_KEY`
6. Start up the containers:

   ```sh
   $ docker-compose up
   ```

   This will build the necessary containers and start them, including the web server on the host and port you specified in `.env`.

   Current (project) directory will be mapped with the container meaning any edits you make will be picked up by the container.


7. Create a superuser if required:
   ```sh
   $ docker-compose exec web python3 manage.py createsuperuser
   ```
   You will find an activation link in the server log output.

## Local Setup (Alternative to Docker)

1. [Python](https://www.python.org/downloads/release/python-365/)

### Installation

1. Install [pipenv](https://pypi.org/project/pipenv/)
2. Clone this repo and `cd sportsapp`
3. Run `pip install --user --upgrade pipenv` to get the latest pipenv version.
4. Run `pipenv --python 3.10`
5. Run `pipenv install`
6. Run `cp .env.example .env`
7. Update .env file

### Getting Started

1. Run `pipenv shell`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Run `python manage.py runserver`
