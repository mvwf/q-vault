FROM python:3.12

WORKDIR /app
RUN pip install --no-cache-dir poetry

# same single dependency set
COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --only main --no-root

# copy ONLY the frontend source
COPY frontend /app

CMD ["streamlit", "run", "app.py", "--server.port=8501"]
