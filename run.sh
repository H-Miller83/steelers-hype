#!/bin/bash

# Build Docker image
docker build -t steelers-hype-app .

# Run container
docker run -p 8080:8080 steelers-hype-app
