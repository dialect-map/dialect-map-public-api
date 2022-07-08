# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app


# Install binary dependencies
RUN apt-get update && \
    apt-get install -y git

# Download public key for github.com (needed for private packages)
RUN mkdir -p -m 0600 ~/.ssh && \
    ssh-keyscan github.com >> ~/.ssh/known_hosts


# Copy Python dependency files
COPY ./reqs /app/reqs

# Install Python dependencies
RUN --mount=type=ssh \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --requirement reqs/requirements-prod.txt && \
    pip install --no-cache-dir --requirement reqs/requirements-spec.txt

# Copy all files
COPY . /app


# State application exposed port
EXPOSE 8080

# Start server
ENTRYPOINT ["./scripts/start_gunicorn.sh"]
