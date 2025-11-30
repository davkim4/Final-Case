#!/bin/bash
docker build -t etl-api .
docker run -p 5000:5000 etl-api