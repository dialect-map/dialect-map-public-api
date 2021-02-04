# syntax=docker/dockerfile:1.0.0-experimental

# Base image
FROM python:3.7-slim

# Set working directory and copy files
WORKDIR /app
COPY . /app


# Install binary dependencies
RUN apt-get update && apt-get install -y git

# Download public key for github.com
# Necessary to allow installation of private packages
RUN mkdir -p -m 0600 ~/.ssh && \
    ssh-keyscan github.com >> ~/.ssh/known_hosts


# Install Python dependencies
RUN --mount=type=ssh \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --requirement requirements.txt


# Tell Docker about the port the application will expose
EXPOSE 8080

# Start server
ENTRYPOINT ["./scripts/start_gunicorn.sh"]
