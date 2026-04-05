# Deployment Directory

| Field | Value |
|---|---|
| Owner | DevOps Team |
| Department | Infrastructure |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Container and orchestration configurations for runtime environment management.

**Purpose:** Define reproducible deployment specifications for development, staging, and production environments



## Overview

This directory contains deployment artifacts for:
- **Docker:** Containerization specifications
- **Kubernetes:** Container orchestration manifests
- **Infrastructure:** Service configuration and startup scripts
- **Monitoring:** Health checks and observability hooks



## Components

### Docker (docker/)

Container image definition and composition:

- `Dockerfile` - Multi-stage build for production image
- `docker-compose.yml` - Local development environment
- `.dockerignore` - Files excluded from build context

**Build production image:**

```bash
docker build -t stochastic-router:latest .
```

**Run locally with Docker Compose:**

```bash
docker-compose -f docker/docker-compose.yml up
```

### Kubernetes (deployment/kubernetes/)

Orchestration manifests for cluster deployment:

- `deployment.yaml` - Pod deployment specification
- `service.yaml` - Service exposure configuration
- `configmap.yaml` - Environment configuration
- `secrets.yaml` - Credential management template
- `ingress.yaml` - HTTP routing rules

**Deploy to cluster:**

```bash
kubectl apply -f deployment/kubernetes/deployment.yaml
kubectl apply -f deployment/kubernetes/service.yaml
```

### Infrastructure Scripts (deployment/scripts/)

Operational automation:

- `deploy.sh` - Automated deployment pipeline
- `health_check.sh` - Readiness and liveness probe
- `migration.sh` - Database schema initialization (future)
- `rollback.sh` - Deployment rollback procedure

**Run deployment:**

```bash
bash deployment/scripts/deploy.sh --environment production --version 0.1.0
```



## Deployment Process

### Local Development

```bash
# Build and run locally
docker-compose -f docker/docker-compose.yml up --build

# Service available at: http://localhost:8000
```

### Staging Environment

```bash
# Build image
docker build -t stochastic-router:staging .

# Tag for registry
docker tag stochastic-router:staging registry.example.com/stochastic-router:staging

# Push to registry
docker push registry.example.com/stochastic-router:staging

# Deploy to staging cluster
kubectl set image deployment/stochastic-router \
  stochastic-router=registry.example.com/stochastic-router:staging \
  -n staging
```

### Production Deployment

```bash
# Build and tag release
docker build -t stochastic-router:0.1.0 .
docker tag stochastic-router:0.1.0 registry.example.com/stochastic-router:0.1.0

# Push to registry
docker push registry.example.com/stochastic-router:0.1.0

# Deploy to production
bash deployment/scripts/deploy.sh --environment production --version 0.1.0

# Verify rollout
kubectl rollout status deployment/stochastic-router -n production
```



## Configuration

### Environment Variables

Configure via Kubernetes ConfigMap:

```yaml
# deployment/kubernetes/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: stochastic-router-config
data:
  LOG_LEVEL: "INFO"
  API_PORT: "8000"
  WORKERS: "4"
  GRAPH_PATH: "/data/graphs/nyc_latest.pkl"
```

### Secrets

Store sensitive data via Kubernetes Secrets:

```bash
# Create secret from environment file
kubectl create secret generic stochastic-router-secrets \
  --from-file=.env \
  -n production
```

**Required secrets:**
- GTFS_RT_API_KEY - Realtime feed API key
- DATABASE_URL - Database connection string (future)



## Health & Monitoring

### Health Checks

The deployment includes:

- **Startup probe:** Waits for graph loading (30s timeout)
- **Liveness probe:** Verifies API responsiveness (10s interval)
- **Readiness probe:** Confirms feed freshness (5s interval)

**Manual health check:**

```bash
curl http://localhost:8000/api/health
```

**Response:**

```json
{
  "status": "healthy",
  "version": "0.1.0",
  "graph_loaded": true,
  "feeds_updated": "2026-04-05T14:32:00Z"
}
```

### Logging

Logs are written to stdout for container log aggregation:

```bash
# View logs
kubectl logs deployment/stochastic-router -n production

# Stream logs
kubectl logs -f deployment/stochastic-router -n production
```

### Metrics

Prometheus metrics exposed at `/metrics`:

```bash
curl http://localhost:8000/metrics
```

**Tracked metrics:**
- Request latency (ms)
- Route computation time (ms)
- API error rates
- Graph load time (ms)
- Feed freshness age (hours)



## Resource Requirements

### Minimum (Development)

```yaml
resources:
  requests:
    cpu: 500m
    memory: 512Mi
  limits:
    cpu: 1000m
    memory: 1Gi
```

### Recommended (Production)

```yaml
resources:
  requests:
    cpu: 2000m
    memory: 4Gi
  limits:
    cpu: 4000m
    memory: 8Gi
```

**Rationale:**
- Graph loading: ~2 GB memory for NYC
- Request handling: ~500m CPU per concurrent request
- Headroom: 50% above typical load



## Rollback Procedure

If deployment issues occur:

```bash
# Quick rollback to previous version
kubectl rollout undo deployment/stochastic-router -n production

# Verify rollback
kubectl rollout status deployment/stochastic-router -n production

# Or manual rollback script
bash deployment/scripts/rollback.sh --target previous
```



## Troubleshooting

| Issue | Solution |
|-------|----------|
| Pod fails to start | Check logs: kubectl logs pod-name; verify resources allocated |
| High latency | Monitor CPU/memory; check graph load time in liveness probe |
| Feed not updating | Verify API key in secrets; check feed freshness endpoint |
| Deployment timeout | Increase startup probe timeout in Kubernetes manifest |
| Container won't pull | Check registry credentials in imagePullSecrets |



## Related

- [Docker Image Definition](/docker/Dockerfile)
- [Docker Compose](/docker/docker-compose.yml)
- [Kubernetes Deployment](/deployment/kubernetes/deployment.yaml)
- [Architecture Overview](/docs/architecture/overview.md)
- [Security Policy](/SECURITY.md)

---

Document Control

- Owner: DevOps Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
