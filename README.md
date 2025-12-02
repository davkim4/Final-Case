# Final-Case

## 1) Executive Summary
### Problem
Organizations often receive raw numerical data that varies widely in scale and meaning. Stakeholders need a simple, interpretable way to understand whether a given item is significant or not significant, instead of looking at raw numeric values. The challenge is that:
- The raw numbers may not be normalized
- Some values should have more influence on the final score
- Decision-makers often just need a simple High or Low label
- The score must be computed consistently and automatically

### Solution 
This project provides a containerized ETL microservice that reads raw JSON input, normalizes each value, computes a weighted quality score, and classifies each item as either High or Low. The system uses squared scoring to amplify large differences—high raw values contribute much more to the final score after squaring, helping the microservice better identify truly significant cases. The cleaned data and classification are saved to src/processed.json and exposed through a stable Flask API.

## 2) System Overview
### Course Concepts
This project implements the following:
Containerization (Docker) – reproducible execution environment
Microservices – API exposing /run and /data
ETL Pipelines – Extract–Transform–Load via Pandas
CI Automation – GitHub Actions that build, test, and lint the service
Cloud Deployment (optional) – Azure Container Apps / Container Registry

### Architecture Diagram

### Data / Models / Services
Raw Data - src/db.json (10 rows of simple numeric values)
Processed Data - src/processed.json (Enriched with tags and squared values)
API Service - Flask app exposing /run (start ETL) and /data (return processed output)
Docker Image - ~420MB Python 3.11 slim container
CI Pipeline - GitHub Actions workflow running pytest

## 3) How to Run (Local)
### Docker
```bash
# build
docker build -t etl-api .

# run
docker run --rm -p 5050:5000 etl-api

# trigger ETL
curl http://localhost:5050/run

# view processed data
curl http://localhost:5050/data
```

## 4) Design Decisions
### Why this concept?
I chose a containerized ETL microservice because it touches on key course concepts: reproducibility, API design, automation, and deployment. Docker ensures anyone can run the service identically across machines. On the other hand, the alternatives of FastAPI, Airflow/Prefect, and SQL database were unused for the reasons of being overkill for simple ETL API (FastAPI), too heavy for a small project (Airflow/Prefect), and because JSON-only was simpler and met requirements (SQL database).

Alternatives Considered:

### Tradeoffs
Simplicity vs Scalability: Flask is lightweight but not ideal for large-scale ETL.
JSON I/O vs Database: Easy to use; less flexible for large datasets.
Single-file container: Fast demo; not production-grade structure.

### Security & Privacy
.env.example created to avoid committing secrets.
No PII data.
Input files are validated implicitly via Pandas parsing.

### Ops
Custom logger in src/logger.py
No metrics system yet (future improvement)
Can be scaled horizontally if deployed as a container app

## 5) Results & Evaluation
### Sample Outputs
/run → triggers ETL
/data → returns processed JSON like:
```json
[
  {"id": 1, "value": 10, "value_squared": 100, "tag": "low"},
  {"id": 7, "value": 99, "value_squared": 9801, "tag": "high"}
]
```

### Tests
tests/test_api.py includes smoke tests for both endpoints.
CI runs the test suite automatically on every push.

### Performance
ETL completes < 0.1s for 10 rows.
Memory footprint extremely small (<100MB during runtime).

### Screenshots

## 6) What's Next
### Planned improvements
Deploy final image to Azure Container Apps (extra credit)
Add /health and /metrics endpoints
Add input validation and error handling
Add caching for repeated reads
Add API query filters (e.g., /data?tag=high)
Add optional PostgreSQL backend
Add automated load tests in CI

## 7) Links
Github Repo: github.com/davkim4/Final-Case
Public Cloud App: 
