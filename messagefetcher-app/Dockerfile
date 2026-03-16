FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install the necessary libraries
# We do this before copying code to take advantage of Docker caching
RUN pip install flask requests

# Copy your local scripts into the container
COPY . .

# We leave the CMD empty because we will define which 
# script to run (frontend vs backend) in the compose file
