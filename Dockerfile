FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBUG=0


WORKDIR /app


RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc python3-dev musl-dev \
    && pip install pipenv \
    && apt-get remove -y gcc python3-dev musl-dev \
    && rm -rf /var/lib/apt/lists/*



# Install dependencies
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /app

EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --no-input

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
