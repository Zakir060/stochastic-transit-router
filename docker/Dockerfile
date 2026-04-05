# =============================================================================
# Stochastic Transit Router - Production Dockerfile
# Containerized Application Deployment
#
# This Dockerfile builds a production-optimized container for the Stochastic
# Transit Router API service. Uses multi-stage builds for minimal image size,
# comprehensive health checks, security best practices, and performance tuning.
#
# Build: docker build -t stochastic-transit-router:latest .
# Run:   docker run -p 8000:8000 stochastic-transit-router:latest
#
# Documentation: https://docs.docker.com/engine/reference/builder/
# Best Practices: https://docs.docker.com/develop/dev-best-practices/
# =============================================================================

# STAGE 1: BUILDER - Compile dependencies and prepare environment
# =============================================================================
FROM python:3.12-slim as builder

LABEL maintainer="Zakir Bayramov <zakirbayramov942@gmail.com>, Gustav Olaf Yunus Laitinen-Lundström Fredriksson-Imanov <olaf.laitinen@uni.lu>"
LABEL description="Stochastic Transit Router - Production API Container"
LABEL version="0.1.0"

# ============================================================================
# ENVIRONMENT SETUP - Performance and Behavior Tuning
# ============================================================================

# Python runtime optimizations
ENV PYTHONDONTWRITEBYTECODE=1          # Prevents .pyc file generation (saves space, improves startup)
ENV PYTHONUNBUFFERED=1                 # Unbuffered output for real-time logging in containers
ENV PYTHONHASHSEED=random              # Security: randomize hash functions to prevent attacks
ENV PIP_NO_CACHE_DIR=1                 # Reduce pip cache in container image (saves 100+ MB)
ENV PIP_DISABLE_PIP_VERSION_CHECK=1    # Skip pip version checks (faster installs)

# Application environment
ENV APP_ENV=production                 # Mark environment for conditional behavior
ENV LOG_LEVEL=INFO                     # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# ============================================================================
# SYSTEM DEPENDENCIES - Install required OS packages
# ============================================================================

WORKDIR /builder

# Update package manager and install minimal OS dependencies
# Using python:3.12-slim base: ~150MB (vs python:3.12: ~1GB)
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Build dependencies for Python packages with C extensions
    build-essential \
    gcc \
    g++ \
    git \
    # Clean up package manager cache to reduce layer size
    && rm -rf /var/lib/apt/lists/*

# ============================================================================
# PYTHON DEPENDENCIES - Install application packages
# ============================================================================

# Copy dependency specifications only (for better Docker layer caching)
COPY pyproject.toml setup.py* setup.cfg* README.md ./

# Upgrade pip, setuptools, wheel for better dependency resolution
RUN pip install --no-cache-dir --upgrade \
    pip>=24.0 \
    setuptools>=77.0.0 \
    wheel>=0.43.0

# Install project with all dependencies
# Using editable install (-e) to respect setup.py/pyproject.toml configuration
RUN pip install --no-cache-dir -e . && \
    # Verify installation succeeded
    python -c "import stochastic_transit_router; print(f'Package installed successfully')"

# ============================================================================
# STAGE 2: RUNTIME - Minimal production image
# =============================================================================
FROM python:3.12-slim as runtime

LABEL maintainer="Zakir Bayramov <zakirbayramov942@gmail.com>, Gustav Olaf Yunus Laitinen-Lundström Fredriksson-Imanov <olaf.laitinen@uni.lu>"
LABEL description="Stochastic Transit Router - Production API Container"
LABEL version="0.1.0"

# ============================================================================
# ENVIRONMENT - Replicate builder environment
# ============================================================================

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=1
ENV APP_ENV=production
ENV LOG_LEVEL=INFO

# ============================================================================
# SYSTEM SETUP - Security and operational configuration
# ============================================================================

# Create non-root user for security (principle of least privilege)
# Running as root is a security risk; containers should run as unprivileged users
RUN useradd -m -u 1000 -s /bin/bash appuser

WORKDIR /app

# Install runtime dependencies only (no build tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    # HTTP client utilities for health checks and debugging
    curl \
    # Clean up
    && rm -rf /var/lib/apt/lists/*

# ============================================================================
# APPLICATION FILES - Copy from builder stage
# ============================================================================

# Copy installed Python packages from builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application source code and configuration
COPY --chown=appuser:appuser src ./src
COPY --chown=appuser:appuser pyproject.toml README.md LICENSE SECURITY.md ./
COPY --chown=appuser:appuser docker/entrypoint.sh ./

# Make entrypoint executable
RUN chmod +x ./entrypoint.sh

# ============================================================================
# PORT AND SERVICE EXPOSURE
# ============================================================================

# Expose the application port (documentation only, doesn't actually open port)
# Real port binding happens with "docker run -p 8000:8000"
EXPOSE 8000

# ============================================================================
# HEALTH CHECK - Kubernetes and Docker Compose readiness/liveness probes
# ============================================================================

# Check if the API is responding to HTTP requests
# - Interval: 30 seconds between checks
# - Timeout: 10 seconds to wait for response
# - Retries: 3 failed checks before marking unhealthy
# - StartPeriod: 60 seconds before first health check (allow startup time)
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# ============================================================================
# PERMISSIONS AND SECURITY
# ============================================================================

# Switch to non-root user for execution (security best practice)
USER appuser

# ============================================================================
# ENTRYPOINT - Application startup command
# ============================================================================

# Use entrypoint script for graceful startup and process management
ENTRYPOINT ["./entrypoint.sh"]

# Default command: Run Uvicorn ASGI server for FastAPI application
# Can be overridden: docker run ... /bin/bash (for debugging)
CMD ["uvicorn", "src.stochastic_transit_router.api.app:app", \
     "--host", "0.0.0.0", \
     "--port", "8000", \
     "--workers", "4", \
     "--log-level", "info"]

# =============================================================================
# PRODUCTION NOTES
# =============================================================================
#
# Image Size Optimization:
# - Uses python:3.12-slim (150MB vs 1GB for full image)
# - Multi-stage build: doesn't include build tools in final image
# - Layer caching: dependencies copied separately for better cache hits
# - PIP no-cache: skips downloading cache archive
#
# Security Best Practices:
# - Non-root user (appuser:1000): restricts container privileges
# - Minimal OS packages: only runtime requirements included
# - Read-only filesystem: consider "docker run --read-only" for production
# - Network isolation: should run behind reverse proxy/load balancer
#
# Performance Tuning:
# - PYTHONUNBUFFERED=1: real-time logging (important for monitoring)
# - Multiple Uvicorn workers: leverage multi-core CPU (4 workers default)
# - Connection pooling: configured in application code
#
# Debugging:
# docker run -it --entrypoint /bin/bash stochastic-transit-router:latest
# docker exec -it <container-id> /bin/bash
# docker logs --follow <container-id>
#
# Example Production Deployment:
# docker run -d \
#   --name stochastic-router \
#   --restart always \
#   -p 8000:8000 \
#   -e LOG_LEVEL=WARNING \
#   -e APP_ENV=production \
#   --cpus 2 \
#   --memory 2g \
#   stochastic-transit-router:latest
#
# =============================================================================
