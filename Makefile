# =============================================================================
# Stochastic Transit Router - GNU Makefile
# Development Workflow Automation and Build Orchestration
#
# This Makefile provides convenient commands for common development tasks:
# - Installation and environment setup
# - Code quality checks (linting, type checking, formatting)
# - Testing (unit, integration, benchmarks, E2E)
# - Documentation building and validation
# - Cleaning build artifacts and caches
# - Development workflow utilities
#
# Usage: make <target> [OPTION=value]
# Help:  make help
# List:  make list
#
# Documentation: https://www.gnu.org/software/make/manual/
# =============================================================================

# ============================================================================
# MAKEFILE CONFIGURATION
# ============================================================================

# Set shell to bash for better compatibility and features
SHELL := /bin/bash

# Delete target if recipe fails (cleanup partial files)
.DELETE_ON_ERROR:

# Print recipes before executing (show what's happening)
.VERBOSE:

# Disable built-in rules (faster, explicit is better)
MAKEFLAGS += --no-builtin-rules
.SUFFIXES:

# ============================================================================
# GLOBAL VARIABLES AND CONFIGURATION
# ============================================================================

# Python executable (use python3.12 specifically, fallback to python)
PYTHON := python3.12
ifeq ($(shell which python3.12),)
    PYTHON := python3
endif

# Virtual environment path
VENV := .venv

# Project name and version
PROJECT_NAME := stochastic-transit-router
PROJECT_VERSION := $(shell $(PYTHON) -c "import tomllib; print(tomllib.loads(open('pyproject.toml').read())['project']['version'])" 2>/dev/null || echo "unknown")

