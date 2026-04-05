#!/usr/bin/env bash
# =============================================================================
# Stochastic Transit Router - Container Entrypoint Script
# Process Management, Health Checks, and Graceful Shutdown
#
# This script serves as the main entry point for the Docker container.
# It handles:
# - Process initialization and configuration
# - Graceful shutdown (SIGTERM handling)
# - Health check endpoints
# - Environment validation
# - Logging and monitoring setup
#
# Usage: docker run stochastic-transit-router:latest [COMMAND] [ARGS...]
# Default: Starts Uvicorn ASGI server for FastAPI application
# =============================================================================

set -euo pipefail

# ============================================================================
# GLOBAL VARIABLES AND CONFIGURATION
# ============================================================================

# Script metadata
readonly SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly APP_DIR="${APP_DIR:-/app}"

# Logging configuration
readonly LOG_PREFIX="[$(date +'%Y-%m-%d %H:%M:%S')]"

# Application configuration (from environment variables)
readonly APP_ENV="${APP_ENV:-production}"
readonly LOG_LEVEL="${LOG_LEVEL:-INFO}"
readonly WORKERS="${WORKERS:-4}"
readonly HOST="${HOST:-0.0.0.0}"
readonly PORT="${PORT:-8000}"

# Process management
PID_FILE="/var/run/stochastic-router.pid"
GRACEFUL_SHUTDOWN_TIMEOUT=30

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

#
# log_msg: Print timestamped log message to stderr
#
log_msg() {
    local level="$1"
    shift
    echo "${LOG_PREFIX} [${level}] $*" >&2
}

#
# log_info: Print info message
#
log_info() {
    log_msg "INFO" "$@"
}

#
# log_warn: Print warning message
#
log_warn() {
    log_msg "WARN" "$@"
}

#
# log_error: Print error message
#
log_error() {
    log_msg "ERROR" "$@"
}

#
# log_debug: Print debug message (only if DEBUG=1)
#
log_debug() {
    if [ "${DEBUG:-0}" = "1" ]; then
        log_msg "DEBUG" "$@"
    fi
}

#
# cleanup: Graceful shutdown hook - handles SIGTERM signal
#
cleanup() {
    local exit_code=$?
    local signal="${1:-UNKNOWN}"

    log_info "Received signal: ${signal}, initiating graceful shutdown"

    # Send SIGTERM to application process
    if [ -f "${PID_FILE}" ]; then
        local pid=$(cat "${PID_FILE}")
        if kill -0 "${pid}" 2>/dev/null; then
            log_info "Terminating process ${pid}..."
            kill -TERM "${pid}" 2>/dev/null || true

            # Wait for graceful shutdown (up to GRACEFUL_SHUTDOWN_TIMEOUT seconds)
            local elapsed=0
            while kill -0 "${pid}" 2>/dev/null && [ ${elapsed} -lt ${GRACEFUL_SHUTDOWN_TIMEOUT} ]; do
                sleep 1
                elapsed=$((elapsed + 1))
            done

            # Force kill if still running
            if kill -0 "${pid}" 2>/dev/null; then
                log_warn "Process did not shutdown gracefully, forcing kill of ${pid}"
                kill -KILL "${pid}" 2>/dev/null || true
            else
                log_info "Process terminated gracefully"
            fi
        fi
    fi

    # Clean up PID file
    [ -f "${PID_FILE}" ] && rm -f "${PID_FILE}"

    exit ${exit_code}
}

#
# validate_environment: Verify required environment variables and files
#
validate_environment() {
    log_info "Validating environment configuration"

    # Check if Python is available
    if ! command -v python &>/dev/null; then
        log_error "Python interpreter not found in PATH"
        return 1
    fi

    # Check if application code exists
    if [ ! -d "${APP_DIR}/src" ]; then
        log_error "Application source code not found at ${APP_DIR}/src"
        return 1
    fi

    # Verify application can be imported
    if ! python -c "import stochastic_transit_router" 2>/dev/null; then
        log_warn "Could not import stochastic_transit_router (may be normal during initial setup)"
    fi

    log_info "Environment validation passed"
    return 0
}

#
# setup_traps: Configure signal handlers for graceful shutdown
#
setup_traps() {
    log_debug "Setting up signal handlers"

    # Handle SIGTERM (docker stop)
    trap "cleanup SIGTERM" SIGTERM

    # Handle SIGINT (docker kill -s SIGINT)
    trap "cleanup SIGINT" SIGINT

    # Handle EXIT
    trap "cleanup EXIT" EXIT
}

#
# run_api_server: Start Uvicorn ASGI server
#
run_api_server() {
    log_info "Starting Stochastic Transit Router API server"
    log_info "Configuration: APP_ENV=${APP_ENV}, LOG_LEVEL=${LOG_LEVEL}, WORKERS=${WORKERS}"
    log_info "Server: ${HOST}:${PORT}"

    # Save process ID for signal handling
    echo $$ > "${PID_FILE}"

    # Start Uvicorn with configuration
    exec uvicorn \
        "src.stochastic_transit_router.api.app:app" \
        --host "${HOST}" \
        --port "${PORT}" \
        --workers "${WORKERS}" \
        --log-level "$(echo "${LOG_LEVEL}" | tr '[:upper:]' '[:lower:]')" \
        --access-log \
        --use-colors \
        --forwarded-allow-ips="*" \
        --proxy-headers
}

#
# run_cli_command: Run CLI command from stochastic_transit_router
#
run_cli_command() {
    log_info "Running CLI command: $*"

    # Execute the CLI with provided arguments
    exec python -m stochastic_transit_router "$@"
}

#
# run_command: Execute arbitrary shell command
#
run_command() {
    log_info "Executing command: $*"
    exec "$@"
}

#
# print_banner: Print startup banner with system information
#
print_banner() {
    cat <<EOF
╔══════════════════════════════════════════════════════════════════════════╗
║                 Stochastic Transit Router - v0.1.0                       ║
║              Route Intelligence Platform - Production                    ║
╚══════════════════════════════════════════════════════════════════════════╝

Environment Configuration:
  - Environment: ${APP_ENV}
  - Log Level: ${LOG_LEVEL}
  - Server Host: ${HOST}
  - Server Port: ${PORT}
  - Workers: ${WORKERS}
  - Python Version: $(python --version)

Application Details:
  - Working Directory: ${APP_DIR}
  - Process ID: ${BASHPID}
  - Container Hostname: $(hostname)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF
}

# ============================================================================
# MAIN ENTRYPOINT LOGIC
# ============================================================================

#
# main: Entry point function
#
main() {
    log_info "Container starting: ${SCRIPT_NAME}"

    # Print startup banner
    print_banner

    # Setup signal handlers for graceful shutdown
    setup_traps

    # Validate environment configuration
    if ! validate_environment; then
        log_error "Environment validation failed"
        return 1
    fi

    # Route based on first argument
    case "${1:-api}" in
        # Default: Start API server
        api)
            log_info "Mode: API Server"
            run_api_server
            ;;

        # CLI: Run CLI command
        cli)
            shift
            log_info "Mode: CLI"
            run_cli_command "$@"
            ;;

        # Health: Return HTTP health status
        health)
            log_info "Mode: Health Check"
            curl -sf http://localhost:${PORT}/health || exit 1
            ;;

        # Debug: Start bash shell
        debug|bash|sh)
            log_info "Mode: Interactive Shell (Debug)"
            exec /bin/bash
            ;;

        # Custom command: Execute arbitrary command
        *)
            log_info "Mode: Custom Command"
            run_command "$@"
            ;;
    esac
}

# Execute main function
main "$@"
