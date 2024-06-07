# Use an official Python runtime as a parent image
FROM python:3.10-slim AS base

# Install git to handle submodules
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Create and activate a virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use an official Node.js runtime as a parent image
FROM node:18-slim AS node_base

# Install npx globally
RUN npm install -g npx --force

# Use the base image
FROM base AS final

# Set the working directory in the container
WORKDIR /app

# Copy the installed npx from the Node.js image
COPY --from=node_base /usr/local/bin/npx /usr/local/bin/npx

# Copy the rest of the application code
COPY . .

# Copy the .env file into the container
COPY .env .

# Initialize and update git submodules
RUN git submodule init && git submodule update

# Define the command to run the application
CMD ["python", "-m", "app.main"]