# Color output for terminal
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[0;33m
BLUE := \033[0;34m
NC := \033[0m  # No Color

# Directories
SRC_DIR := src
TEST_DIR := tests
DOCS_DIR := docs
SCRIPTS_DIR := scripts
BENCHMARKS_DIR := benchmarks

# Python source directories
PYTHON_DIRS := $(SRC_DIR) $(TEST_DIR) $(SCRIPTS_DIR)

# Coverage thresholds
COVERAGE_THRESHOLD := 80

# Number of parallel workers (0 = auto-detect CPU count)
WORKERS := 0

# ============================================================================
# DECLARE PHONY TARGETS (Not filesystem files)
# ============================================================================

.PHONY: help list info \
	install install-dev install-test install-full \
	venv check-venv \
	lint format typecheck \
	test unit integration schema benchmark e2e \
	coverage coverage-html coverage-report \
	clean clean-py clean-test clean-build clean-cache clean-all \
	docs docs-check docs-format \
	dev dev-server dev-api dev-cli \
	ship release version \
	pre-commit-check pre-commit-run \
	export-requirements \
	health performance \
	shell notebook

# ============================================================================
# HELP AND INFORMATION TARGETS
# ============================================================================

# ============================================================================
# TARGET: help - Display comprehensive help message
# ============================================================================
help:
	@echo "$(BLUE)══════════════════════════════════════════════════════════════════════════════$(NC)"
	@echo "$(BLUE)$(PROJECT_NAME) v$(PROJECT_VERSION) - Development Makefile$(NC)"
	@echo "$(BLUE)══════════════════════════════════════════════════════════════════════════════$(NC)"
	@echo
	@echo "$(GREEN)INSTALLATION:$(NC)"
	@echo "  make install           Install project with core and dev dependencies"
	@echo "  make install-dev       Install with development tools only"
	@echo "  make install-test      Install with testing dependencies only"
	@echo "  make install-full      Install with all optional dependencies"
	@echo "  make venv              Create virtual environment"
	@echo
	@echo "$(GREEN)CODE QUALITY:$(NC)"
	@echo "  make lint              Check code with ruff linter"
	@echo "  make format            Auto-format code with ruff"
	@echo "  make typecheck         Type check with mypy (strict mode)"
	@echo
	@echo "$(GREEN)TESTING:$(NC)"
	@echo "  make test              Run all tests (unit + integration)"
	@echo "  make unit              Run unit tests only"
	@echo "  make integration       Run integration tests only"
	@echo "  make schema            Run schema/contract tests"
	@echo "  make benchmark         Run performance benchmarks"
	@echo "  make e2e               Run end-to-end tests"
	@echo
	@echo "$(GREEN)COVERAGE & REPORTS:$(NC)"
	@echo "  make coverage          Run tests with coverage report (terminal)"
	@echo "  make coverage-html     Generate HTML coverage report"
	@echo "  make coverage-report   Show coverage summary"
	@echo
	@echo "$(GREEN)DOCUMENTATION:$(NC)"
	@echo "  make docs              Check markdown documentation format"
	@echo "  make docs-format       Auto-format markdown files"
	@echo
	@echo "$(GREEN)DEVELOPMENT:$(NC)"
	@echo "  make dev               Run development server (API + hot reload)"
	@echo "  make dev-api           Start API server (uvicorn)"
	@echo "  make dev-cli           Interactive CLI shell"
	@echo "  make shell             Python interactive shell with project loaded"
	@echo "  make notebook          Start Jupyter notebook server"
	@echo
	@echo "$(GREEN)HEALTH & PERFORMANCE:$(NC)"
	@echo "  make health            Quick health check (lint + type + unit tests)"
	@echo "  make performance       Profile performance of key functions"
	@echo
	@echo "$(GREEN)GIT & RELEASE:$(NC)"
	@echo "  make pre-commit-check  Verify pre-commit hooks installed"
	@echo "  make pre-commit-run    Run all pre-commit hooks"
	@echo "  make version           Show project version"
	@echo
	@echo "$(GREEN)UTILITIES:$(NC)"
	@echo "  make export-requirements  Export dependencies to requirements.txt"
	@echo "  make clean             Remove Python cache, build artifacts"
	@echo "  make clean-all         Complete cleanup including venv, data, cache"
	@echo "  make list              List all available targets"
	@echo "  make info              Show project information"
	@echo
	@echo "$(YELLOW)EXAMPLES:$(NC)"
	@echo "  make install && make test                    # Setup and test"
	@echo "  make lint format typecheck                   # Complete code check"
	@echo "  make coverage COVERAGE_THRESHOLD=70         # Custom coverage threshold"
	@echo "  WORKERS=4 make test                          # Use 4 parallel workers"
	@echo

# ============================================================================
# TARGET: list - List all available make targets
# ============================================================================
list:
	@echo "$(BLUE)Available make targets:$(NC)"
	@grep -E '^[a-zA-Z_-]+:' Makefile | grep -v '^\.' | sed 's/:.*//g' | column -t | sort
	@echo
	@echo "Run '$(YELLOW)make <target>$(NC)' to execute a target"
	@echo "Run '$(YELLOW)make help$(NC)' for detailed instructions"

# ============================================================================
# TARGET: info - Show project information
# ============================================================================
info:
	@echo "$(BLUE)Project Information:$(NC)"
	@echo "  Name:           $(PROJECT_NAME)"
	@echo "  Version:        $(PROJECT_VERSION)"
	@echo "  Python:         $(PYTHON)"
	@echo "  Python Version: $$($(PYTHON) --version)"
	@echo "  Venv:           $(VENV)"
	@echo "  Status:         $$([ -d $(VENV) ] && echo 'Active' || echo 'Inactive')"
	@echo
	@echo "$(BLUE)Key Directories:$(NC)"
	@echo "  Source:         $(SRC_DIR)/"
	@echo "  Tests:          $(TEST_DIR)/"
	@echo "  Docs:           $(DOCS_DIR)/"
	@echo "  Scripts:        $(SCRIPTS_DIR)/"
	@echo "  Benchmarks:     $(BENCHMARKS_DIR)/"
	@echo
	@echo "$(BLUE)Targets Summary:$(NC)"
	@echo "  Total targets:  $$(grep -E '^[a-zA-Z_-]+:' Makefile | grep -v '^\.' | wc -l)"
	@echo "  Phony targets:  $$(echo '$(MAKEFILE_LIST)' | wc -w)"

# ============================================================================
# INSTALLATION TARGETS
# ============================================================================

# ============================================================================
# TARGET: venv - Create Python virtual environment
# ============================================================================
venv:
	@echo "$(GREEN)Creating virtual environment...$(NC)"
	$(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)✓ Virtual environment created at $(VENV)/$(NC)"
	@echo "$(YELLOW)Activate with: source $(VENV)/bin/activate$(NC)"

# ============================================================================
# TARGET: check-venv - Verify virtual environment is active
# ============================================================================
check-venv:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "$(RED)✗ Virtual environment not active!$(NC)"; \
		echo "$(YELLOW)Activate with: source $(VENV)/bin/activate$(NC)"; \
		exit 1; \
	else \
		echo "$(GREEN)✓ Virtual environment active: $$VIRTUAL_ENV$(NC)"; \
	fi

# ============================================================================
# TARGET: install - Install project with default dependencies
# ============================================================================
install: check-venv
	@echo "$(GREEN)Installing project with core and dev dependencies...$(NC)"
	$(PYTHON) -m pip install --upgrade pip setuptools wheel
	$(PYTHON) -m pip install -e ".[dev,test]"
	@echo "$(GREEN)✓ Installation complete$(NC)"

# ============================================================================
# TARGET: install-dev - Install development dependencies only
# ============================================================================
install-dev: check-venv
	@echo "$(GREEN)Installing development dependencies...$(NC)"
	$(PYTHON) -m pip install --upgrade pip setuptools wheel
	$(PYTHON) -m pip install -e ".[dev]"
	@echo "$(GREEN)✓ Development dependencies installed$(NC)"

# ============================================================================
# TARGET: install-test - Install testing dependencies only
# ============================================================================
install-test: check-venv
	@echo "$(GREEN)Installing testing dependencies...$(NC)"
	$(PYTHON) -m pip install --upgrade pip setuptools wheel
	$(PYTHON) -m pip install -e ".[test]"
	@echo "$(GREEN)✓ Testing dependencies installed$(NC)"

# ============================================================================
# TARGET: install-full - Install all optional dependencies
# ============================================================================
install-full: check-venv
	@echo "$(GREEN)Installing all dependencies (dev, test, benchmarks, notebooks, deployment)...$(NC)"
	$(PYTHON) -m pip install --upgrade pip setuptools wheel
	$(PYTHON) -m pip install -e ".[dev,test,benchmarks,notebooks,deployment]"
	pre-commit install
	@echo "$(GREEN)✓ Full installation complete$(NC)"

# ============================================================================
# CODE QUALITY TARGETS
# ============================================================================

# ============================================================================
# TARGET: lint - Check code with ruff linter (no fixes)
# ============================================================================
lint: check-venv
	@echo "$(GREEN)Checking code with ruff...$(NC)"
	ruff check $(PYTHON_DIRS) --exit-zero
	ruff format --check $(PYTHON_DIRS) --exit-zero
	@echo "$(GREEN)✓ Linting complete$(NC)"

# ============================================================================
# TARGET: format - Auto-format code with ruff
# ============================================================================
format: check-venv
	@echo "$(GREEN)Auto-formatting code with ruff...$(NC)"
	ruff format $(PYTHON_DIRS)
	ruff check --fix $(PYTHON_DIRS)
	@echo "$(GREEN)✓ Formatting complete$(NC)"

# ============================================================================
# TARGET: typecheck - Type check with mypy (strict mode)
# ============================================================================
typecheck: check-venv
	@echo "$(GREEN)Type checking with mypy (strict mode)...$(NC)"
	mypy --config-file .mypy.ini $(SRC_DIR) --show-error-codes --pretty
	@echo "$(GREEN)✓ Type checking complete$(NC)"

# ============================================================================
# TESTING TARGETS
# ============================================================================

# ============================================================================
# TARGET: test - Run all tests (unit + integration)
# ============================================================================
test: check-venv
	@echo "$(GREEN)Running all tests...$(NC)"
	pytest $(TEST_DIR) -v --tb=short -m "not slow" $(if $(WORKERS),--n $(WORKERS),)
	@echo "$(GREEN)✓ Tests complete$(NC)"

# ============================================================================
# TARGET: unit - Run unit tests only
# ============================================================================
unit: check-venv
	@echo "$(GREEN)Running unit tests...$(NC)"
	pytest $(TEST_DIR)/unit -v --tb=short $(if $(WORKERS),--n $(WORKERS),)
	@echo "$(GREEN)✓ Unit tests complete$(NC)"

# ============================================================================
# TARGET: integration - Run integration tests only
# ============================================================================
integration: check-venv
	@echo "$(GREEN)Running integration tests...$(NC)"
	pytest $(TEST_DIR)/integration -v --tb=short
	@echo "$(GREEN)✓ Integration tests complete$(NC)"

# ============================================================================
# TARGET: schema - Run schema/contract tests
# ============================================================================
schema: check-venv
	@echo "$(GREEN)Running schema/contract tests...$(NC)"
	pytest $(TEST_DIR)/schema tests/contracts -v --tb=short
	@echo "$(GREEN)✓ Schema tests complete$(NC)"

# ============================================================================
# TARGET: benchmark - Run performance benchmarks
# ============================================================================
benchmark: check-venv
	@echo "$(GREEN)Running performance benchmarks...$(NC)"
	pytest $(BENCHMARKS_DIR) --benchmark-only --benchmark-json=benchmark_results.json
	@echo "$(GREEN)✓ Benchmarks complete$(NC)"
	@echo "$(YELLOW)Results saved to benchmark_results.json$(NC)"

# ============================================================================
# TARGET: e2e - Run end-to-end tests
# ============================================================================
e2e: check-venv
	@echo "$(GREEN)Running end-to-end tests...$(NC)"
	pytest $(TEST_DIR)/e2e -v --tb=short
	@echo "$(GREEN)✓ E2E tests complete$(NC)"

# ============================================================================
# COVERAGE TARGETS
# ============================================================================

# ============================================================================
# TARGET: coverage - Run tests with coverage report (terminal output)
# ============================================================================
coverage: check-venv
	@echo "$(GREEN)Running tests with coverage analysis (threshold: $(COVERAGE_THRESHOLD)%)...$(NC)"
	pytest $(TEST_DIR) \
		--cov=$(SRC_DIR) \
		--cov-report=term-missing:skip-covered \
		--cov-report=json \
		--cov-fail-under=$(COVERAGE_THRESHOLD) \
		-v --tb=short
	@echo "$(GREEN)✓ Coverage analysis complete$(NC)"

# ============================================================================
# TARGET: coverage-html - Generate HTML coverage report
# ============================================================================
coverage-html: check-venv coverage
	@echo "$(GREEN)Generating HTML coverage report...$(NC)"
	coverage html
	@echo "$(GREEN)✓ HTML report generated: htmlcov/index.html$(NC)"
	@echo "$(YELLOW)Open: open htmlcov/index.html$(NC)"

# ============================================================================
# TARGET: coverage-report - Show coverage summary
# ============================================================================
coverage-report: check-venv
	@echo "$(GREEN)Coverage report:$(NC)"
	coverage report

# ============================================================================
# DOCUMENTATION TARGETS
# ============================================================================

# ============================================================================
# TARGET: docs - Check markdown documentation format
# ============================================================================
docs: check-venv
	@echo "$(GREEN)Checking markdown documentation...$(NC)"
	mdformat --check README.md AUTHORS.md CONTRIBUTING.md SECURITY.md CHANGELOG.md
	mdformat --check $$(find $(DOCS_DIR) -type f -name '*.md')
	@echo "$(GREEN)✓ Documentation check complete$(NC)"

# ============================================================================
# TARGET: docs-format - Auto-format markdown files
# ============================================================================
docs-format: check-venv
	@echo "$(GREEN)Auto-formatting markdown documentation...$(NC)"
	mdformat README.md AUTHORS.md CONTRIBUTING.md SECURITY.md CHANGELOG.md
	mdformat $$(find $(DOCS_DIR) -type f -name '*.md')
	@echo "$(GREEN)✓ Documentation formatting complete$(NC)"

# ============================================================================
# DEVELOPMENT TARGETS
# ============================================================================

# ============================================================================
# TARGET: dev - Development server (API with hot reload)
# ============================================================================
dev: check-venv
	@echo "$(GREEN)Starting development server (API)...$(NC)"
	@echo "$(YELLOW)Server running at: http://localhost:8000$(NC)"
	@echo "$(YELLOW)API docs at: http://localhost:8000/docs$(NC)"
	@echo "$(YELLOW)Press Ctrl+C to stop$(NC)"
	uvicorn src.api.app:app --reload --port 8000

# ============================================================================
# TARGET: dev-api - Start API server with live reload
# ============================================================================
dev-api: check-venv
	@echo "$(GREEN)Starting FastAPI development server...$(NC)"
	uvicorn src.api.app:app --reload --port 8000 --host 0.0.0.0

# ============================================================================
# TARGET: dev-cli - Interactive CLI shell
# ============================================================================
dev-cli: check-venv
	@echo "$(GREEN)Starting interactive CLI...$(NC)"
	$(PYTHON) -m src.cli.main --interactive

# ============================================================================
# TARGET: shell - Python interactive shell with project context
# ============================================================================
shell: check-venv
	@echo "$(GREEN)Starting Python shell with project context...$(NC)"
	$(PYTHON) -c "import sys; sys.path.insert(0, 'src'); print('$(GREEN)Imported: src directory$(NC)'); import IPython; IPython.start_ipython()" 2>/dev/null || \
	$(PYTHON) -i -c "import sys; sys.path.insert(0, 'src'); print('Use: from src.module import function')"

# ============================================================================
# TARGET: notebook - Start Jupyter notebook server
# ============================================================================
notebook: check-venv
	@echo "$(GREEN)Starting Jupyter notebook server...$(NC)"
	@echo "$(YELLOW)Notebooks location: $(BENCHMARKS_DIR)/notebooks/$(NC)"
	jupyter lab --notebook-dir=.

# ============================================================================
# HEALTH & PERFORMANCE TARGETS
# ============================================================================

# ============================================================================
# TARGET: health - Quick health check (lint + type + unit tests)
# ============================================================================
health: check-venv lint typecheck unit
	@echo
	@echo "$(GREEN)════════════════════════════════════════════════════════════════════════════════$(NC)"
	@echo "$(GREEN)✓ HEALTH CHECK PASSED: Code quality, types, and unit tests all passing$(NC)"
	@echo "$(GREEN)════════════════════════════════════════════════════════════════════════════════$(NC)"

# ============================================================================
# TARGET: performance - Profile performance of key functions
# ============================================================================
performance: check-venv
	@echo "$(GREEN)Running performance profiling...$(NC)"
	$(PYTHON) -m cProfile -s cumtime -m pytest $(BENCHMARKS_DIR) --benchmark-only -q
	@echo "$(GREEN)✓ Performance profiling complete$(NC)"

# ============================================================================
# GIT & RELEASE TARGETS
# ============================================================================

# ============================================================================
# TARGET: pre-commit-check - Verify pre-commit hooks are installed
# ============================================================================
pre-commit-check:
	@echo "$(GREEN)Checking pre-commit hooks...$(NC)"
	@if [ -d .git/hooks ] && [ -f .git/hooks/pre-commit ]; then \
		echo "$(GREEN)✓ Pre-commit hooks installed$(NC)"; \
	else \
		echo "$(YELLOW)Pre-commit hooks not installed. Install with: pre-commit install$(NC)"; \
	fi

# ============================================================================
# TARGET: pre-commit-run - Run all pre-commit hooks on all files
# ============================================================================
pre-commit-run: check-venv
	@echo "$(GREEN)Running pre-commit hooks on all files...$(NC)"
	pre-commit run --all-files
	@echo "$(GREEN)✓ Pre-commit checks complete$(NC)"

# ============================================================================
# TARGET: version - Show project version
# ============================================================================
version:
	@echo "$(BLUE)$(PROJECT_NAME) v$(PROJECT_VERSION)$(NC)"

# ============================================================================
# UTILITIES TARGETS
# ============================================================================

# ============================================================================
# TARGET: export-requirements - Export dependencies to requirements.txt
# ============================================================================
export-requirements: check-venv
	@echo "$(GREEN)Exporting dependencies...$(NC)"
	pip freeze | grep -v "^-e" > requirements-lock.txt
	@echo "$(GREEN)✓ Dependencies exported to requirements-lock.txt$(NC)"

# ============================================================================
# CLEANING TARGETS
# ============================================================================

# ============================================================================
# TARGET: clean-py - Remove Python cache and compiled files
# ============================================================================
clean-py:
	@echo "$(YELLOW)Cleaning Python cache...$(NC)"
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type f -name '*.pyd' -delete
	rm -rf .eggs/ *.egg-info/ dist/ build/
	@echo "$(GREEN)✓ Python cache cleaned$(NC)"

# ============================================================================
# TARGET: clean-test - Remove test artifacts and coverage
# ============================================================================
clean-test:
	@echo "$(YELLOW)Cleaning test artifacts...$(NC)"
	rm -rf .pytest_cache/ .tox/ htmlcov/ .coverage .coverage.*
	rm -rf tests/.pytest_cache/ coverage.xml coverage.json
	@echo "$(GREEN)✓ Test artifacts cleaned$(NC)"

# ============================================================================
# TARGET: clean-build - Remove build and type-check caches
# ============================================================================
clean-build:
	@echo "$(YELLOW)Cleaning build and cache directories...$(NC)"
	rm -rf .mypy_cache/ .ruff_cache/ build/ dist/
	@echo "$(GREEN)✓ Build caches cleaned$(NC)"

# ============================================================================
# TARGET: clean-cache - Remove all IDE and editor caches
# ============================================================================
clean-cache:
	@echo "$(YELLOW)Cleaning IDE and editor caches...$(NC)"
	rm -rf .vscode/ .idea/ .DS_Store Thumbs.db
	rm -rf *.swp *.swo *~ .*.un~
	@echo "$(GREEN)✓ IDE caches cleaned$(NC)"

# ============================================================================
# TARGET: clean - Remove Python, test, and build artifacts
# ============================================================================
clean: clean-py clean-test clean-build
	@echo "$(GREEN)✓ Cleanup complete (Python, tests, builds)$(NC)"

# ============================================================================
# TARGET: clean-all - Complete cleanup including venv and data
# ============================================================================
clean-all: clean
	@echo "$(YELLOW)Removing virtual environment and generated data...$(NC)"
	rm -rf $(VENV)/ .venv/
	rm -rf data/cache/* data/processed/* data/exports/* data/manifests/*.jsonl
	rm -rf htmlcov/ .coverage .mypy_cache/ .ruff_cache/
	rm -f benchmark_results.json requirements-lock.txt
	@echo "$(GREEN)✓ Complete cleanup finished. Ready for fresh start.$(NC)"

# ============================================================================
# DEFAULT TARGET
# ============================================================================

# If no target specified, show help
.DEFAULT_GOAL := help

# ============================================================================
# SPECIAL TARGETS
# ============================================================================

# Silent target for internal use (suppresses output)
.SILENT: info version

# ============================================================================
# NOTES AND DOCUMENTATION
# ============================================================================

# QUICK REFERENCE:
# ================
#
# Installation & Setup:
#   make venv              # Create virtual environment
#   make install           # Install with dev + test deps
#   make install-full      # Install everything
#
# Development Workflow:
#   make lint              # Check code style
#   make format            # Auto-format code
#   make typecheck         # Check types
#   make health            # Quick quality check
#   make dev               # Start dev server
#
# Testing:
#   make test              # Run all tests
#   make coverage          # Run with coverage report
#   make coverage-html     # Generate HTML report
#   make benchmark         # Run performance tests
#
# Cleanup:
#   make clean             # Remove caches and build artifacts
#   make clean-all         # Full cleanup (careful!)
#
# Documentation:
#   make docs              # Check markdown format
#   make docs-format       # Auto-format markdown
#

# ADVANCED USAGE:
# ===============
#
# Run with custom options:
#   make test WORKERS=8           # Use 8 parallel workers
#   make coverage COVERAGE_THRESHOLD=70  # Custom coverage threshold
#
# Chain targets:
#   make format typecheck test    # Format, check types, then test
#   make clean install health     # Clean, install, quick health check
#

# ENVIRONMENT VARIABLES:
# =====================
#
# PYTHON      - Python executable (default: python3.12 or python3)
# VENV        - Virtual environment path (default: .venv)
# WORKERS     - Parallel test workers (default: 0 = auto)
# COVERAGE_THRESHOLD - Minimum coverage % (default: 80)

# COLORS:
# =======
# GREEN    - Success messages
# YELLOW   - Warnings, action items
# RED      - Errors
# BLUE     - Headers, info

# TROUBLESHOOTING:
# ================
#
# Issue: "make: command not found"
#   Solution: Install GNU Make
#   - macOS: brew install make gmake
#   - Linux: apt-get install build-essential
#   - Windows: choco install make or use WSL2
#
# Issue: "SHELL: command not found"
#   Solution: Ensure bash is installed
#   Windows: Use Git Bash or WSL2
#
# Issue: Virtual environment not found
#   Solution: Run: make venv && make install
#

# INTEGRATION WITH CI/CD:
# =======================
#
# GitHub Actions:
#   - name: Run checks
#     run: make health
#
#   - name: Run tests
#     run: make coverage
#
# GitLab CI:
#   script:
#     - make install-full
#     - make health
#     - make coverage
#

# Last Updated: 2026-04-05
# Maintained by: Zakir Bayramov, Gustav Olaf Yunus Laitinen-Lundström Fredriksson-Imanov

