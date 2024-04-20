# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libboost-all-dev \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the local directory contents into the container
COPY . /usr/src/app

# Install Python packages
RUN pip install camel-tools pandas elasticsearch

# Run script.py when the container launches
CMD ["python", "./camel_tools_analyzer.py"]
