#!/bin/bash
docker build -t etl-api .
docker run -p 5050:5000 etl-api