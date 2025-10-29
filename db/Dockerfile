# Use a small official PostgreSQL image
FROM postgres:15-alpine

# Copy initialization SQL script
COPY init.sql /docker-entrypoint-initdb.d/

# Expose default Postgres port
EXPOSE 5432

# Environment variables (for testing)
ENV POSTGRES_USER=testuser
ENV POSTGRES_PASSWORD=testpass
ENV POSTGRES_DB=testdb

# Optional: healthcheck to test readiness
HEALTHCHECK CMD pg_isready -U $POSTGRES_USER || exit 1
