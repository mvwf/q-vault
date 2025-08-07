FROM python:3.12

# psycopg2 needs libpq
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app/backend/

# install Poetry
RUN pip install --no-cache-dir poetry

# copy dependency files
COPY pyproject.toml poetry.lock* /app/backend/

# copy alembic .ini
COPY alembic.ini /app/backend/

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root

COPY backend /app/backend/

# run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
