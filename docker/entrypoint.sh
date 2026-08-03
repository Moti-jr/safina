#!/bin/sh
set -e

echo "═══════════════════════════════════════"
echo "  Safina Initiative — Starting up"
echo "═══════════════════════════════════════"

# Wait for PostgreSQL to be ready
# nc (netcat) tests if a TCP connection can be made
echo "⏳ Waiting for PostgreSQL at $POSTGRES_HOST:$POSTGRES_PORT..."
while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done
echo "✅ PostgreSQL is ready"

# Run database migrations
# This creates/updates all database tables
echo "⏳ Running migrations..."
python manage.py migrate --noinput
echo "✅ Migrations complete"

# Collect static files into STATIC_ROOT
# WhiteNoise will serve them from there
echo "⏳ Collecting static files..."
python manage.py collectstatic --noinput
echo "✅ Static files collected"

echo "🚀 Starting Gunicorn..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info
