# Security Policy & Incident Response

| Field | Value |
|---|---|
| Owner | Security Team |
| Department | Security |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Restricted |

## Executive Summary

This document defines comprehensive security policies, vulnerability management procedures, supported versions, operational safeguards, and incident response processes for the **Stochastic Transit Router** project. The document is intended for:

- **Security researchers** reporting vulnerabilities
- **Contributors** implementing security-sensitive features
- **Producers** deploying the system in production
- **Maintainers** responsible for security operations

**Last Updated:** 2026-04-05
**Scope:** All components in this repository
**Primary Contacts:** zakirbayramov942@gmail.com, olaf.laitinen@uni.lu
**Emergency Escalation:** Both maintainers (simultaneous notification)

---

## Table of Contents

1. [Supported Versions & Lifecycle](#supported-versions--lifecycle)
2. [Vulnerability Reporting Process](#vulnerability-reporting-process)
3. [Sensitivity Classification](#sensitivity-classification)
4. [Response & Remediation Procedures](#response--remediation-procedures)
5. [Severity & Timeline](#severity-and-timeline)
6. [Operational Safeguards](#operational-safeguards)
7. [Development Security Practices](#development-security-practices)
8. [Known Limitations & Mitigations](#known-limitations--mitigations)
9. [Compliance & Auditing](#compliance--auditing)
10. [Security Checklist](#security-checklist)
11. [Related Documentation](#related-documentation)

---

## Supported Versions & Lifecycle

### Version Support Matrix

| Version | Python | Status | Release Date | End of Support | Security Patches | Notes |
|---------|--------|--------|--------------|----------------|------------------|-------|
| 0.1.x | 3.12+ | ✓ Supported | 2026-04-05 | 2027-04-05 | Yes (12 months) | Current stable release - receives all security updates |
| 0.0.x | Any | ✗ Unsupported | Pre-alpha | 2026-04-05 | No | Pre-release development version - no security support |

### Support Lifecycle Details

**Current Stable Release (0.1.x):**
- Released: 2026-04-05
- End of Support: 2027-04-05
- Security Patch Window: Full 12 months
- Maintenance: Active (bug fixes, security updates, minor enhancements)
- Upgrade Policy: Non-breaking; users encouraged to upgrade within 30 days of patch release

**Pre-Release Version (0.0.x):**
- Status: No longer supported
- Users: Migrate to 0.1.x immediately
- Patch Policy: No security patches will be released; upgrade required for fixes

### Version Deprecation Schedule

| Version | EOL Announcement | Final Security Patch | Support Ends |
|---------|------------------|---------------------|--------------|
| 0.1.x | 2027-01-05 | 2027-04-05 | 2027-04-05 |
| 0.2.x | TBD (18 months post-release) | TBD | TBD |

### How to Check Your Version

```bash
# Check installed version
pip show stochastic-transit-router

# Check version from Python
python -c "import stochastic_transit_router; print(stochastic_transit_router.__version__)"

# Verify you're on a supported version
# Expected: 0.1.x or later
```

---

## Vulnerability Reporting Process

### Reporting Guidelines

**CRITICAL:** Do NOT use GitHub Issues, GitHub Discussions, or any public channel for security reports.

#### Step 1: Initial Report

Send an email to **BOTH** maintainers with the following information:

**Required Information:**
- Your full name and contact information
- Affected component(s) and version(s)
- Detailed vulnerability description
- Proof of concept or reproduction steps
- Estimated severity (Critical/High/Medium/Low)
- Impact assessment (data exposure, availability, integrity, confidentiality)
- Timeline preference (if you plan public disclosure)

**Optional Information:**
- Suggested remediation
- Your organization/affiliation
- CVSS score (if you've calculated one)
- Related CVEs (if applicable)
- Security advisories or standards (CWE, OWASP)

**Email Template:**

```
Subject: [SECURITY] Vulnerability Report - <component> - <short description>

Affected Version(s): <list versions>
Affected Component(s): <e.g., GTFS Loader, API Route Handler>
Severity: <Critical/High/Medium/Low>
CVSS Score (if available): <score>

## Vulnerability Description
[Detailed description of the vulnerability]

## Proof of Concept / Reproduction Steps
[Step-by-step instructions to reproduce]

## Impact Assessment
[What an attacker could do with this vulnerability]

## Potential Fix
[Optional - your suggested fix]

## Timeline Preferences
[Do you have a disclosure deadline?]
```

**Send To:**
```
Zakir Bayramov      <zakirbayramov942@gmail.com>
Gustav Olaf Yunus   <olaf.laitinen@uni.lu>
```

#### Step 2: Confidentiality Agreement

By reporting a vulnerability:
- You agree NOT to disclose the vulnerability publicly until a patch is released
- You acknowledge we may contact you for clarification
- You authorize us to prepare a security advisory
- You understand we will credit you (with permission) upon disclosure

### Reporting Channels

| Channel | Status | Use Case |
|---------|--------|----------|
| Email (both maintainers) | ✓ Preferred | All vulnerability reports |
| GitHub Security Advisory | ⚠ Secondary | If email is unavailable |
| PGP Encryption | ⚠ Available | For highly sensitive reports (public keys on GitHub) |
| Public Issues | ✗ Never | Do NOT use for security reports |
| Slack/Discord | ✗ Never | Do NOT use for security reports |

### Response Guarantee

**Initial Response SLA:**
- **Acknowledgement:** Within 2 working days (48 hours)
- **Initial Assessment:** Within 5 working days
- **Status Updates:** Every 5-7 days thereafter

We will provide you with:
1. Incident reference number (e.g., SEC-2026-001)
2. Initial severity assessment
3. Estimated timeline for fix release
4. Point of contact for questions

---

## Sensitivity Classification

### Information Classification Levels

| Level | Definition | Inside Project | Public Exposure | Handling |
|-------|-----------|-----------------|-----------------|----------|
| **Public** | May be freely shared; no confidentiality needed | Documentation, API specs, architecture | GitHub public repository | No restrictions |
| **Internal** | For project team only; not for external distribution | Development notes, security procedures, credentials | Private repository access | Password-protected; team only |
| **Restricted** | Highly sensitive; limited access required | Security vulnerabilities, pre-disclosure advisories, zero-days | Encrypted email only | Immediate destruction after incident closure |

### Pre-Disclosure Embargo Policy

**Zero-Day Vulnerabilities (0-day):**
- Embargo period: 90 days from patch release
- During embargo: Details withheld from public documentation
- After embargo: Full disclosure permitted
- Coordination: We align with other affected projects' disclosure timelines

**Known Vulnerabilities (N-day):**
- Embargo period: 30 days from patch release
- During embargo: Advisory withheld or redacted
- After embargo: Full advisory published
- Coordination: May contact other maintainers for parallel disclosure

### Embargo Breach Consequences

If a reporter breaches embargo:
- We will immediately publish the advisory (if patch available)
- Reporter will be banned from future bug bounty programs (if applicable)
- We reserve right to report to relevant authorities (if applicable)

---

## Response & Remediation Procedures

### Incident Response Team

| Role | Team Member(s) | Responsibility |
|------|-----------------|-----------------|
| **Coordinator** | Zakir Bayramov | Lead response; customer communication |
| **Technical Lead** | Gustav Olaf Yunus Laitinen-Lundström Fredriksson-Imanov | Severity assessment; fix development |
| **Code Reviewer** | Both maintainers | Patch review; approval before release |
| **Release Manager** | Zakir Bayramov | Package distribution; advisory publication |

### Triage Process

**Timeline: Day 1-2**

Upon receiving a vulnerability report:

1. **Acknowledge receipt** (within 24 hours)
   - Send incident reference number
   - Confirm reporter identity
   - Request any missing information

2. **Verify vulnerability** (within 48 hours)
   - Reproduce the issue independently
   - Assess reproducibility (100%, sometimes, rarely)
   - Document proof of concept

3. **Classify severity** (within 5 days)
   - Evaluate CVSS score
   - Assess real-world exploitability
   - Determine business impact
   - Assign priority level

### Investigation Phase

**Timeline: Day 2-7**

1. **Root cause analysis**
   - Identify vulnerable code location(s)
   - Determine how vulnerability was introduced
   - Check if similar vulnerabilities exist elsewhere

2. **Scope assessment**
   - Determine affected versions
   - Identify affected components
   - Calculate number of users/deployments
   - Assess business impact

3. **Exploitation scenarios**
   - Document realistic attack vectors
   - Evaluate attack difficulty (easy/moderate/complex)
   - Assess damage potential

### Fix Development & Review

**Timeline: Day 5-15+**

1. **Patch development**
   - Create fix branch from latest release tag
   - Keep changes minimal and focused
   - Include comprehensive test coverage
   - Document fix in commit message

2. **Code review** (Security-Focused)
   - Both maintainers review independently
   - Check for regression risks
   - Verify fix completeness
   - Validate test coverage
   - Approval required from both

3. **Testing**
   - Unit tests (must pass)
   - Integration tests (must pass)
   - Regression tests (running full test suite)
   - Performance tests (no regressions)

### Release & Disclosure

**Timeline: Day 15-30+**

1. **Prepare security advisory**
   - Document vulnerability details
   - Provide mitigation steps
   - Credit reporter (if appropriate)
   - Use GitHub Security Advisory format

2. **Release security patch**
   - Tag new version (e.g., 0.1.1)
   - Publish to PyPI
   - Deploy to all affected systems
   - Verify installation works

3. **Publish advisory**
   - Post on GitHub Security Advisory (public)
   - Notify affected users via email list (if applicable)
   - Announce in project communication channels
   - Update CHANGELOG.md

4. **Post-incident**
   - Document lessons learned
   - Update security procedures (if needed)
   - Audit similar code patterns
   - Schedule review of related components

---

## Severity and Timeline

### CVSS v3.1 Severity Classification

| Severity | CVSS Score | Real-World Impact | Response SLA | Example Vulnerability |
|----------|------------|------|------|--------|
| **Critical** | 9.0–10.0 | Arbitrary code execution, complete system compromise, full data breach, remote exploit without authentication | **24 hours** initial response; **48 hours** patch release | Unauthenticated RCE, SQL injection with data access, privilege escalation to admin |
| **High** | 7.0–8.9 | Significant privilege escalation, substantial data exposure, authentication/authorization bypass, availability impact | **3 days** response; **7 days** patch release | Authenticated RCE, unauthenticated information disclosure, privilege escalation to user |
| **Medium** | 4.0–6.9 | Limited privilege escalation, partial data exposure, limited DoS, functional impairment | **7 days** response; **30 days** patch release | Unauthenticated access to non-critical data, limited DoS, input validation bypass |
| **Low** | 0.1–3.9 | Minor information disclosure, edge-case crashes, non-exploitable behavior | **30 days** response; **90 days** patch release | Verbose error messages, deprecated API usage warnings |

### Severity Assessment Criteria

**Confidentiality Impact:**
- High: Complete data exposure (all records, all fields)
- Medium: Partial data exposure (some records or some fields)
- Low: Minimal information disclosure

**Integrity Impact:**
- High: Can modify critical system state or user data without authorization
- Medium: Can modify non-critical data or limited system state
- Low: Can only modify logs or non-functional metadata

**Availability Impact:**
- High: Complete service outage or unavailable for extended period (>1 hour)
- Medium: Significant performance degradation (50%+ latency increase)
- Low: Minor performance impact or rare conditions

**Attack Complexity:**
- Low: Simple exploitation; no special configuration; readily available tools
- High: Complex exploitation; requires specific conditions; special setup needed

**Authentication Required:**
- Yes: Exploit requires valid credentials
- No: Exploit works on unauthenticated API/component

### Timeline Examples

**Critical CVSS 9.5 - Remote Unauthenticated Code Execution**
```
Day 1: Initial contact + verification (4 hours)
Day 1-2: Severity assessment (24 hours)
Day 2-3: Root cause identified; fix in progress (24 hours)
Day 3: Patch tested; ready for release (24 hours)
Total: 72 hours to patch release
```

**High CVSS 7.5 - Authenticated Information Disclosure**
```
Day 1: Initial contact + verification (24 hours)
Day 2-3: Severity assessment (48 hours)
Day 3-5: Fix development and testing (48 hours)
Day 5-7: Patch released (2 days)
Total: 7 days to patch release
```

---

## Operational Safeguards

### Defense-in-Depth Architecture

```
Layer 1: Input Validation (API Gateway)
         ↓
Layer 2: Pydantic Schema Enforcement
         ↓
Layer 3: Business Logic Validation
         ↓
Layer 4: Data Integrity Checks
         ↓
Layer 5: Access Control & Authorization
         ↓
Layer 6: Audit Logging & Monitoring
```

### Secrets Management

**Policy:**
- All API keys, authentication tokens, and credentials managed via environment variables
- Secrets NEVER hardcoded in source code or configuration files
- Secrets NEVER logged in debug output or error messages
- Pre-commit hooks scan for accidentally committed secrets

**Implementation:**
```python
# ✓ CORRECT: Secrets from environment
import os

API_KEY = os.getenv("TRANSIT_API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# ✗ WRONG: Hardcoded secrets
API_KEY = "sk-1234567890abcdef"  # NEVER!
DB_PASSWORD = "MyPassword123"     # NEVER!
```

**Environment Variable Convention:**
```
TRANSIT_API_KEY              # External API keys
TRANSIT_DB_PASSWORD         # Database credentials
TRANSIT_AUTH_SECRET         # JWT/Auth secrets
TRANSIT_GCP_SERVICE_ACCOUNT  # Cloud credentials
```

**Rotation Policy:**
- Secrets rotated every 90 days minimum
- Rotation triggered immediately upon suspected compromise
- Old secrets maintained for 7 days for backward compatibility

### Input Validation

**Principle:** All external inputs are malicious until proven otherwise.

**Implementation: Pydantic Schema Enforcement**

```python
from pydantic import BaseModel, Field, validator
from datetime import datetime

class RouteRequest(BaseModel):
    origin: int = Field(..., gt=0, description="Valid node ID")
    destination: int = Field(..., gt=0, description="Valid node ID")
    departure_time: int = Field(..., ge=0, le=2**31-1, description="Unix timestamp")
    max_transfers: int = Field(default=5, ge=0, le=20)

    @validator('arrival_time')
    def validate_time_bounds(cls, v):
        now = int(datetime.now().timestamp())
        if v < now:
            raise ValueError("Cannot request historical routes")
        if v > now + 7*24*3600:  # 7 days
            raise ValueError("Requested time beyond planning horizon")
        return v

    @validator('origin', 'destination')
    def validate_node_exists(cls, v):
        if not graph.has_node(v):
            raise ValueError(f"Node {v} does not exist")
        return v
```

**Validation Points:**
- Type checking (int, str, float, bool)
- Range checking (min/max values)
- Pattern checking (regex for strings)
- Referential integrity (does ID exist?)
- Business logic validation (departure time >= current time)

**Coverage:** 100% of API endpoints; 100% of CLI inputs

### Authentication & Authorization

**Current Status:** v0.1.0 includes NO built-in authentication

**Deployment Recommendation:** Use reverse proxy (nginx) with:
- OAuth 2.0 / OIDC integration
- API key management
- Rate limiting
- TLS termination

**Example Nginx Configuration:**
```nginx
server {
    listen 443 ssl http2;
    ssl_certificate /etc/ssl/certs/transit-router.crt;
    ssl_certificate_key /etc/ssl/private/transit-router.key;
    ssl_protocols TLSv1.2 TLSv1.3;

    auth_basic "Stochastic Transit Router";
    auth_basic_user_file /etc/nginx/.htpasswd;

    location /api/ {
        proxy_pass http://localhost:8000;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Scheme $scheme;
    }
}
```

### Rate Limiting

**Configuration:**
- Per-IP limit: 1,000 requests per 15 minutes (67 req/min)
- Burst limit: 100 requests per 10 seconds (6 req/sec)
- Penalty: Auto-blacklist after 10 violations (24-hour cooldown)

**Implementation:**
```python
from fastapi import Request
from fastapi_limiter import FastAPILimiter

@app.get("/route")
@limiter.limit("1000/15minutes")
async def get_route(request: Request):
    # Endpoint logic
    pass
```

**Bypass Considerations:**
- Registered users: 10x higher limits (if auth layer added)
- Admin accounts: Unlimited (with monitoring)
- Whitelist: Internal microservices (if deployed)

### Feed Handling & Validation

**Real-time Feed Security:**

| Aspect | Mechanism | Details |
|--------|-----------|---------|
| **Schema Validation** | Pydantic models | Reject invalid GTFS-RT messages |
| **Timeout Protection** | 30-second timeout | Prevent stalled feed hangs |
| **Integrity Checking** | SHA-256 hash validation | Detect corrupted feeds |
| **Retry Logic** | Exponential backoff (max 3 retries) | Robust to transient failures |
| **Stale Detection** | Age check (>10 min warning) | Alert if feed outdated |
| **Fallback Strategy** | Use static schedule if feed fails | Graceful degradation |
| **Quarantine** | Isolate failed feeds from routing | Prevent bad data propagation |

**Feed Refresh Procedure:**
```python
import asyncio
import hashlib
from datetime import datetime, timedelta

async def refresh_feeds():
    for feed_url in FEED_URLS:
        try:
            # Fetch with timeout
            response = await fetch_url(feed_url, timeout=30)

            # Integrity check
            feed_hash = hashlib.sha256(response.content).hexdigest()
            if not validate_hash(feed_hash, expected_hash):
                print(f"SECURITY: Feed hash mismatch for {feed_url}")
                continue

            # Schema validation
            gtfs_rt = parse_gtfs_rt(response.content)

            # Age check
            feed_age = datetime.now() - gtfs_rt.timestamp
            if feed_age > timedelta(minutes=10):
                print(f"WARNING: Feed age is {feed_age}")

            # Update
            update_routing_data(gtfs_rt)

        except TimeoutError:
            print(f"WARN: Feed fetch timeout for {feed_url}")
            # Fall back to static schedule
        except Exception as e:
            print(f"ERROR: Feed parsing failed: {e}")
            # Quarantine feed; use previous version
```

### Dependency Management

**Policy:**
- All versions pinned in `pyproject.toml` (no floating versions)
- Dependabot enabled for automated vulnerability scanning
- CI/CD fails if vulnerable packages detected (via Safety/Bandit)
- Security updates applied within 7 days of disclosure
- Breaking updates reviewed by maintainers before merge

**Dependencies Audit:**

```bash
# Check for known vulnerabilities
pip install safety
safety check

# Generate SBOM (Software Bill of Materials)
pip install cyclonedx-bom
cyclonedx-py -o sbom.xml

# Review dependency tree
pip install pipdeptree
pipdeptree
```

**Vulnerable Dependency Response:**

1. **Alert received** → Immediate assessment
2. **If critical** → Apply patch same day
3. **If high** → Apply patch within 3 days
4. **If medium/low** → Apply patch within 7 days
5. **Patch applied** → Run full test suite
6. **Tests pass** → Release new version
7. **Users notified** → Via GitHub release notes

### Code Review & SAST

**Mandatory Code Review:**
- All changes require review by at least one maintainer
- Security-sensitive changes require review by both maintainers
- Reviewers check for:
  - Hardcoded secrets
  - Input validation gaps
  - Unsafe deserialization
  - Injection vulnerabilities
  - Cryptographic weaknesses

**Static Analysis Security Testing (SAST):**
- Ruff with security rules enabled
- Bandit for Python-specific issues
- MyPy strict type checking
- All checks required to pass before merge

**Pre-commit Hooks:**
```bash
# Installed automatically on 'make dev-setup'
pre-commit install

# Checks run on every commit:
- Secret scanning (detect-secrets)
- Ruff linting + formatting
- MyPy type checking
- YAML validation
- Trailing whitespaces
```

### TLS/HTTPS Requirements

**Minimum Configuration:**
- TLS 1.2 or later (no SSL 3.0, TLS 1.0, 1.1)
- Strong cipher suites (ECDHE, AES-256-GCM)
- HSTS header enabled (Strict-Transport-Security)
- Certificate validity checked (no self-signed in production)

**API Deployment (FastAPI + Uvicorn):**
```bash
# Production deployment with TLS
uvicorn \
    stochastic_transit_router.api.main:app \
    --ssl-keyfile=/etc/ssl/private/key.pem \
    --ssl-certfile=/etc/ssl/certs/cert.pem \
    --ssl-version=TLSv1_2
```

### Error Handling & Information Disclosure

**Policy:**
- Production errors return generic messages ("Internal Server Error")
- Detailed stacktraces logged serverside only
- No database details in error messages
- No file paths in error messages
- No version numbers in error messages (if avoidable)

**Error Response Examples:**
```python
# ✓ CORRECT: Generic frontend error
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error. Please try again later."}
    )

# ✗ WRONG: Leaks sensitive information
return {
    "error": "Database connection failed on host db.internal.example.com",
    "exception": "psycopg2.OperationalError: ...",
    "traceback": "..."
}
```

---

## Development Security Practices

### Secure Coding Standards

**1. Input Sanitization**
```python
# Sanitize user-provided graph node IDs
def get_shortest_path(origin_id: int, destination_id: int) -> Path:
    # Validation at schema layer (Pydantic)
    # Additional checks before graph operations
    if not isinstance(origin_id, int):
        raise ValueError("origin_id must be integer")
    if origin_id not in self.graph:
        raise ValueError(f"Node {origin_id} not in graph")
    # Safe to use
    return self.graph.shortest_path(origin_id, destination_id)
```

**2. Avoid Dangerous Functions**
```python
# ✗ DANGEROUS: eval(), exec(), pickle unsafe loads
data = pickle.loads(untrusted_data)  # Risk: arbitrary code execution
result = eval(user_input)            # Risk: arbitrary code execution

# ✓ SAFE: Use safe alternatives
import json
data = json.loads(untrusted_data)    # Safe: only JSON structures
data = pickle.loads(untrusted_data, encoding='latin1')  # Restricted to objects
# OR use secure alternative like msgpack with schema validation
```

**3. Cryptography Best Practices**
```python
import secrets
from cryptography.fernet import Fernet

# ✓ CORRECT: Use secrets for random values
random_token = secrets.token_urlsafe(32)

# ✗ WRONG: Don't use random module for security
import random
weak_token = str(random.random())

# Use established crypto libraries, not custom implementations
# Let Fernet handle encryption/decryption
cipher = Fernet(key)
encrypted = cipher.encrypt(b"secret")
```

**4. Logging & Debugging**
```python
import logging
logger = logging.getLogger(__name__)

# ✓ CORRECT: Safe logging
logger.info(f"User {user_id} requested route")
logger.debug(f"Route calculation parameters: {params}")

# ✗ WRONG: Logging secrets
logger.info(f"API key: {api_key}")
logger.debug(f"Database password: {db_password}")

# Use structured logging (JSON) for analysis
import structlog
logger.info("route_requested", user_id=user_id, timestamp=datetime.now())
```

### Security Testing

**Test Categories:**

| Category | Framework | Examples |
|----------|-----------|----------|
| **Unit Tests** | pytest | Validate input ranges, error conditions |
| **Integration Tests** | pytest + respx | API endpoint security, feed validation |
| **Security Tests** | pytest + custom | Injection attempts, malformed inputs |
| **Fuzz Testing** | hypothesis | Random input generation; crash detection |
| **SAST** | Bandit, Ruff | Code pattern analysis; vulnerability detection |

**Example Security Test:**
```python
import pytest
from hypothesis import given, strategies as st

class TestInputValidation:

    @given(st.integers())
    def test_node_id_validation(self, node_id):
        """Security: Only valid node IDs accepted"""
        if node_id < 0 or node_id > 1_000_000:
            with pytest.raises(ValueError):
                route_service.get_node(node_id)
        else:
            # Should not raise if valid
            result = route_service.get_node(node_id)
            assert result is not None or node_id not in graph

    def test_sql_injection_prevention(self):
        """Security: SQL injection attempt blocked"""
        malicious_input = "1; DROP TABLE routes; --"
        # Should be rejected as invalid integer
        with pytest.raises(ValueError):
            RouteRequest(origin=malicious_input)
```

### Deployment Security

**Pre-Deployment Checklist:**

- [ ] All dependencies updated and vulnerability-scanned
- [ ] Security environment variables configured
- [ ] TLS certificate installed (valid, not self-signed)
- [ ] Database credentials changed from defaults
- [ ] Logging configured (sensitive data excluded)
- [ ] Rate limiting enabled
- [ ] Firewall rules configured
- [ ] Backups tested
- [ ] Monitoring & alerting configured
- [ ] Incident response procedures documented

---

## Known Limitations & Mitigations

### Deterministic Seeding (Reproducibility)

| Aspect | limitation | Implications | Mitigation |
|--------|-----------|--------------|-----------|
| **What** | Benchmark reproducibility uses fixed random seeds | Predictable results for deterministic testing | Seed values logged separately; not used in production routing |
| **Risk** | Seed values become known; future runs predictable (low risk) | Theoretical concern; minimal real-world impact | Use cryptographically random seeds in production |
| **Mitigation** | Seeds documented in benchmark configs, not in code | Random values can be manually verified | Change seeds for each deployment cycle |

### Graph In-Memory Storage

| Aspect | Limitation | Implications | Mitigation |
|--------|-----------|--------------|-----------|
| **What** | Full transit graph loaded into RAM during startup | Memory usage ~500MB for NYC; larger networks need more RAM | Monitor memory; consider graph partitioning strategies |
| **Risk** | Out-of-memory crash if graph swells; slow startup | Service disruption if RAM exhausted | Set memory limits; implement graph compression |
| **Mitigation** | Pre-calculate graph size; monitor RSS memory | Proactive capacity planning | Implement incremental graph loading (roadmap item) |

### Real-Time Feed Latency

| Aspect | Limitation | Implications | Mitigation |
|--------|-----------|--------------|-----------|
| **What** | 30-60 second delay between feed update and service availability | Routing suggestions may be slightly stale | Document latency in API responses |
| **Risk** | User receives suboptimal suggestions if feed stale | Low risk; suggestions still valid | Use cached fall-back if feed stale |
| **Mitigation** | Fetch feeds every 30 seconds; validate age | Explicit API response timestamp | Cache previous feed version; use if fresshness check fails |

### No Authentication (v0.1.0)

| Aspect | Limitation | Implications | Mitigation |
|--------|-----------|--------------|-----------|
| **What** | API lacks per-user authentication | Any client can access endpoints | Assume production includes reverse proxy (nginx) with auth |
| **Risk** | Unauthenticated access; no per-user rate limiting | Resource exhaustion; privacy concerns | Deploy behind authentication layer |
| **Mitigation** | Document deployment requirements | Use examples from CONTRIBUTING guide | Roadmap: Implement optional API key authentication in v0.2 |

### Pickle Deserialization

| Aspect | Limitation | Implications | Mitigation |
|--------|-----------|--------------|-----------|
| **What** | Graph serialized/deserialized via pickle | Pickle can execute arbitrary code if malicious | Only load graphs from trusted sources |
| **Risk** | Malicious pickle files can execute code | Critical if attacker controls graph files | Validate file source; checksum verification |
| **Mitigation** | Graph files stored in secure location | File permissions restrict write access | Roadmap: Migrate to msgpack (safer serialization) |

---

## Compliance & Auditing

### Applicable Standards & Frameworks

| Standard | Coverage | Status | Notes |
|----------|----------|--------|-------|
| **OWASP Top 10** | Web application security risks | Designed to mitigate all 10 | Input validation, injection prevention, secure headers |
| **CWE (Common Weakness Enumeration)** | Software weakness catalog | Addressed in code review | Static analysis checks CWE patterns |
| **NIST Cybersecurity Framework** | Security governance | Roadmap (v0.2+) | Currently implements core practices |
| **EUPL-1.2 License** | Open-source compliance | Full compliance | All files include EUPL headers |
| **GDPR** | Data privacy (if deployed in EU) | Partially applicable | No user data stored by default; document handling if integrated |

### Audit Trail & Logging

**Audit Events:**
- API requests (timestamp, endpoint, IP, response code — no request body)
- Authentication attempts (if auth layer added)
- Security policy changes (documented in ADRs)
- Vulnerability reports received
- Patches released

**Log Retention:**
- Application logs: 90 days (compressed after 30 days)
- Security events: 1 year (encrypted storage)
- Incident reports: Permanent (separate archive)

**Log Access:**
- Restricted to maintainers and security team
- No export to external logging services (self-hosted only)
- Read access logged (audit of audit logs)

### Security Audit & Penetration Testing

**Self-Assessment Frequency:** Annually

**External Assessment:** Available upon request (not currently contracted)

**Testing Scope (if performed):**
- Input validation resilience (fuzzing, injection attempts)
- Authentication/authorization logic
- API endpoint security
- Dependency vulnerability assessment
- Secrets/credentials exposure check
- Cryptography implementation review

---

## Security Checklist for Contributors

Before submitting a pull request with security-sensitive changes:

**Code Security:**
- [ ] No hardcoded secrets (API keys, passwords, tokens)
- [ ] All user inputs validated with Pydantic or similar
- [ ] No disabled security checks (e.g., `# type: ignore` justified)
- [ ] Type hints present (no `Any` without justification)
- [ ] Error messages don't leak sensitive information
- [ ] No use of `eval()`, `exec()`, or `compile()` on user input
- [ ] Proper exception handling (no bare `except:`)

**Logging & Debugging:**
- [ ] No sensitive data in logs (credentials, API keys, PII)
- [ ] Debug logging controlled via environment variable
- [ ] Meaningful error messages (balance clarity with security)
- [ ] Timestamps included in log records

**Testing:**
- [ ] Security test cases added for new features
- [ ] Edge cases tested (negative values, max values, nulls)
- [ ] Error conditions tested
- [ ] Performance tests confirm no regressions

**Dependencies:**
- [ ] New dependencies reviewed for security history
- [ ] Dependency licenses compatible (EUPL-1.2)
- [ ] No deprecated or unmaintained libraries
- [ ] Version pinned (no floating versions)

**Documentation:**
- [ ] Security implications documented in code comments
- [ ] If applicable, PRs mention any security considerations in description
- [ ] Updates to SECURITY.md if procedures changed
- [ ] CHANGELOG entry for security fixes/changes

**Pre-Submission:**
- [ ] `make lint` passes (Ruff)
- [ ] `make type-check` passes (MyPy strict)
- [ ] `make test` passes (all tests)
- [ ] Pre-commit hooks pass locally (`pre-commit run --all-files`)

---

## Incident Response Plan

### Incident Severity Levels

| Level | Criteria | Example | Response Lead |
|-------|----------|---------|---|
| **Critical** | Production outage; data breach; RCE | Ransomware attack; database compromise | Lead Maintainer (Zakir) |
| **High** | Significant degradation; security incident | DoS attack; authentication bypass | Technical Lead (Olaf) |
| **Medium** | Partial service impairment | One feed failing; minor bug | Coordinator |
| **Low** | Minor issues; no security impact | Typo in documentation | Notification only |

### Incident Response Steps

1. **Detection & Alerting** (Continuous)
   - Monitoring alerts
   - User reports
   - Security scanner notifications

2. **Triage** (Within 1 hour)
   - Verify issue
   - Assess severity
   - Declare incident

3. **Communication** (Within 2 hours)
   - Notify incident team
   - Notify stakeholders (if critical)
   - Establish status page

4. **Mitigation** (Ongoing)
   - Implement temporary fix
   - Scale resources (if needed)
   - Isolate affected components

5. **Resolution** (Within X hours)
   - Deploy permanent fix
   - Validate resolution
   - Close incident

6. **Post-Incident** (Within 7 days)
   - Conduct blameless postmortem
   - Document lessons learned
   - Implement preventative measures

---

## Security Roadmap

### Planned Enhancements (v0.2+)

**Tier 1 (High Priority):**
- [ ] API key authentication (per-user endpoints)
- [ ] TLS verification enforcement
- [ ] Migrate from pickle to msgpack serialization
- [ ] Generate SBOM (Software Bill of Materials)

**Tier 2 (Medium Priority):**
- [ ] Rate limiting per authenticated user
- [ ] Request signing (HMAC-SHA256)
- [ ] OAuth 2.0 integration examples
- [ ] Security headers (CSP, X-Frame-Options, etc.)

**Tier 3 (Lower Priority):**
- [ ] Intrusion detection system (IDS)
- [ ] Formal security audit
- [ ] Penetration testing engagement
- [ ] SOC 2 Type II compliance

---

## Additional Resources

### External Security References

- **OWASP Cheat Sheets:** https://cheatsheetseries.owasp.org/
- **OWASP Top 10:** https://owasp.org/www-project-top-ten/
- **CWE/SANS Top 25:** https://cwe.mitre.org/top25/
- **Python Security Best Practices:** https://python.readthedocs.io/en/latest/library/security_warnings.html
- **NIST Cybersecurity Framework:** https://www.nist.gov/cyberframework
- **FastAPI Security:** https://fastapi.tiangolo.com/tutorial/security/

### Internal Documentation

- [Contributing Guide](/CONTRIBUTING.md) — Development requirements
- [CI Pipeline](/.github/workflows/ci.yml) — Automated security checks
- [ADR 0010: Real-time Feed Strategy](/docs/adr/0010_realtime_feed_strategy.md) — Feed security design
- [Reproducibility Guide](/docs/operations/reproducibility.md) — Operational security
- [Architecture Overview](/docs/architecture/overview.md) — System security design

---

## Contact & Support

**Security Team:**
- Zakir Bayramov (Lead): zakirbayramov942@gmail.com
- Gustav Olaf Yunus Laitinen-Lundström Fredriksson-Imanov (Technical): olaf.laitinen@uni.lu

**For Security Issues:** Email both maintainers; do NOT use public channels

**For General Questions:** Use GitHub Discussions

---

Document Control

- Owner: Security Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Restricted
- Contact: zakirbayramov942@gmail.com
