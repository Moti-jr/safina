# ── Stage 1: Builder ─────────────────────────────────────
# We use a temporary container just to install packages
# This keeps the final image small
FROM python:3.12-slim AS builder

# Set working directory inside the container
WORKDIR /app

# Install system dependencies needed to compile Python packages
# gcc and libpq-dev are needed for psycopg2 (PostgreSQL driver)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first — Docker caches this layer
# If requirements.txt doesn't change, Docker skips reinstalling
COPY requirements.txt .

# Install all Python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ── Stage 2: Runtime ─────────────────────────────────────
# Start fresh from a clean slim image
# Copy only what we need from the builder stage
FROM python:3.12-slim

WORKDIR /app

# Install only runtime system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    netcat-openbsd \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user for security
# Never run your app as root inside a container
RUN useradd -m -u 1000 appuser

# Copy installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages \
                    /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# Copy project code — owned by appuser
COPY --chown=appuser:appuser . .

# Create folders for static and media files
RUN mkdir -p /app/staticfiles /app/media && \
    chown -R appuser:appuser /app/staticfiles /app/media

# Switch to non-root user
USER appuser

# Tell Docker this container listens on port 8000
EXPOSE 8000

# Run the entrypoint script when container starts
ENTRYPOINT ["./docker/entrypoint.sh"]
