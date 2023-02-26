# Use a Python 3.9 base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy poetry files
COPY pyproject.toml poetry.lock server.crt server.key /app/

# Install poetry
RUN apt-get update
RUN apt-get install curl -y
RUN #curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN curl -sSL https://install.python-poetry.org | python3 -
#ENV PATH="/root/.poetry/bin:${PATH}"
ENV PATH="/root/.local/bin:${PATH}"
RUN poetry install --no-root --no-interaction --no-ansi

# Copy server and client code
COPY server.py client.py /app/

# Expose server port
EXPOSE 8888

# Start server by default
CMD ["poetry", "run", "python", "server.py"]
